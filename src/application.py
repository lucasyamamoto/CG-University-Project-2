from window import Window

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WINDOW_NAME = "Application"

class Application:
    def __init__(self):
        """Initialize application"""
        self.window = Window(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)
        # Initialize application here

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.window.swap_buffers()