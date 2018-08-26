import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_network_check import NETWORKCheckPage


class TestNetworkCheck(NETWORKCheckPage):
    """
    :avocado: enable
    :avocado: tags=network
    """


    def test_changestatus_ui(self):
        change_status_string = self.change_firewallstatus_ui()
        firewall_status_now = self.get_firewall_status_ui()
        self.assertEqual(change_status_string,firewall_status_now)
    def test_changestatus_same(self):
        firewall_status_ui = self.get_firewall_status_ui()
        firewall_status_cmd = self.get_firewall_status_cmd()
        self.assertEqual(firewall_status_ui,firewall_status_cmd)

#    def test_chpassword(self):
 #       self.ch_password()
