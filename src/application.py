from window import Window
from graphics import Graphics
from object3d import Object3D

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WINDOW_NAME = "Application"

class Application:
    def __init__(self):
        """Initialize application"""
        self.window = Window(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.graphics = Graphics()
        self.cube = Object3D(self.graphics, "Caixa Teste", "assets/caixa.obj", "assets/caixa.jpg")

        # Initialize application here

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.graphics.clear_screen()
            self.graphics.draw_object(self.cube.id, self.cube.start_vertex, self.cube.end_vertex)
            self.graphics.set_camera()
            self.window.swap_buffers()
        self.window.terminate()
