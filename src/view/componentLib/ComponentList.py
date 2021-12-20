class ComponentList():
    def __init__(self, owner):
        self.owner = owner
        self._all = []
        self._by_name = {}

    def __getitem__(self, index):
        return self._all[index]

    def create_component(self, name, *args, **kwargs):
        comp = self.owner.manager.ComponentRegistry[name]()
        comp.manager = self.owner.manager
        comp.init(*args, **kwargs)
        comp.update()
        self._add_component(comp)
        return comp

    def getComponents(self, name):
        return self._by_name.get(name)

    
    def _add_component(self, comp):
        self._all.append(comp)
        name = type(comp).__name__
        by_name = self.getComponents(name)
        if by_name == None:
            by_name = []
            self._by_name[name] = by_name
        by_name.append(comp)