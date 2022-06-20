from OpenGL.GL import *
import numpy as np
from PIL import Image

TEXTURES_AMOUNT = 10
BUFFER_AMOUNT = 2

class Graphics:
    def __init__(self, camera):
        self.vertex_code = """
                attribute vec3 position;
                attribute vec2 texture_coord;
                varying vec2 out_texture;
                        
                uniform mat4 model;
                uniform mat4 view;
                uniform mat4 projection;        
                
                void main(){
                    gl_Position = projection * view * model * vec4(position,1.0);
                    out_texture = vec2(texture_coord);
                }
                """

        self.fragment_code = """
                uniform vec4 color;
                varying vec2 out_texture;
                uniform sampler2D samplerTexture;
                
                void main(){
                    vec4 texture = texture2D(samplerTexture, out_texture);
                    gl_FragColor = texture;
                }
                """

        self.vertices = []
        self.textures_coord = []
        self.objects_amount = -1
        self.camera = camera

        # Request a program and shader slots from GPU
        self.program  = glCreateProgram()
        self.vertex   = glCreateShader(GL_VERTEX_SHADER)
        self.fragment = glCreateShader(GL_FRAGMENT_SHADER)

        # Set shaders source
        glShaderSource(self.vertex, self.vertex_code)
        glShaderSource(self.fragment, self.fragment_code)

        # Compile shaders
        glCompileShader(self.vertex)
        if not glGetShaderiv(self.vertex, GL_COMPILE_STATUS):
            error = glGetShaderInfoLog(self.vertex).decode()
            print(error)
            raise RuntimeError("Erro de compilacao do Vertex Shader")

        glCompileShader(self.fragment)
        if not glGetShaderiv(self.fragment, GL_COMPILE_STATUS):
            error = glGetShaderInfoLog(self.fragment).decode()
            print(error)
            raise RuntimeError("Erro de compilacao do Fragment Shader")

        # Attach shader objects to the program
        glAttachShader(self.program, self.vertex)
        glAttachShader(self.program, self.fragment)

        # Build program
        glLinkProgram(self.program)
        if not glGetProgramiv(self.program, GL_LINK_STATUS):
            print(glGetProgramInfoLog(self.program))
            raise RuntimeError('Linking error')
    
        # Make program the default program
        glUseProgram(self.program)

        # Enable and generate texture
        glEnable(GL_TEXTURE_2D)
        self.textures = glGenTextures(TEXTURES_AMOUNT)

        glEnable(GL_DEPTH_TEST) ### importante para 3D

        # Request a buffer slot from GPU
        self.buffers = glGenBuffers(BUFFER_AMOUNT)

    def get_object_id(self):
        self.objects_amount += 1
        return self.objects_amount

    def load_model_from_file(self, filename):
        """Loads a Wavefront OBJ file. """
        vertices = []
        texture_coords = []
        faces = []

        material = None

        # Open the file for reading
        for line in open(filename, "r"): # For each line
            if line.startswith('#'): continue 
            values = line.split() # Split on spaces
            if not values: continue

            # Get vertices
            if values[0] == 'v':
                vertices.append(values[1:4])

            # Get texture coordinates
            elif values[0] == 'vt':
                texture_coords.append(values[1:3])

            # Get faces
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'f':
                face = []
                face_texture = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        face_texture.append(int(w[1]))
                    else:
                        face_texture.append(0)

                faces.append((face, face_texture, material))

        model = {}
        model['vertices'] = vertices
        model['texture'] = texture_coords
        model['faces'] = faces

        return model

    def load_texture_from_file(self, texture_id, img_textura):
        """Loads a texture from a image file. """
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        img = Image.open(img_textura)
        img_width = img.size[0]
        img_height = img.size[1]
        image_data = img.tobytes("raw", "RGB", 0, -1)
        #image_data = np.array(list(img.getdata()), np.uint8)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img_width, img_height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)


    def insert_model_vertices(self, model):
        """Inserts the model vertices into the vertices array"""
        start_vertex = len(self.vertices)
        for face in model['faces']:
            for vertice_id in face[0]:
                self.vertices.append(model['vertices'][vertice_id-1] )
            for texture_id in face[1]:
                self.textures_coord.append(model['texture'][texture_id-1] )
                
        end_vertex = len(self.vertices)
        return start_vertex, end_vertex


    def upload_data(self):
        """Uploads the vertices and textures into the GPU"""
        vertices = np.zeros(len(self.vertices), [("position", np.float32, 3)])
        vertices['position'] = self.vertices
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[0])
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        stride = vertices.strides[0]
        offset = ctypes.c_void_p(0)
        loc_vertices = glGetAttribLocation(self.program, "position")
        glEnableVertexAttribArray(loc_vertices)
        glVertexAttribPointer(loc_vertices, 3, GL_FLOAT, False, stride, offset)

        textures = np.zeros(len(self.textures_coord), [("position", np.float32, 2)])
        textures['position'] = self.textures_coord
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[1])
        glBufferData(GL_ARRAY_BUFFER, textures.nbytes, textures, GL_STATIC_DRAW)
        stride = textures.strides[0]
        offset = ctypes.c_void_p(0)
        loc_texture_coord = glGetAttribLocation(self.program, "texture_coord")
        glEnableVertexAttribArray(loc_texture_coord)
        glVertexAttribPointer(loc_texture_coord, 2, GL_FLOAT, False, stride, offset)


    def clear_screen(self):
        """Clears the screen"""
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)


    def draw_object(self, id, start_vertex, end_vertex):
        """Draws a object"""
        if self.camera is None: return

        # rotacao
        angle = 1.0;
        r_x = 0.0; r_y = 0.0; r_z = 1.0;
        
        # translacao
        t_x = 0.0; t_y = -1.0; t_z = 0.0;
        
        # escala
        s_x = 1.0; s_y = 1.0; s_z = 1.0;
        
        mat_model = self.camera.model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
        loc_model = glGetUniformLocation(self.program, "model")
        glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
        glBindTexture(GL_TEXTURE_2D, id)
        glDrawArrays(GL_TRIANGLES, start_vertex, end_vertex-start_vertex)


    def update_camera(self):
        """Updates the camera"""
        if self.camera is None: return

        mat_view = self.camera.view()
        loc_view = glGetUniformLocation(self.program, "view")
        glUniformMatrix4fv(loc_view, 1, GL_TRUE, mat_view)

        mat_projection = self.camera.projection()
        loc_projection = glGetUniformLocation(self.program, "projection")
        glUniformMatrix4fv(loc_projection, 1, GL_TRUE, mat_projection)    
