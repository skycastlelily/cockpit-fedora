import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from page_objects.page_storage_check import StorageCheckPage


class TestStorageCheck(StorageCheckPage):
    """
    :avocado: enable
    :avocado: tags=storage
    """
    def test_nfs_mount(self):
        self.add_nfs_mount()
        self.assert_element_visible(self.nfs_mount_click % self.server_path)

    def test_nfs_umount(self):
        nfs_mount_button = "//button[text()='Mount']"
        self.umount_nfs_mount()
        self.assert_element_visible(nfs_mount_button)

    def test_nfs_remount(self):
        nfs_unmount_button = "//button[text()='Unmount']"
        self.remount_nfs_mount()
        self.assert_element_visible(nfs_unmount_button)

    def test_nfs_edit(self):
        #nfs_editmount_click = "//td[text()='%s')]" % self.edit_path
        self.edit_nfs_mount()

    def test_delete_mount(self):
        none_nfs_mount = "//div[contains(@class,'empty-panel-text')]"
        self.delete_nfs_mount()
        self.assert_element_visible(none_nfs_mount)

