"""
    Resources Module

    Module related to I/O devices, especifically 1 scanner, 2 printers, 
    1 modem and 2 SATA disks. Only user processes can have access to these 
    services. Mutual exclusion between the processes is implemented.
"""

class ResourceManager:

    def __init__(self):
        # A resource with value of 0 means it's free, otherwise it's being used
        self.resources = {'scanner': 0, 'printers': [0, 0], 'modem': 0, 'disks': [0, 0]}

    def resources_availability(self, process):
        """
            Verifies if the process has permission to allocate the resources (if it's 
            a real-time or not) and if the resources are available or not, raising 
            an exception if it fails.
            throws:
                Exception with an error message
        """
        # Check if it is a real-time process trying to allocate a resource
        if process.priority == 0 and (process.scanner or process.modem \
                        or process.printer_cod or process.disk_cod):
            raise Exception('Processos de tempo real não podem alocar recursos.')

        # Since it's not a real-time process, let's verify the resources availability
        proc_printer_idx = process.printer_cod -1
        proc_disk_idx = process.disk_cod -1
        err_msgs = []
        if process.scanner and self.resources['scanner']:
            err_msgs.append('Scanner ocupado, não foi possível alocar este recurso.')
        if process.modem and self.resources['modem']:
            err_msgs.append('Modem ocupado, não foi possível alocar este recurso.')
        if process.printer_cod and self.resources['printers'][proc_printer_idx]:
            err_msgs.append(f'Impressora {process["printer_cod"]} ocupada, não foi possível alocar este recurso.')
        if process.disk_cod and self.resources['disks'][proc_disk_idx]:
            err_msgs.append(f'Disco {process["disk_cod"]} ocupado, não foi possível alocar este recurso.')

        if len(err_msgs) > 0:
            err_msgs = '\n'.join(err_msgs)
            raise Exception(err_msgs)

    def allocate(self, process):
        """
            Allocates all the resources the process is requesting. It's assumed
            that the resources_availability() was already called.
            Args:
                process ('obj') a Process.
        """
        try:
            resources_availability(process)

        proc_printer_idx = process.printer_cod -1
        proc_disk_idx = process.disk_cod -1
        self.resources['scanner'] = process.scanner
        self.resources['modem'] = process.modem
        if process.printer_cod > 0:
            self.resources['printers'][proc_printer_idx] = 1
        if process.disk_cod > 0:
            self.resources['disks'][proc_disk_idx] = 1

    def free(self, process):
        """
            Deallocates every resource used by the process.
        """
        if process.scanner:
            self.resources['scanner'] = 0
        if process.modem:
            self.resources['modem'] = 0
        if process.printer_cod > 0:
            self.resources['printers'][process.printer_cod -1] = 0
        if process.disk_cod > 0:
            self.resources['disks'][process.disk_cod -1] = 0

