from datafix.core.collector import Collector
from datafix.nodes.maya.actions.select_node import SelectNodeByName

from maya import cmds


class _NodeCollector(Collector):
    child_actions = [SelectNodeByName]

    def run(self):
        super().run()
        # set node.name to short name, nicer for UI
        for node in self.children:
            node.name = node.data.split('|')[-1]


class MeshTransformCollector(_NodeCollector):
    def collect(self):
        # set() avoids duplicates of same transform, when a transform contains multiple meshes (shapes)
        return list(set(cmds.listRelatives(cmds.ls(type='mesh'), p=True)))


class MeshLongNameCollector(_NodeCollector):
    def collect(self):
        return cmds.ls(type='mesh', long=True)


class MaterialLongNameCollector(_NodeCollector):
    def collect(self):
        return cmds.ls(type='shadingEngine', long=True)


class TransformLongNameCollector(_NodeCollector):
    def collect(self):
        return cmds.ls(type='transform', long=True)


class CameraLongNameCollector(_NodeCollector):
    def collect(self):
        return cmds.ls(type='camera', long=True)


class LightLongNameCollector(_NodeCollector):
    def collect(self):
        return cmds.ls(type='light', long=True)


class JointLongNameCollector(_NodeCollector):
    def collect(self):
        return cmds.ls(type='joint', long=True)
