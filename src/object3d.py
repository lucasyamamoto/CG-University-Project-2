class Object3D:
    def __init__(self, graphics, name, model_file, texture_file):
        self.id = graphics.get_object_id()
        self.name = name
        self.model = graphics.load_model_from_file(model_file)
        graphics.load_texture_from_file(self.id, texture_file)
        self.start_vertex, self.end_vertex = graphics.insert_model_vertices(self.model)
        print("{}: start vertex: {} end vertex: {}".format(self.name, self.start_vertex, self.end_vertex))
