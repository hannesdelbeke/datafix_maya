from datafix.core.collector import Collector
from datafix_maya.nodes.actions.select_node import SelectNodeByName
from datafix_maya.types import Material
from maya import cmds


class MaterialsCollector(Collector):
    child_actions = [SelectNodeByName]
    # exclude_default_nodes = True

    def collect(self):
        names = cmds.ls(mat=True)

        # if self.exclude_default_nodes:
        #     default_nodes = cmds.ls(defaultNodes=True)
        #     names = [n for n in names if n not in default_nodes]

        return [Material(n) for n in names]


class AppliedMaterialsCollector(Collector):
    child_actions = [SelectNodeByName]

    def collect(self):
        used_material_names = set()
        shape_nodes = cmds.ls(type='shape', long=True)
        for shape in shape_nodes:
            # Get shading engines connected to the shape
            shading_engines = cmds.listConnections(shape, type='shadingEngine') or []
            for se in shading_engines:
                # Get materials connected to the shading engine
                materials = cmds.ls(cmds.listConnections(se), materials=True) or []
                used_material_names.update(materials)
        return [Material(n) for n in used_material_names]
