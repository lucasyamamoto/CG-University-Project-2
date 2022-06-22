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

        self.cat = Object3D(self.graphics, 
                "Cat", "assets/cat/cat.obj", "assets/cat/Cat_diffuse.jpg", 
                Transform(
                    angle=270, 
                    translation=vec3(-6, 0, 5), 
                    rotation=vec3(1, 0, 0), 
                    scale=vec3(0.1, 0.1, 0.1)
                    ))

        self.person = Object3D(self.graphics, 
                "Person", "assets/person/person.obj", "assets/person/person.jpg", 
                Transform(
                    translation=vec3(-10, 0, 0), 
                    scale=vec3(0.01, 0.01, 0.01)
                    ))

        self.moon = Object3D(self.graphics, 
                "Moon", "assets/moon/moon.obj", "assets/moon/moon.png",
                Transform(
                    translation=vec3(0, 90, -100), 
                    scale=vec3(2, 2, 2)
                    ))

        self.floor = Object3D(self.graphics, 
                "Floor", "assets/flat/flat.obj", "assets/flat/flat.jpg", 
                Transform(
                    translation=vec3(0, 0, 0), 
                    scale=vec3(100, 100, 100)
                    ))

        self.sky = Object3D(self.graphics, 
                "Sky", "assets/flat/flat.obj", "assets/flat/flat.jpg", 
                Transform(
                    translation=vec3(0, 100, 0), 
                    scale=vec3(100, 100, 100)
                    ))

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.frame += 1
            self.window.poll_events()
            self.graphics.clear_screen()

            # Objects
            self.graphics.draw_object(self.cat, self.cat.transform)
            self.graphics.draw_object(self.person, self.person.transform)
            self.graphics.draw_object(self.moon, self.moon.transform)
            self.graphics.draw_object(self.floor, self.floor.transform)
            self.graphics.draw_object(self.sky, self.sky.transform)

            self.graphics.update_camera()
            self.graphics.upload_data()
            self.window.swap_buffers()
        self.window.terminate()
