from datafix.core import Action
import maya.cmds as cmds


class SelectNodeByName(Action):
    name = "Select Node"
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.name = "Select Node"

    def action(self):
        cmds.select(self.parent.data)