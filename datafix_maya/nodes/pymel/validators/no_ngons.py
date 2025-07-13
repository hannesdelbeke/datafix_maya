from datafix.core import Validator, NodeState, Action
import logging

import pymel.core as pm


# def find_ngons_slow(mesh_name):
#     # TODO, tested and works, but might be slow, no open maya.
#     """
#     Validates whether the given mesh has n-gons.
#     Raises an exception if n-gons are found.
#     """
#     if not cmds.objExists(mesh_name):
#         raise Exception(f"{mesh_name} does not exist in the scene.")
#
#     faces_with_ngons = []
#
#     # Get the number of faces in the mesh
#     num_faces = cmds.polyEvaluate(mesh_name, face=True)
#
#     # Iterate through all faces
#     for i in range(num_faces):
#         # Get the vertices of the face (ignoring UV or split normals issues)
#         face_vertices = cmds.polyListComponentConversion(f"{mesh_name}.f[{i}]", fromFace=True, toVertex=True)
#         vertex_count = len(cmds.ls(face_vertices, flatten=True))
#
#         # If a face has more than 4 vertices, it's an n-gon
#         if vertex_count > 4:
#             faces_with_ngons.append(f"{mesh_name}.f[{i}]")
#
#     if faces_with_ngons:
#         raise Exception(f"{mesh_name} has n-gons: {len(faces_with_ngons)} found ({', '.join(faces_with_ngons[:5])}...)")
#
#     return True


def get_ngon_ids(mesh_name):
    """
    Validates whether the given mesh has n-gons.
    Raises an exception if n-gons are found.
    """
    if not pm.objExists(mesh_name):
        raise Exception(f"{mesh_name} does not exist in the scene.")

    faces_with_ngons = []

    # Get the number of faces in the mesh
    num_faces = pm.polyEvaluate(mesh_name, face=True)

    # Iterate through all faces
    for i in range(num_faces):
        # Get the vertices of the face (ignoring UV or split normals issues)
        face_vertices = pm.polyListComponentConversion(f"{mesh_name}.f[{i}]", fromFace=True, toVertex=True)
        vertex_count = len(pm.ls(face_vertices, flatten=True))

        # If a face has more than 4 vertices, it's an n-gon
        if vertex_count > 4:
            faces_with_ngons.append(f"{mesh_name}.f[{i}]")

    return faces_with_ngons


class NgonValidator(Validator):
    required_type = str  # long mesh name

    def validate(self, data):
        ngon_ids = get_ngon_ids(mesh_name=data)

        state = NodeState.SUCCESS
        if list(ngon_ids):
            state = NodeState.FAIL
            message = f"{data} has n-gons: {len(ngon_ids)} found ({', '.join(ngon_ids[:5])}...)"

        data = ngon_ids

        return data, state, message
