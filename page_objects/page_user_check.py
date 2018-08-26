from time import sleep
import xmltodict
from seleniumlib import SeleniumTest
from utils.machine import RunCmdError



class UserCheckPage(SeleniumTest):
    """
    :avocado: disable
    """

    USER_CREATE_LINK = "#sidebar-menu a[href='/users']"
    USER_FRAME_NAME = "/users"
    CREATE_USER_BUTTON = "#accounts-create"
    SELECT_THE_USER =  "//div[contains(text(), '%s')]"
    SET_PASSWORD_BUTTON = "#account-set-password"
    # we can put the following param into config.yml,but don't think it's neccessary
    create_username = 'test2'
    old_password = 'testcockpit'
    new_password = 'testfedora'

    def create_user(self):
        # login page elements
        self.hover_and_click(self.CREATE_USER_BUTTON)
        user_realname_input = "#accounts-create-real-name"
        user_username_input = "#accounts-create-user-name"
        user_passwd_input = "#accounts-create-pw1"
        user_passwd2_input = "#accounts-create-pw2"
        create_button = "#accounts-create-create"

        self.input_text(user_realname_input, self.create_username)
        self.input_text(user_username_input, self.create_username)
        self.input_text(user_passwd_input, self.old_password)
        self.input_text(user_passwd2_input, self.old_password)
        self.hover_and_click(create_button)

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
        self.click(self.USER_CREATE_LINK)
        self.switch_to_frame(self.USER_FRAME_NAME)


