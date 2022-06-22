import math
import glm
import numpy as np

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pos   = glm.vec3(-5,  10.0,  30.0);
        self.front = glm.vec3(0.0,  0.0,  -1.0);
        self.up    = glm.vec3(0.0,  1.0,  0.0);

    def model(self, angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z):
        angle = math.radians(angle)
        
        matrix_transform = glm.mat4(1.0) # instanciando uma matriz identidade
        
        # aplicando translacao
        matrix_transform = glm.translate(matrix_transform, glm.vec3(t_x, t_y, t_z))    
        
        # aplicando rotacao
        matrix_transform = glm.rotate(matrix_transform, angle, glm.vec3(r_x, r_y, r_z))
        
        # aplicando escala
        matrix_transform = glm.scale(matrix_transform, glm.vec3(s_x, s_y, s_z))
        
        matrix_transform = np.array(matrix_transform)
        
        return matrix_transform

    def view(self):
        mat_view = glm.lookAt(self.pos, self.pos + self.front, self.up);
        mat_view = np.array(mat_view)
        return mat_view

    def projection(self):
        # perspective parameters: fovy, aspect, near, far

        # lembrar de mudar
        mat_projection = glm.perspective(glm.radians(45.0), self.width/self.height, 0.1, 1000.0)

        mat_projection = np.array(mat_projection)    
        return mat_projection
