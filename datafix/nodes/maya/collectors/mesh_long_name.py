from datafix.core.collector import Collector
from datafix.nodes.maya.actions.select_node import SelectNodeByName

from maya import cmds


class MeshLongNameCollector(Collector):
    child_actions = [SelectNodeByName]

    def collect(self):
        return cmds.ls(type='mesh', long=True)

