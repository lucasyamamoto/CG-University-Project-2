import glfw

class Window:
    def __init__(self, name, width, height):
        """Init GLFW window and show"""
        glfw.init()
        glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
        self._window = glfw.create_window(width, height, name, None, None)
        glfw.make_context_current(self._window)
        glfw.show_window(self._window)
    
    def set_key_callback(self, callback):
        """Set key input callback"""
        glfw.set_key_callback(self._window, callback)
    
    def set_mouse_callback(self, callback):
        """Set mouse input callback"""
        glfw.set_cursor_pos_callback(self._window, callback)

    def set_cursor_pos(self, x, y):
        """Set cursor position"""
        glfw.set_cursor_pos(self._window, x, y)

    def poll_events(self):
        """Poll events"""
        glfw.poll_events()
    
    def get(self):
        """Get GLFW window"""
        return self._window

    def should_close(self):
        """Get exit message"""
        return glfw.window_should_close(self._window)

    def swap_buffers(self):
        """Swap window buffers"""
        glfw.swap_buffers(self._window)

    def terminate(self):
        """Clean-up window before exiting"""
        glfw.terminate()
