from time import sleep
import xmltodict
from seleniumlib import SeleniumTest
from utils.machine import RunCmdError



class DockerCheckPage(SeleniumTest):
    """
    :avocado: disable
    """

    DOCKER_LINK = "#sidebar-menu a[href='/docker']"
    DOCKER_FRAME_NAME = "/docker"
    #DOCKER_START_BUTTON = "//*[@class=blank-state-pf-main-action and data-action='docker-start']"
    DOCKER_START_BUTTON = "//*[@data-action='docker-start']"
    #DOCKER_RUN_BUTTON = "//*[@class='btn btn-default btn-control-ct fa fa-play']"
    DOCKER_RUN_BUTTON = "//button[contains(@class, 'fa-play')]"
    DOCKER_RUN_COMMAND = "#containers-run-image-command"
    DOCKER_RUN_RUN = "#containers-run-image-run"

    def open_page(self):
        self.click(self.DOCKER_LINK)
        self.switch_to_frame(self.DOCKER_FRAME_NAME)

    def start_container(self, username='lnie',passwd='testredhat'):
        self.hover_and_click(self.DOCKER_START_BUTTON)
        sleep(self.WAIT_DOCKER_START)

        #user_realname_input = "#accounts-create-real-name"

        #self.input_text(user_passwd2_input, passwd)
        #self.hover_and_click(create_button)
    def run_container(self,command='/bin/bash'):
        self.hover_and_click(self.DOCKER_RUN_BUTTON)
        sleep(2)
        self.input_text(DOCKER_RUN_COMMAND,command )
        self.hover_and_click(self.DOCKER_RUN_RUN)
        sleep(3)
    def get_container_status(self):
        container_run_status="tbody:nth-child(1) tr:nth-child(1) td:nth-child(6)"
        self.get_text(container_run_status)






