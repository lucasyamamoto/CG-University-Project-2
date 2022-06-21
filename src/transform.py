from glm import vec3

class Transform:
    def __init__(self, angle=0, translation=vec3(0.0, -1.0, 0.0), rotation=vec3(0.0, 0.0, 1.0), scale=vec3(1.0, 1.0, 1.0)):
        self.a = angle
        self.t = translation
        self.r = rotation
        self.s = scale
