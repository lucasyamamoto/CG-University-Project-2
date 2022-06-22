from window import Window
from input import Input
from camera import Camera
from graphics import Graphics
from object3d import Object3D
from transform import Transform
from glm import vec3
import math as m

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

        self.cat = Object3D(self.graphics, "Cat", "assets/cat/cat.obj", "assets/cat/Cat_diffuse.jpg")
        self.moon = Object3D(self.graphics, "Moon", "assets/moon/moon.obj", "assets/moon/moon.png")
        self.person = Object3D(self.graphics, "Person", "assets/person/person.obj", "assets/person/person.jpg")
        self.floor = Object3D(self.graphics, "Floor", "assets/flat/flat.obj", "assets/flat/flat.jpg")
        self.sky = Object3D(self.graphics, "Sky", "assets/flat/flat.obj", "assets/flat/flat.jpg")

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop here
            self.frame += 1
            self.window.poll_events()
            self.graphics.clear_screen()

            # Objects
            self.graphics.draw_object(self.cat.id, self.cat.start_vertex, self.cat.end_vertex, Transform(
                angle=270, 
                translation=vec3(-6, 0, 5), 
                rotation=vec3(1, 0, 0), 
                scale=vec3(0.1, 0.1, 0.1)
                ))

            self.graphics.draw_object(self.person.id, self.person.start_vertex, self.person.end_vertex, Transform(
                translation=vec3(-10, 0, 0), 
                scale=vec3(0.01, 0.01, 0.01)
                ))

            self.graphics.draw_object(self.moon.id, self.moon.start_vertex, self.moon.end_vertex, Transform(
                translation=vec3(0, 90, -100), 
                scale=vec3(2, 2, 2)
                ))

            self.graphics.draw_object(self.floor.id, self.floor.start_vertex, self.floor.end_vertex, Transform(
                translation=vec3(0, 0, 0), 
                scale=vec3(100, 100, 100)
                ))

            self.graphics.draw_object(self.sky.id, self.sky.start_vertex, self.sky.end_vertex, Transform(
                translation=vec3(0, 100, 0), 
                scale=vec3(100, 100, 100)
                ))

            self.graphics.update_camera()
            self.graphics.upload_data()
            self.window.swap_buffers()
        self.window.terminate()
