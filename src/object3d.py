from graphics import Graphics

class Object3D:
    def __init__(self, gfx, name, model_file, texture_file):
        self.id = gfx.get_object_id()
        self.name = name
        self.model = gfx.load_model_from_file(model_file)
        gfx.load_texture_from_file(self.id, texture_file)
        self.start_vertex, self.end_vertex = gfx.insert_model_vertices(self.model)
        print("{}: start vertex: {} end vertex: {}".format(self.name, self.start_vertex, self.end_vertex))
