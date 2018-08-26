from time import sleep
import xmltodict
from seleniumlib import SeleniumTest
from utils.machine import RunCmdError



class TerminalCheckPage(SeleniumTest):
    """
    :avocado: disable
    """

    TERMINAL_CREATE_LINK = "#sidebar-tools a[href='/system/terminal']"
    TERMINAL_FRAME_NAME = "/terminal"
    INPUT_COMMAND = "//div[contains(text(), 'localhost')]"
    CREATE_USER_BUTTON = "#accounts-create"
    SELECT_THE_USER =  "//div[contains(text(), '%s')]"
    SET_PASSWORD_BUTTON = "#account-set-password"
    # we can put the following param into config.yml,but don't think it's neccessary
    create_username = 'test2'
    old_password = 'testcockpit'
    new_password = 'testfedora'

    def input_somecommand(self):
        # login page elements
        sleep(2)
        self.driver.find_element_by_xpath(self.INPUT_COMMAND).send_keys('useradd test3\n')
        sleep(3)
        #self.input_text(user_username_input, self.create_username)
        #self.hover_and_click(create_button)

    def delete_user(self):

        DELETE_USER_CLICK = self.SELECT_THE_USER % self.create_username
        DELETE_USER_BUTTON = "#account-delete"
        DELETE_FILES_CHECKBOX = "#account-confirm-delete-files"
        delete_account_apply = "#account-confirm-delete-apply"
        self.click(DELETE_USER_CLICK)
        self.hover_and_click(DELETE_USER_BUTTON)
        self.click(DELETE_FILES_CHECKBOX)
        self.click(delete_account_apply)
        sleep(3)

    def ch_password(self):

        CHANGE_PASSWORD_CLICK = self.SELECT_THE_USER % self.create_username
        #old_password_input = "#account-set-password-old"
        new_password_input = "#account-set-password-pw1"
        new_password_confirm = "#account-set-password-pw2"
        change_password_apply = "#account-set-password-apply"

        self.click(CHANGE_PASSWORD_CLICK)
        self.hover_and_click(self.SET_PASSWORD_BUTTON)
        #self.input_text(old_password_input, self.old_password)
        self.input_text(new_password_input, self.new_password)
        self.input_text(new_password_confirm, self.new_password)
        self.hover_and_click(change_password_apply)
        sleep(3)


    def open_page(self):
        self.click(self.TERMINAL_CREATE_LINK)
        self.switch_to_frame(self.TERMINAL_FRAME_NAME)


