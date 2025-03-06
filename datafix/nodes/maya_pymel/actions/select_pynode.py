from datafix.core import Action
import pymel.core as pm


class SelectNode(Action):
    required_type = pymel.core.general.PyNode

    def action(self):
        pm.select(self.parent.data)