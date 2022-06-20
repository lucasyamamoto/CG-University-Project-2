from window import Window
from input import Input
from camera import Camera
from graphics import Graphics
from object3d import Object3D

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WINDOW_NAME = "Application"

class Application:
    def __init__(self):
        """Initialize application"""
        self.window = Window(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.camera = Camera(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.input = Input(self.camera, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.graphics = Graphics(self.camera)

        self.window.set_mouse_callback(self.input.mouse_event)
        self.window.set_key_callback(self.input.key_event)
        self.window.set_cursor_pos(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        self.house = Object3D(self.graphics, "Casa", "assets/casa.obj", "assets/casa.jpg")
        # Initialize application here

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.window.poll_events()

            self.graphics.clear_screen()
            self.graphics.draw_object(self.house.id, self.house.start_vertex, self.house.end_vertex)
            self.graphics.update_camera()

            self.window.swap_buffers()
        self.window.terminate()
