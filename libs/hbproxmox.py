import re
from proxmoxer import ProxmoxAPI

class TraiOiProxmox:
  def __init__(self, p_node, p_user, p_pass):
    self.proxmox = ProxmoxAPI(
        p_node,
        user=p_user,
        password=p_pass,
        port="443",
        verify_ssl=False)

  def stop_vm(self, vm_name):
    self.vms_list = []
    for node in self.proxmox.nodes.get():
      node_info = self.proxmox.nodes(node["node"])
      for vm in node_info.qemu.get():
        if(vm["name"] == vm_name):
          print(node_info.qemu(vm["vmid"]).status.stop.post())

  def start_vm(self, vm_name):
    self.vms_list = []
    for node in self.proxmox.nodes.get():
      node_info = self.proxmox.nodes(node["node"])
      for vm in node_info.qemu.get():
        if(vm["name"] == vm_name):
          print(node_info.qemu(vm["vmid"]).status.start.post())
