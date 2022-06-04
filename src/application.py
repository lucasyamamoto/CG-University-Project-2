from window import Window

class Application:
    def __init__(self):
        """Initialize application"""
        self.window = Window()
        # Initialize application here

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.window.swap_buffers()