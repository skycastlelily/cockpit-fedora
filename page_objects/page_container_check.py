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
    WAIT_DOCKER_START=20
    DOCKER_RUN_BUTTON = "div#containers-images>div>table>tbody>tr>td:nth-of-type(6)>button"
    #DOCKER_RUN_BUTTON = "div#containers-images>div>table"
    DOCKER_RUN_COMMAND = "#containers-run-image-command"
    DOCKER_RUN_RUN = "#containers-run-image-run"

    def open_page(self):
        self.click(self.DOCKER_LINK)
        self.switch_to_frame(self.DOCKER_FRAME_NAME)

    def start_container(self):
        self.hover_and_click(self.DOCKER_START_BUTTON)
        sleep(self.WAIT_DOCKER_START) 
   
    def docker_pull_image(self):
        cmd = "docker pull nginx"
        self.host.execute(cmd)

    def docker_rm_image(self):
        cmd = "docker rmi nginx"
        self.host.execute(cmd)

    def run_container_cmd(self):
        cmd = "docker run --name extending -d nginx"
        self.host.execute(cmd)
        sleep(2)
        cmd = "docker run -it --name flash fedora ls"
        self.host.execute(cmd)

    def stop_container_cmd(self,name_id="extending"):
        cmd = " docker stop '%s' " % name_id
        self.host.execute(cmd)

    def delete_container_cmd(self,name_id="extending"):
        cmd = " docker rm '%s' " % name_id
        self.host.execute(cmd)

   
    def run_container_ui(self,command='/bin/bash'):
        self.hover_and_click(self.DOCKER_RUN_BUTTON)
        sleep(2)
        self.input_text(DOCKER_RUN_COMMAND,command )
        self.hover_and_click(self.DOCKER_RUN_RUN)
        sleep(3)

    def get_container_status(self):
        container_run_status="tbody:nth-child(1) tr:nth-child(1) td:nth-child(6)"
        self.get_text(container_run_status)





