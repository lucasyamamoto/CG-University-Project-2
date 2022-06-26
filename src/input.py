import glm
import math
import glfw

class Input:
    def __init__(self, camera, width, height):
        self.firstMouse = True
        self.yaw = -90.0 
        self.pitch = 0.0
        self.lastX =  width/2
        self.lastY =  height/2
        self.camera = camera

    def mouse_event(self, window, xpos, ypos):
        if self.firstMouse:
            self.lastX = xpos
            self.lastY = ypos
            self.firstMouse = False

        xoffset = xpos - self.lastX
        yoffset = self.lastY - ypos
        self.lastX = xpos
        self.lastY = ypos

        sensitivity = 0.3 
        xoffset *= sensitivity
        yoffset *= sensitivity

        self.yaw += xoffset;
        self.pitch += yoffset;

        
        if self.pitch >= 90.0: self.pitch = 90.0
        if self.pitch <= -90.0: self.pitch = -90.0

        front = glm.vec3()
        front.x = math.cos(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))
        front.y = math.sin(glm.radians(self.pitch))
        front.z = math.sin(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))
        self.camera.front = glm.normalize(front)

        # print("Mouse pos", xpos, ypos)

    def key_event(self, window, key, scancode, action, mods):
        # Set exit key
        if key == glfw.KEY_ESCAPE and (action==glfw.PRESS or action==glfw.REPEAT):
            glfw.set_window_should_close(window, True)

        cameraSpeed = 1.0
        if key == glfw.KEY_W and (action==glfw.PRESS or action==glfw.REPEAT): # tecla W
            self.camera.pos += cameraSpeed * self.camera.front
        
        if key == glfw.KEY_S and (action==glfw.PRESS or action==glfw.REPEAT): # tecla S
            self.camera.pos -= cameraSpeed * self.camera.front
        
        if key == glfw.KEY_A and (action==glfw.PRESS or action==glfw.REPEAT): # tecla A
            self.camera.pos -= glm.normalize(glm.cross(self.camera.front, self.camera.up)) * cameraSpeed
            
        if key == glfw.KEY_D and (action==glfw.PRESS or action==glfw.REPEAT): # tecla D
            self.camera.pos += glm.normalize(glm.cross(self.camera.front, self.camera.up)) * cameraSpeed

        if key == glfw.KEY_Q and (action==glfw.PRESS or action==glfw.REPEAT): # tecla Q
            self.camera.fov += 1

        if key == glfw.KEY_E and (action==glfw.PRESS or action==glfw.REPEAT): # tecla E
            self.camera.fov -= 1


        # print("Camera pos", self.camera.pos)
            
        # if key == 80 and action==1 and polygonal_mode==True:
        #     polygonal_mode=False
        # else:
        #     if key == 80 and action==1 and polygonal_mode==False:
        #         polygonal_mode=True

        # Minimum height
        if self.camera.pos.y < 1.0:
            self.camera.pos.y = 1.0
        # Maximum height
        elif self.camera.pos.y > 50.0:
            self.camera.pos.y = 50.0

        # Define x and z limits
        if self.camera.pos.x < -150.0:
            self.camera.pos.x = -150.0
        elif self.camera.pos.x > 150.0:
            self.camera.pos.x = 150.0
        if self.camera.pos.z < -150.0:
            self.camera.pos.z = -150.0
        elif self.camera.pos.z > 150.0:
            self.camera.pos.z = 150.0
