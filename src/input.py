import glm
import math

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
        cameraSpeed = 0.2
        if key == 87 and (action==1 or action==2): # tecla W
            self.camera.pos += cameraSpeed * self.camera.front
        
        if key == 83 and (action==1 or action==2): # tecla S
            self.camera.pos -= cameraSpeed * self.camera.front
        
        if key == 65 and (action==1 or action==2): # tecla A
            self.camera.pos -= glm.normalize(glm.cross(self.camera.front, self.camera.up)) * cameraSpeed
            
        if key == 68 and (action==1 or action==2): # tecla D
            self.camera.pos += glm.normalize(glm.cross(self.camera.front, self.camera.up)) * cameraSpeed

        # print("Camera pos", self.camera.pos)
            
        # if key == 80 and action==1 and polygonal_mode==True:
        #     polygonal_mode=False
        # else:
        #     if key == 80 and action==1 and polygonal_mode==False:
        #         polygonal_mode=True
            
