from datafix.core import Action

class SelectNode(Action):
    # def __init__(self, node):
    #     self.node = node
    required_type = 'mesh name'

    def action(self):
        # self.parent contains a datanode. that has either meshname or mesh
        import pymel.core as pm