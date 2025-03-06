from datafix.core.collector import Collector
from maya import cmds


class MeshLongNameCollector(Collector):
    def collect(self):
        return cmds.ls(type='mesh', long=True)

