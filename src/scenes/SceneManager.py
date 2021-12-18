class SceneManager(object):
    def __init__(self):
        self.scenes = {}

    def add_scene(self, scene):
        self.scenes[scene.name] = scene
        scene.manager = self

    def to_scene(self, scene_name, *args, **kwargs):
        scene = self.scenes[scene_name]
        scene.init_scene(*args, **kwargs)
        self.scene = scene
