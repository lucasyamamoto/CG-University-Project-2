from window import Window
from input import Input
from camera import Camera
from graphics import Graphics
from object3d import Object3D
from transform import Transform
from glm import vec3
import glm

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_NAME = "Application"

class Application:
    def __init__(self):
        """Initialize application"""
        self.window = Window(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.camera = Camera(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.input = Input(self.camera, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.graphics = Graphics(self.camera)
        self.frame = 0

        # Configure input
        self.window.set_mouse_callback(self.input.mouse_event)
        self.window.set_key_callback(self.input.key_event)
        self.window.set_cursor_pos(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        # Instanciate 3D models
        self.cat = Object3D(self.graphics, 
                "Cat", "assets/cat/cat.obj", "assets/cat/Cat_diffuse.jpg", 
                Transform(
                    angle=270, 
                    translation=vec3(-6, 0, 5), 
                    rotation=vec3(1, 0, 0), 
                    scale=vec3(0.15, 0.15, 0.15)
                    ))

        self.person = Object3D(self.graphics, 
                "Person", "assets/person/person.obj", "assets/person/person.jpg", 
                Transform(
                    translation=vec3(-10, 0, 0), 
                    scale=vec3(0.015, 0.015, 0.015)
                    ))

        self.moon = Object3D(self.graphics, 
                "Moon", "assets/moon/moon.obj", "assets/moon/moon.png",
                Transform(
                    translation=vec3(0, 90, -100), 
                    scale=vec3(2, 2, 2)
                    ))

        self.moonanimation = glm.rotate(glm.mat4(1.0), 0.1, vec3(0.0, 1.0, 0.0))

        self.floor = Object3D(self.graphics, 
                "Floor", "assets/flat/flat.obj", "assets/flat/flat.jpg", 
                Transform(
                    translation=vec3(0, 0, 0), 
                    scale=vec3(2, 2, 2)
                    ))

        self.grass = Object3D(self.graphics, 
                "Floor", "assets/flat/grass.obj", "assets/flat/grass.jpg", 
                Transform(
                    translation=vec3(0, 0, 0), 
                    scale=vec3(2, 2, 2)
                    ))

        self.sky = Object3D(self.graphics, 
                "Sky", "assets/sky/nightsky.obj", "assets/sky/nightsky.jpg", 
                )

        self.house = Object3D(self.graphics, 
                "House", "assets/house/house.obj", "assets/house/house.jpg", 
                Transform(
                    translation=vec3(0, 0, 0), 
                    scale=vec3(3, 3, 3)
                    ))

        self.car = Object3D(self.graphics, 
                "Car", "assets/car/car.obj", "assets/car/car.png", 
                Transform(
                    translation=vec3(0, 0, -100), 
                    scale=vec3(10, 10, 10),
                    rotation=vec3(0, 1, 0),
                    angle=0
                    ))

        self.caranimation = glm.rotate(glm.mat4(1.0), 0.3, vec3(0.0, 1.0, 0.0))

    def run(self):
        """Run main loop"""
        while not self.window.should_close():
            # Main loop
            self.frame += 1
            self.window.poll_events()
            self.graphics.clear_screen()

            # Update animations
            self.moon.transform.t = vec3(self.moonanimation * glm.vec4(self.moon.transform.t, 1.0))
            self.car.transform.t = vec3(self.caranimation * glm.vec4(self.car.transform.t, 1.0))
            self.car.transform.a = glm.degrees(glm.atan(self.car.transform.t.x/self.car.transform.t.z))
            if self.car.transform.t.z > 0.0:
                self.car.transform.a += 180.0

            # Draw objects
            self.graphics.draw_object(self.cat, self.cat.transform)
            self.graphics.draw_object(self.person, self.person.transform)
            self.graphics.draw_object(self.moon, self.moon.transform, True)
            self.graphics.draw_object(self.floor, self.floor.transform)
            self.graphics.draw_object(self.grass, self.grass.transform)
            self.graphics.draw_object(self.sky, self.sky.transform)
            self.graphics.draw_object(self.house, self.house.transform)
            self.graphics.draw_object(self.car, self.car.transform)

            # Update screen
            self.graphics.update_camera()
            self.graphics.upload_data()
            self.window.swap_buffers()
        self.window.terminate()
