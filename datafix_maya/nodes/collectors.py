from datafix.core.collector import Collector
from datafix_maya.nodes.actions.select_node import SelectNodeByName
from datafix_maya import types
from maya import cmds
import inspect
from typing import List


class _NodeCollector(Collector):
    child_actions = [SelectNodeByName]

    def run(self):
        super().run()
        # set node.name to short name, nicer for UI
        for node in self.children:
            node.name = node.data.split('|')[-1]

def is_newtype(obj):
    return hasattr(obj, '__supertype__') and isinstance(obj.__supertype__, type)

# Extract all NewType aliases from types
for name, type_alias in inspect.getmembers(types):
    if is_newtype(type_alias):
        maya_type = name  # assuming the alias name matches Maya node type string

        # Create a function to collect nodes of this type
        def collect_func(self, _maya_type=maya_type, _type_alias=type_alias):
            names = cmds.ls(type=_maya_type, long=True) or []
            return [_type_alias(n) for n in names]

        # Create a new collector class dynamically
        collector_class = type(
            f"{name}Collector",
            (_NodeCollector,),
            {
                "collect": collect_func,
                "__annotations__": {"collect": List[type_alias]}
            }
        )

        # Register the collector class in the global namespace
        globals()[f"{name}Collector"] = collector_class


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

