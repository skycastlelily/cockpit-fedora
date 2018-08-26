from time import sleep
import xmltodict
from seleniumlib import SeleniumTest
from utils.machine import RunCmdError



class UpdatesCheckPage(SeleniumTest):
    """
    :avocado: disable
    """
    WAIT_PAGE_LOAD = 70
    WAIT_SOFTWARE_LOAD  = 40
    UPDATES_CREATE_LINK = "#sidebar-tools a[href='/updates']"
    UPDATES_FRAME_NAME = "/updates"
    CHECK_UPDATE_BUTTON = "//button[text()='Check for Updates']"
    INSTALL_UPDATE_BUTTON = "//button[text()='Install All Updates']"
    UPDATE_PROGRESS_BAR = "//div[contains(@class,'progress-main-view')]"
    INPUT_COMMAND = "//div[contains(text(), 'localhost')]"
    CREATE_USER_BUTTON = "#accounts-create"
    SELECT_THE_USER =  "//div[contains(text(), '%s')]"
    SET_PASSWORD_BUTTON = "#account-set-password"

    def check_updates(self):
        sleep(self.WAIT_PAGE_LOAD)
        self.click(self.CHECK_UPDATE_BUTTON)
        self.assert_element_visible(self.UPDATE_PROGRESS_BAR)
        sleep(self.WAIT_SOFTWARE_LOAD)
        self.assert_element_visible(self.INSTALL_UPDATE_BUTTON)


    def open_page(self):
        self.click(self.UPDATES_CREATE_LINK)
        self.switch_to_frame(self.UPDATES_FRAME_NAME)


