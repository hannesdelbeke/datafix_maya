from datafix.core.collector import Collector
from datafix_maya.nodes.actions.select_node import SelectNodeByName
from datafix_maya import types
from datafix_maya.types.standard import _MayaNode
import maya.cmds as cmds
import inspect
from typing import List


class _NodeCollector(Collector):
    child_actions = [SelectNodeByName]

    def run(self):
        super().run()
        # set node.name to short name, nicer for UI
        for node in self.children:
            node.name = node.data.split('|')[-1]

# Extract all NewType aliases from types
for var_name, var_value in inspect.getmembers(types):
    if var_name.startswith("_"):
        continue
    if not isinstance(var_value, type):
        continue
    if not issubclass(var_value, _MayaNode):
        continue

    NodeClass: "_MayaNode" = var_value
    maya_type = NodeClass.maya_type

    # Create a function to collect nodes of this type
    def collect_func(self, _maya_type=maya_type, _NodeClass=NodeClass):
        names = cmds.ls(type=_maya_type, long=True) or []
        return [_NodeClass(n) for n in names]

    # Create a new collector class dynamically
    collector_class = type(
        f"{var_name}Collector",
        (_NodeCollector,),
        {
            "collect": collect_func,
            "__annotations__": {"collect": List[NodeClass]}
        }
    )

    # Register the collector class in the global namespace
    globals()[f"{var_name}Collector"] = collector_class


# class MeshCollector(_NodeCollector):
#     def collect(self) -> List[types.mesh]:
#         names = cmds.ls(type='mesh', long=True)
#         return [types.mesh(x) for x in names]
#
#
# class MaterialCollector(_NodeCollector):
#     def collect(self):
#         names = cmds.ls(type='shadingEngine', long=True)
#         return [types.shadingEngine(x) for x in names]

