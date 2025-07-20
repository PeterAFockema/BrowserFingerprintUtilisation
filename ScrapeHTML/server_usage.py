import subprocess

class ServerUsage():
    '''A class for the declaration of a server, it's use cases, and closing it down'''

    #Variable we will use for declaring our server process
    process = None

    def __init__(self) -> None:
        pass

    def startTheXvfbServerProcess(self, display):
        # Start the Xvfb server
        return subprocess.Popen(["Xvfb", f"{display}", "-screen", "0", "1024x768x24", "-nolisten", "tcp"])
    
    def startTheXvfbServerProcessUsingDifferentFromDefaultDisplayValues(self, display):
        # Start the Xvfb server
        return subprocess.Popen(["Xvfb", f"{display}", "-screen", "0", "512x768x24", "-nolisten", "tcp"])
    
    def start_the_Xvfb_server_process_using_different_from_default_display_values(self, display):
        # Start the Xvfb server
        return subprocess.Popen(["Xvfb", f"{display}", "-screen", "0", "512x768x24", "-nolisten", "tcp"])
    
    def killTheXcfbServerProcess(self, processToKill):
        #Kill the server process
        processToKill.kill()