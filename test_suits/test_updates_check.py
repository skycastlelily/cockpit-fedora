import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_updates_check import UpdatesCheckPage


class TestUpdatesCheck(UpdatesCheckPage):
    """
    :avocado: enable
    :avocado: tags=updates
    """
   # new_user_select = "//div[@class='cockpit-account-user-name'][text() = '%s']" % 'test2'
    def test_check_updates(self):
        self.check_updates()
        #self.assert_element_visible(self.new_user_select)


