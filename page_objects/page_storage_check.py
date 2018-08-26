import os
from time import sleep
import xmltodict
from seleniumlib import SeleniumTest
from utils.machine import RunCmdError


class StorageCheckPage(SeleniumTest):
    """
    :avocado: disable
    """
    nfs_address = os.environ.get('NFS_ADDRESS')
    server_path = os.environ.get('SERVER_PATH')
    local_path = os.environ.get('LOCAL_PATH')
    edit_path = os.environ.get('EDIT_PATH')
   # MACHINES_LINK = "#sidebar-menu a[href='/machines']"
    #USER_FRAME_NAME = "#host-apps a[href='/users']"
    STORAGE_LINK = "#sidebar-menu a[href='/storage']"
    STORAGE_FRAME_NAME = "/storage"
    BUTTON_NFS_MOUNT = "//button[contains(@class, 'btn-primary')]"
    nfs_mount_click = "//td[contains(text(), '%s')]"

    def add_nfs_mount(self):
        nfs_server_address = "//input[@class='form-control'][@data-field='server']"
        path_on_server = "//input[@class='combobox form-control'][@type='text']"
        local_mount_point = "//input[@class='form-control'][@data-field='dir']"
        add_mount_point = "//button[@class='btn btn-primary apply'][@data-action='apply']"
        cmd = 'mkdir %s' % self.local_path
        self.host.execute(cmd)
        self.hover_and_click(self.BUTTON_NFS_MOUNT)
        self.input_text(nfs_server_address,self.nfs_address)
        self.input_text(path_on_server,self.server_path)
        self.input_text(local_mount_point,self.local_path)
        self.click(add_mount_point)
        sleep(3)

       # firewall_status_button = "//label[contains(@class,'btn active')]"
        #return self.get_text(firewall_status_button)
    def umount_nfs_mount(self):
       # nfs_mount_click = "tbody:nth-child(3) tr:nth-child(1) td:nth-child(1)"
        #nfs_mount_click = "//td[contains(text(), 'testmount')]"
        nfs_umount_button = "//button[text()='Unmount']"
        self.click(self.nfs_mount_click % self.server_path)
        self.click(nfs_umount_button)
    def remount_nfs_mount(self):
        self.click(self.nfs_mount_click % self.server_path)
        nfs_remount_button = "//button[text()='Mount']"
        self.click(nfs_remount_button)
    def edit_nfs_mount(self):
        nfs_edit_button = "//button[text()='Edit']"
        local_mount_point = "//input[@class='form-control'][@data-field='dir']"
        nfs_ro_mount = "//input[@type='checkbox'][@data-field='mount_ro']"
       # nfs_editmount_click = "//td[contains(text(), '%s')]" % self.edit_path
        cmd = 'mkdir %s' % self.edit_path
        self.host.execute(cmd)
        add_mount_point = "//button[@class='btn btn-primary apply'][@data-action='apply']"
        self.click(self.nfs_mount_click % self.server_path)
        self.click(nfs_edit_button)
        self.click(nfs_ro_mount)
        self.input_text(local_mount_point,self.edit_path)
        self.click(add_mount_point)
        sleep(2)
        #self.assert_element_visible(nfs_editmount_click)

    def delete_nfs_mount(self):
        self.click(self.nfs_mount_click % self.server_path)
        delete_mount_button = "//button[text()='Remove']"
        self.hover_and_click(delete_mount_button)
    def open_page(self):
        self.click(self.STORAGE_LINK)
        self.switch_to_frame(self.STORAGE_FRAME_NAME)

