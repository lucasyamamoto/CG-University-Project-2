from window import Window
from input import Input
from camera import Camera
from graphics import Graphics
from object3d import Object3D
from transform import Transform
from glm import vec3

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
        self.frame = 0

        self.window.set_mouse_callback(self.input.mouse_event)
        self.window.set_key_callback(self.input.key_event)
        self.window.set_cursor_pos(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        #self.house = Object3D(self.graphics, "Casa", "assets/casa.obj", "assets/casa.jpg")
        self.cat = Object3D(self.graphics, "Cat", "assets/cat/cat.obj", "assets/cat/Cat_bump.jpg")
        #self.house = Object3D(self.graphics, "Casa", "assets/casa2.obj", "assets/casa2.png")

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.frame += 1
            self.window.poll_events()

            self.graphics.clear_screen()

            #self.graphics.draw_object(self.house.id, self.house.start_vertex, self.house.end_vertex)
            self.graphics.draw_object(self.cat.id, self.cat.start_vertex, self.cat.end_vertex, Transform(angle=self.frame*5))
            #self.graphics.draw_object(self.house.id, self.house.start_vertex, self.house.end_vertex, self.house.transform)


            self.graphics.update_camera()
            self.graphics.upload_data()

            self.window.swap_buffers()
        self.window.terminate()
