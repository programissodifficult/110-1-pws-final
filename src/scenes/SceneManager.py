class SceneManager(object):
    def __init__(self):
        self.scenes = {}

    def add_scene(self, scene):
        self.scenes[scene.name] = scene
        scene.manager = self
        if not hasattr(self, 'scene'):
            self.scene = scene

    def to_scene(self, scene_name):
        self.scene = self.scenes[scene_name]
