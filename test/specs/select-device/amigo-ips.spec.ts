import { expect as expectChai } from 'chai'
import { expect as expectWDIO } from '@wdio/globals'
import delay from '../delay'
import Main from '../../pageobjects/main.page'
import SelectDevice from '../../pageobjects/select-device.page'

// eslint-disable-next-line no-undef
describe('SelectDevicePage: page select \'amigo_ips\' option', () => {

  // eslint-disable-next-line no-undef
  before(async () => {
    await Main.selectDeviceButton.click()
    await delay(1000)
    await SelectDevice.formArrow.click()
    await delay(1000)
  })

  // eslint-disable-next-line no-undef
  it('should be in SelectDevicePage', async () => {
    await expectWDIO(SelectDevice.page).toBeDisplayed()
  })

  // eslint-disable-next-line no-undef
  it('should be selected', async () => {    
    await SelectDevice.list_item_amigo_ips.click()
    await delay(1000)
    await expectWDIO(SelectDevice.formSelected).toHaveText('maixpy_amigo_ips')
  })

  // eslint-disable-next-line no-undef
  it('should click \'select\' go out of SelectDevicePage', async () => {   
    await SelectDevice.formSelectButton.click()
    await delay(1000)
    await expectWDIO(SelectDevice.page).not.toBeDisplayed() 
  })

  // eslint-disable-next-line no-undef
  it('should the \'select device\' changed to \'maixpy_amigo_ips\'', async () => {  
    const deviceButtonText = await Main.selectDeviceButton.$('span.v-btn__content').getText()    
    expectChai(deviceButtonText).not.to.be.equal(' SELECT_DEVICE')
    expectChai(deviceButtonText).to.be.equal(' MAIXPY_AMIGO_IPS')
  })    
})
