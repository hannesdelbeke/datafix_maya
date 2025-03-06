from datafix.core import Validator, active_session, NodeState, Action
from maya import cmds
import logging

import maya.api.OpenMaya as om
import maya.cmds as cmds
from collections import defaultdict
from typing import List
from maya.api.OpenMaya import MIntArray


# def get_ngon_ids(mesh_name) -> MIntArray:
#     """Finds ngons (faces with more than 4 sides) in the given mesh."""
#     ngons = om.MIntArray()  # Store ngon face IDs
#
#     if not cmds.objExists(mesh_name):
#         logging.error(f"{mesh_name} does not exist in the scene.")
#         return ngons
#
#     # Get the DAG path of the mesh
#     selection = om.MSelectionList()
#     selection.add(mesh_name)
#     dag_path = selection.getDagPath(0)
#
#     if not dag_path.hasFn(om.MFn.kMesh):
#         logging.error(f"{mesh_name} is not a mesh.")
#         return ngons
#
#     mesh_fn = om.MFnMesh(dag_path)
#     poly_iter = om.MItMeshPolygon(dag_path)  # Iterate over all faces
#
#     while not poly_iter.isDone():
#         if poly_iter.polygonVertexCount() > 4:
#             ngons.append(poly_iter.index())  # Store the ngon index
#
#         poly_iter.next()
#
#     return ngons



def find_ngons_slow(mesh_name):
    # TODO, tested and works, but might be slow, no open maya.
    """
    Validates whether the given mesh has n-gons.
    Raises an exception if n-gons are found.
    """
    if not cmds.objExists(mesh_name):
        raise Exception(f"{mesh_name} does not exist in the scene.")

    faces_with_ngons = []

    # Get the number of faces in the mesh
    num_faces = cmds.polyEvaluate(mesh_name, face=True)

    # Iterate through all faces
    for i in range(num_faces):
        # Get the vertices of the face (ignoring UV or split normals issues)
        face_vertices = cmds.polyListComponentConversion(f"{mesh_name}.f[{i}]", fromFace=True, toVertex=True)
        vertex_count = len(cmds.ls(face_vertices, flatten=True))

        # If a face has more than 4 vertices, it's an n-gon
        if vertex_count > 4:
            faces_with_ngons.append(f"{mesh_name}.f[{i}]")

    if faces_with_ngons:
        raise Exception(f"{mesh_name} has n-gons: {len(faces_with_ngons)} found ({', '.join(faces_with_ngons[:5])}...)")

    return True


class NgonValidator(Validator):
    required_type = str  # long mesh name

    def validate(self, data):
        find_ngons_slow(data)
        # ngon_ids = get_ngon_ids(mesh_name=data)
        #
        # state = NodeState.SUCCESS
        #
        # # if list(ngon_ids):
        #     state = NodeState.FAIL
        #     message = f"{data} has n-gons: {len(ngon_ids)} found ({', '.join(ngon_ids[:5])}...)"
        #
        # data = ngon_ids
        #
        # return data, state, message


# class NGonSelect(Action):

    #     """
    #     Validates whether the given mesh has n-gons.
    #     Raises an exception if n-gons are found.
    #     """
    #     if not cmds.objExists(data):
    #         raise Exception(f"{data} does not exist in the scene.")
    #
    #     faces_with_ngons = []
    #
    #     # Get the number of faces in the mesh
    #     num_faces = cmds.polyEvaluate(data, face=True)
    #
    #     # Iterate through all faces
    #     for i in range(num_faces):
    #         # Get the vertices of the face (ignoring UV or split normals issues)
    #         face_vertices = cmds.polyListComponentConversion(f"{data}.f[{i}]", fromFace=True, toVertex=True)
    #         vertex_count = len(cmds.ls(face_vertices, flatten=True))
    #
    #         # If a face has more than 4 vertices, it's an n-gon
    #         if vertex_count > 4:
    #             faces_with_ngons.append(f"{data}.f[{i}]")
    #
    #     if faces_with_ngons:
    #         raise Exception(f"{data} has n-gons: {len(faces_with_ngons)} found ({', '.join(faces_with_ngons[:5])}...)")
    #
    #     return True

    # def find_ngons(self, SLMesh):
    #     # TODO advanced validator. doesn't just fail. it collects which faces are ngons
    #     #  we actually don't need to know which faces are ngons, untill the user wants to fix them



# def iter_ngons(selection_list_mesh):
#     """
#     Find ngons (polygons with more than 4 edges) in the selected mesh.
#     returns a dictionary with the mesh UUID as key and a list of face indices as value.
#     """
#     ngons = defaultdict(list)
#     sel_it = om.MItSelectionList(selection_list_mesh)
#     while not sel_it.isDone():
#         face_it = om.MItMeshPolygon(sel_it.getDagPath())
#         fn = om.MFnDependencyNode(sel_it.getDagPath().node())
#         uuid = fn.uuid().asString()
#         while not face_it.isDone():
#             num_of_edges = face_it.getEdges()
#             if len(num_of_edges) > 4:
#                 ngons[uuid].append(face_it.index())
#             face_it.next()
#         sel_it.next()
#     return ngons




