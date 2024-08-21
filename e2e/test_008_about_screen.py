import os
from unittest.mock import patch, MagicMock, call
from kivy.base import EventLoop, EventLoopBase
from kivy.tests.common import GraphicUnitTest
from kivy.core.text import LabelBase, DEFAULT_FONT
from src.app.screens.about_screen import AboutScreen


class TestAboutScreen(GraphicUnitTest):

    @classmethod
    def setUpClass(cls):
        cwd_path = os.path.dirname(__file__)
        rel_assets_path = os.path.join(cwd_path, "..", "assets")
        assets_path = os.path.abspath(rel_assets_path)
        terminus_path = os.path.join(assets_path, "terminus.ttf")
        nanum_path = os.path.join(assets_path, "NanumGothic-Regular.ttf")
        LabelBase.register(name="terminus", fn_regular=terminus_path)
        LabelBase.register(name="nanum", fn_regular=nanum_path)
        LabelBase.register(DEFAULT_FONT, terminus_path)

    @classmethod
    def teardown_class(cls):
        EventLoop.exit()

    @patch.object(EventLoopBase, "ensure_window", lambda x: None)
    @patch(
        "src.app.screens.base_screen.BaseScreen.get_locale", return_value="en_US.UTF-8"
    )
    def test_render_main_screen(self, mock_get_locale):
        screen = AboutScreen()
        self.render(screen)

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window
        grid = window.children[0].children[0]
        label = grid.children[0]

        self.assertEqual(window.children[0], screen)
        self.assertEqual(screen.name, "AboutScreen")
        self.assertEqual(screen.id, "about_screen")
        self.assertEqual(grid.id, "about_screen_grid")
        self.assertEqual(label.id, "about_screen_label")

        text = "\n".join(
            [
                "".join(
                    [
                        "[font=terminus]",
                        f"[size={screen.SIZE_G}sp]",
                        "[color=#00AABB]",
                        "[ref=SourceCode][b]v0.0.2-alpha[/b][/ref]",
                        "[/color]",
                        "[/size]",
                        "[/font]",
                    ]
                ),
                "",
                "",
                "".join(
                    [
                        "[font=terminus]",
                        f"[size={screen.SIZE_M}sp]",
                        "follow us on X: [color=#00AABB][ref=X]@selfcustodykrux[/ref][/color]",
                        "[/size]",
                        "[/font]",
                    ]
                ),
                "",
                "",
                "".join(
                    [
                        "[font=terminus]",
                        f"[size={screen.SIZE_M}sp]",
                        "[color=#00FF00]",
                        "[ref=Back]",
                        "Back",
                        "[/ref]",
                        "[/color]",
                        "[/size]",
                        "[/font]",
                    ]
                ),
            ]
        )

        self.assertEqual(label.text, text)
        mock_get_locale.assert_has_calls([call(), call(), call(), call()])

    @patch.object(EventLoopBase, "ensure_window", lambda x: None)
    @patch(
        "src.app.screens.base_screen.BaseScreen.get_locale", return_value="pt_BR.UTF-8"
    )
    def test_update_locale(self, mock_get_locale):
        screen = AboutScreen()
        self.render(screen)

        # get your Window instance safely
        EventLoop.ensure_window()
        window = EventLoop.window
        grid = window.children[0].children[0]
        label = grid.children[0]

        screen.update(name="ConfigKruxInstaller", key="locale", value="pt_BR.UTF-8")

        text = "\n".join(
            [
                "".join(
                    [
                        "[font=terminus]",
                        f"[size={screen.SIZE_G}sp]",
                        "[color=#00AABB]",
                        "[ref=SourceCode][b]v0.0.2-alpha[/b][/ref]",
                        "[/color]",
                        "[/size]",
                        "[/font]",
                    ]
                ),
                "",
                "",
                "".join(
                    [
                        "[font=terminus]",
                        f"[size={screen.SIZE_M}sp]",
                        "siga-nos no X: [color=#00AABB][ref=X]@selfcustodykrux[/ref][/color]",
                        "[/size]",
                        "[/font]",
                    ]
                ),
                "",
                "",
                "".join(
                    [
                        "[font=terminus]",
                        f"[size={screen.SIZE_M}sp]",
                        "[color=#00FF00]",
                        "[ref=Back]",
                        "Voltar",
                        "[/ref]",
                        "[/color]",
                        "[/size]",
                        "[/font]",
                    ]
                ),
            ]
        )
        self.assertEqual(label.text, text)
        mock_get_locale.assert_has_calls(
            [call(), call(), call(), call(), call(), call(), call()]
        )

    @patch.object(EventLoopBase, "ensure_window", lambda x: None)
    @patch(
        "src.app.screens.base_screen.BaseScreen.get_locale", return_value="en_US.UTF-8"
    )
    @patch("src.app.screens.about_screen.webbrowser")
    def test_on_press_version(self, mock_webbrowser, mock_get_locale):
        mock_webbrowser.open = MagicMock()

        screen = AboutScreen()
        self.render(screen)

        # get your Window instance safely
        EventLoop.ensure_window()

        action = getattr(screen, "on_ref_press_about_screen_label")
        action("Mock", "SourceCode")

        mock_get_locale.assert_has_calls([call(), call(), call(), call()])
        mock_webbrowser.open.assert_called_once_with(
            "https://selfcustody.github.io/krux/getting-started/installing/from-gui/"
        )

    @patch.object(EventLoopBase, "ensure_window", lambda x: None)
    @patch(
        "src.app.screens.base_screen.BaseScreen.get_locale", return_value="en_US.UTF-8"
    )
    @patch("src.app.screens.about_screen.webbrowser")
    def test_on_press_x_formerly_known_as_twitter(
        self, mock_webbrowser, mock_get_locale
    ):
        mock_webbrowser.open = MagicMock()

        screen = AboutScreen()
        self.render(screen)

        # get your Window instance safely
        EventLoop.ensure_window()

        action = getattr(screen, "on_ref_press_about_screen_label")
        action("Mock", "X")

        mock_get_locale.assert_has_calls([call(), call(), call(), call()])
        mock_webbrowser.open.assert_called_once_with("https://x.com/selfcustodykrux")

    @patch.object(EventLoopBase, "ensure_window", lambda x: None)
    @patch(
        "src.app.screens.base_screen.BaseScreen.get_locale", return_value="en_US.UTF-8"
    )
    @patch("src.app.screens.about_screen.AboutScreen.set_screen")
    def test_on_press_back(self, mock_set_screen, mock_get_locale):
        screen = AboutScreen()
        self.render(screen)

        # get your Window instance safely
        EventLoop.ensure_window()

        action = getattr(screen, "on_ref_press_about_screen_label")
        action("Mock", "Back")

        mock_get_locale.assert_has_calls([call(), call(), call()])
        mock_set_screen.assert_called_once_with(name="MainScreen", direction="right")
