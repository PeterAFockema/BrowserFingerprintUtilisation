import os

class Display():

    'Class relating to display ports'

    #Variable we will use for declaring our display process
    display_process = None

    def __init__(self) -> None:
        pass

    def setDisplayPortAsEnvironmentVariable(self):
        # Set the display port as an environment variable
        display_port = os.environ.get("DISPLAY_PORT", "99")
        self.display_process = f":{display_port}"
        os.environ["DISPLAY"] = self.display_process
        # return self.display_process