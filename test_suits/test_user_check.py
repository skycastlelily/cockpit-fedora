import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_user_check import UserCheckPage


class TestUserCheck(UserCheckPage):
    """
    :avocado: enable
    :avocado: tags=user
    """
    new_user_select = "//div[@class='cockpit-account-user-name'][text() = '%s']" % 'test2'
    def test_create_user(self):
        self.create_user()
        self.assert_element_visible(self.new_user_select)

    def test_chpassword(self):
        self.ch_password()

    def test_delete_user(self):
        self.delete_user()
        self.assert_element_invisible(self.new_user_select)

