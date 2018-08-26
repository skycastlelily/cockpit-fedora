import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_container_check import DockerCheckPage


class TestDockerCheck(DockerCheckPage):
    """
    :avocado: enable
    :avocado: tags=docker
    """
    CONTAINER_FILTER = "#containers-filter"
#    def test_startcontainer(self):
 #       self.start_container()
  #      self.assert_element_visible(self.CONTAINER_FILTER)

    def test_runcontainer(self):
        self.run_container()
        container_status = self.get_container_status()
        self.assertEqual(container_status,'running')
