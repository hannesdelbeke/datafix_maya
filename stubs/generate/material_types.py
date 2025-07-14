import maya.cmds as cmds


def get_all_assignable_material_types():
    """
    detect all material types, without needing instances of them in your Maya scene.
    """
    # cmds.ls(mat=True) returns Material nodes
    # but a material node doesn't exist. instead it returns different node types.
    # this is an issue for datafix since validators and collectors rely on node types.
    # This method is used to find all assignable material types in Maya.

    all_node_types = cmds.ls(nt=True)
    assignable_material_types = []

    # Shader types that are assignable typically inherit from both 'shadingDependNode' and 'surfaceShader'
    for t in all_node_types:
        derived = cmds.nodeType(t, derived=True, isTypeName=True)
        inherited = cmds.nodeType(t, inherited=True, isTypeName=True)

        # Criteria: must inherit from shadingDependNode AND surfaceShader (or similar assignable shader type)
        if 'shadingDependNode' in inherited:
            # Test if node can be created and connected to a shading group
            try:
                tmp = cmds.shadingNode(t, asShader=True)
                sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
                cmds.connectAttr(f"{tmp}.outColor", f"{sg}.surfaceShader", force=True)
                cmds.delete(tmp, sg)
                assignable_material_types.append(t)
            except Exception as e:
                print(e)  # Node type exists but isn't instantiable as a shader or isn't assignable

    return sorted(set(assignable_material_types))


def print_material_types():
    """Prints all assignable material types in Maya."""
    material_types = get_all_assignable_material_types()
    print("All assignable material types in Maya:")
    for mat in material_types:
        print(f"{mat}")

