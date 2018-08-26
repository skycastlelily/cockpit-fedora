from time import sleep
import xmltodict
from seleniumlib import SeleniumTest
from utils.machine import RunCmdError



class NETWORKCheckPage(SeleniumTest):
    """
    :avocado: disable
    """

    NETWORK_LINK = "#sidebar-menu a[href='/network']"
    NETWORK_FRAME_NAME = "/network"
    SELECT_FIREWALL_STATUS="//span[contains(text(), '%s')]"

    def get_firewall_status_ui(self):

        firewall_status_button="//label[contains(@class,'btn active')]"
        return self.get_text(firewall_status_button)

    def get_firewall_status_cmd(self):
        firewall_status = self.get_firewall_status_ui()
        if firewall_status == 'ON':
            cmd = 'systemctl status firewalld | grep "running"'
            cmd_status='ON'
        else:
            cmd = 'systemctl status firewalld | grep "dead"'
            cmd_status='OFF'
        result = self.host.execute(cmd)
        if result:
            return cmd_status
        else:
            return 'FAIL'

    def change_firewallstatus_ui(self):
        # login page elements
        firewall_status = self.get_firewall_status_ui()
        if firewall_status == 'ON':
            change_status_to = self.SELECT_FIREWALL_STATUS % "Off"
            change_status_string='OFF'
        else:
            change_status_to = self.SELECT_FIREWALL_STATUS % "On"
            change_status_string='ON'
        self.click(change_status_to)
        sleep(5)
        return change_status_string



    def open_page(self):
        self.click(self.NETWORK_LINK)
        self.switch_to_frame(self.NETWORK_FRAME_NAME)

        #self.click(self.USER_FRAME_NAME)
        #self.driver.switch_to.frame(self.USER_FRAME_NAME)

