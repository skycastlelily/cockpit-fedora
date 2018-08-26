import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_terminal_check import TerminalCheckPage


class TestTerminalCheck(TerminalCheckPage):
    """
    :avocado: enable
    :avocado: tags=terminal
    """
   # new_user_select = "//div[@class='cockpit-account-user-name'][text() = '%s']" % 'test2'
    def test_cmd_user(self):
        self.input_somecommand()
        #self.assert_element_visible(self.new_user_select)


