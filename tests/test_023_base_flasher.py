from unittest import TestCase
from unittest.mock import MagicMock, patch

from serial import SerialException
from src.utils.flasher.base_flasher import BaseFlasher
from .shared_mocks import MockListPortsGrep


class TestBaseFlasher(TestCase):

    @patch("os.path.exists", return_value=True)
    def test_set_firmware(self, mock_exists):
        b = BaseFlasher()
        b.firmware = "mock/test/kboot.kfpkg"
        mock_exists.assert_called_once_with("mock/test/kboot.kfpkg")

    @patch("os.path.exists", return_value=False)
    def test_fail_set_firmware(self, mock_exists):
        with self.assertRaises(ValueError) as exc_info:
            b = BaseFlasher()
            b.firmware = "mock/test/kboot.kfpkg"
            mock_exists.assert_called_once_with("mock/test/kboot.kfpkg")

        self.assertEqual(
            str(exc_info.exception), "File do not exist: mock/test/kboot.kfpkg"
        )

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_amigo(self, mock_grep):
        f = BaseFlasher()
        f.port = "amigo"
        mock_grep.assert_called_once_with("0403")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_amigo_tft(self, mock_grep):
        f = BaseFlasher()
        f.port = "amigo_tft"
        mock_grep.assert_called_once_with("0403")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_amigo_ips(self, mock_grep):
        f = BaseFlasher()
        f.port = "amigo_ips"
        mock_grep.assert_called_once_with("0403")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_m5stickv(self, mock_grep):
        f = BaseFlasher()
        f.port = "m5stickv"
        mock_grep.assert_called_once_with("0403")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_bit(self, mock_grep):
        f = BaseFlasher()
        f.port = "bit"
        mock_grep.assert_called_once_with("0403")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_ports_cube(self, mock_grep):
        f = BaseFlasher()
        f.port = "cube"
        mock_grep.assert_called_once_with("0403")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_dock(self, mock_grep):
        f = BaseFlasher()
        f.port = "dock"
        mock_grep.assert_called_once_with("7523")

    @patch(
        "src.utils.flasher.base_flasher.list_ports.grep", new_callable=MockListPortsGrep
    )
    def test_set_port_yahboom(self, mock_grep):
        f = BaseFlasher()
        f.port = "yahboom"
        mock_grep.assert_called_once_with("7523")

    def test_fail_set_port(self):
        with self.assertRaises(ValueError) as exc_info:
            f = BaseFlasher()
            f.port = "mock"

        self.assertEqual(str(exc_info.exception), "Device not implemented: mock")

    def test_set_board_amigo(self):
        f = BaseFlasher()
        f.board = "amigo"
        self.assertEqual(f.board, "goE")

    def test_set_board_amigo_tft(self):
        f = BaseFlasher()
        f.board = "amigo_tft"
        self.assertEqual(f.board, "goE")

    def test_set_board_amigo_ips(self):
        f = BaseFlasher()
        f.board = "amigo_ips"
        self.assertEqual(f.board, "goE")

    def test_set_board_m5stickv(self):
        f = BaseFlasher()
        f.board = "m5stickv"
        self.assertEqual(f.board, "goE")

    def test_set_board_bit(self):
        f = BaseFlasher()
        f.board = "bit"
        self.assertEqual(f.board, "goE")

    def test_set_board_dock(self):
        f = BaseFlasher()
        f.board = "dock"
        self.assertEqual(f.board, "dan")

    def test_set_board_yahboom(self):
        f = BaseFlasher()
        f.board = "yahboom"
        self.assertEqual(f.board, "goE")

    def test_set_board_cube(self):
        f = BaseFlasher()
        f.board = "cube"
        self.assertEqual(f.board, "goE")

    def test_fail_set_board(self):
        with self.assertRaises(ValueError) as exc_info:
            f = BaseFlasher()
            f.board = "mock"
        self.assertEqual(str(exc_info.exception), "Device not implemented: mock")

    def test_set_print_callback(self):
        f = BaseFlasher()
        f.print_callback = MagicMock()
        f.print_callback()
        f.print_callback.assert_called_once()

    @patch("src.utils.flasher.base_flasher.Serial", side_effect=SerialException())
    def test_fail_is_port_working(self, mock_serial):

        f = BaseFlasher()
        result = f.is_port_working(port="mock")
        self.assertFalse(result)

        mock_serial.assert_called_once_with("mock")

    @patch("src.utils.flasher.base_flasher.Serial")
    def test_is_port_working(self, mock_serial):

        f = BaseFlasher()
        result = f.is_port_working(port="mock")
        self.assertTrue(result)

        mock_serial.assert_called_once_with("mock")
