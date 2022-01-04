class ComponentList():
    def __init__(self, owner):
        self.owner = owner
        self._all = []
        self._by_name = {}

    def __getitem__(self, index):
        return self._all[index]

    def create_component(self, name, *args, first=False, **kwargs):
        comp = self.owner.manager.ComponentRegistry[name]()
        comp.manager = self.owner.manager
        comp.init(*args, **kwargs)
        comp.update()
        self._add_component(comp, first)
        return comp

    def get_components(self, name):
        return self._by_name.get(name)

    
    def _add_component(self, comp, first):
        if first:
            self._all.insert(0, comp)
        else:
            self._all.append(comp)
        name = type(comp).__name__
        by_name = self.get_components(name)
        if by_name == None:
            by_name = []
            self._by_name[name] = by_name
        by_name.append(comp)