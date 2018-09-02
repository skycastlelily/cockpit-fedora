import os
from time import sleep
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_container_check import DockerCheckPage


class TestDockerCheck(DockerCheckPage):
    """
    :avocado: enable
    :avocado: tags=docker
    """
    SELECT_BUTTON = "div#containers-containers-filter>button"
    SELECT_RUNNING_CONTAINER = "//li[@data-value='Images and running containers']"
    SELECT_EVERYTHING = "//li[@data-value='Everything']"
    CONTAINER_FILTER = "#containers-filter"
    container_running_text = "//td[text()='running']"
    container_exited_text = "//td[text()='exited']" 
    image_pull_name = "//th[contains(text(), 'nginx')]"
    def test_startcontainer(self):
        self.start_container()
        self.assert_element_visible(self.CONTAINER_FILTER)

    def test_pull_image(self):
        self.docker_pull_image()
        self.assert_element_visible(self.image_pull_name)

    def test_cmdrun(self):
        self.click(self.SELECT_BUTTON)
        self.hover_and_click(self.SELECT_RUNNING_CONTAINER)
        self.run_container_cmd()
        self.assert_element_visible(self.container_running_text)
        self.assert_element_invisible(self.container_exited_text)

    def test_everything(self):
        self.click(self.SELECT_BUTTON)
        self.hover_and_click(self.SELECT_EVERYTHING)
        sleep(3)
        self.assert_element_visible(self.container_running_text)
        self.assert_element_visible(self.container_exited_text)
        def test_cmd_stop(self):
        self.stop_container_cmd()
        self.assert_element_invisible(self.container_running_text)

    def test_cmd_delete(self):
        running_container_name = "//th[text()='extending']"
        self.delete_container_cmd()
        self.assert_element_invisible(running_container_name)

    def test_remove_image(self):
        self.docker_rm_image()
        self.assert_element_invisible(self.image_pull_name)


