#!/usr/bin/env python
# VMware vSphere Python SDK

"""
Python program for listing the vms on an ESX / vCenter host
"""

from __future__ import print_function

import argparse
import atexit
import getpass
import ssl
import sys
import utilities
import connecter
import time

import vm_ops

def GetArgs():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(
            description='Process args for retrieving all the Virtual Machines')
    parser.add_argument('-s', '--host', required=False, action='store',
                        help='Remote host to connect to')
    parser.add_argument('-o', '--port', type=int, default=443, action='store',
                        help='Port to connect on')
    parser.add_argument('-u', '--user', required=False, action='store',
                        help='User name to use when connecting to host')
    parser.add_argument('-p', '--password', required=False, action='store',
                        help='Password to use when connecting to host')
    args = parser.parse_args()
    return args

def main():
    """
    Simple command-line program for listing the virtual machines on a system.
    """
    args = GetArgs()

    config = connecter.readConfig("config.json")
    details = connecter.ConnectDetails(host=config["host"], port=config["port"], user=config["user"], password=config["password"])
    si = connecter.DConnecter(details).connect()

    content = si.RetrieveContent()
    vcenter = vm_ops.VCenter(content)
    obj_folders = vcenter.getFoldersFromNames(['europa tests', 'eris tests', 'mercury tests', 'fistiq tests', 'saturn tests', 'alice tests'])
    print("OBJ FOLDERS : ", obj_folders)
    obj_vms = vcenter.getVMsFromFolders(obj_folders)
    print("OBJ VMS : ", obj_vms)
    for vm in obj_vms:
        print('Found VM :', vm.name)

    # container = content.rootFolder  # starting point to look into
    # print("Root Folder : ", container)
    # viewType = [vim.Folder]  # object types to look for
    # recursive = True  # whether we should look into it recursively
    # containerView = content.viewManager.CreateContainerView(
    #         container, viewType, recursive)
    #
    # print("VM details...")
    # children = containerView.view
    # for child in children:
    #     # print("Now :", time.time())
    #     # print("VM Name : ", child.name)
    #     # print("Uptime : ", child.summary.quickStats.uptimeSeconds)
    #     # print(child.availableField)
    #     # print("="*75)
    #     # print(child.customValue)
    #
    #     # print(dir(child))
    #     print(child, child.name)
    #
    #     # utilities.print_vm_info(child)
    #     # sys.exit(1)


    return 0


# Start program
if __name__ == "__main__":
    main()
