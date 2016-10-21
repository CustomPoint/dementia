from pyVmomi import vim


class VCenter:
    def __init__(self, content):
        # name - obj value
        self._content = content
        self.allFolders = {}

    def _getAllFolders(self):
        if self.allFolders:
            return self.allFolders
        container = self._content.rootFolder  # starting point to look into
        viewType = [vim.Folder]  # object types to look for
        recursive = True  # whether we should look into it recursively
        containerView = self._content.viewManager.CreateContainerView(
                container, viewType, recursive)
        children = containerView.view
        for child in children:
            self.allFolders[str(child.name).lower()] = child

    def getVMsFromFolders(self, folders):
        """
            Function that takes the given folders and retrieves all VMs
            :return list of VM targeted devices. OBJs returned values.
        """
        returnedVMs = []
        for folder in folders:
            print("Root Folder : ", folder, "[{0}]".format(folder.name))
            viewType = [vim.VirtualMachine]  # object types to look for
            recursive = True  # whether we should look into it recursively
            containerView = self._content.viewManager.CreateContainerView(folder, viewType, recursive)
            children = containerView.view
            for child in children:
                returnedVMs.append(child)
        return returnedVMs

    def getFoldersFromNames(self, names):
        """
            Function that takes the given folders and retrieves all VMs
            :return list of Folders. OBJs returned values.
        """
        returnedFolders = []
        self._getAllFolders()
        for name in names:
            if name in self.allFolders:
                returnedFolders.append(self.allFolders[str(name).lower()])
            else:
                print("Name was not found as folder: ", name)
        return returnedFolders




