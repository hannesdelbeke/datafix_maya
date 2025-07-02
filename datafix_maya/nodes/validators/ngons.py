from datafix.core import Validator, active_session, NodeState, Action, Collector
import datafix_maya.types
from maya import cmds
import maya.api.OpenMaya as om
import maya.cmds as cmds
from collections import defaultdict
from maya.api.OpenMaya import MIntArray


def find_ngons(mesh_dag_paths: om.MItSelectionList ):
    # TODO test
    """
    mesh_dag_paths is a MSelectionList of mesh DAG paths.
    """
    # based on MIT licensed code from github.com/JakobJK/modelChecker

    # UUIDs are used to uniquely identify dependency graph nodes
    ngons = defaultdict(list)  # dictionary mapping UUIDs to lists of face indices with ngons
    selIt = om.MItSelectionList(mesh_dag_paths)  # iterator over list of mesh DAG paths

    while not selIt.isDone():  # iterate through selection list
        faceIt = om.MItMeshPolygon(selIt.getDagPath())  # iterator over mesh faces for current DAG path
        fn = om.MFnDependencyNode(selIt.getDagPath().node())  # create function set to access node metadata
        uuid = fn.uuid().asString()  # get UUID of current node as string

        while not faceIt.isDone():  # iterate through faces of current mesh
            numOfEdges = faceIt.getEdges()  # get list of edge indices for the current face
            if len(numOfEdges) > 4:  # check if face is an ngon (more than 4 edges)
                ngons[uuid].append(faceIt.index())  # add face index to list under this UUID
            faceIt.next()  # move to next face

        selIt.next()  # move to next selected object

    return ngons  # ngons is a dict of format [uuid: [face_indices]]



def find_ngons_slow(mesh_name):
    # tested and works, but might be slow, no open maya.
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

    return faces_with_ngons


class SelectNgons(Action):
    """delete construction history"""
    # todo a bool to say if running this action triggers revalidation
    def action(self):
        ngon_faces = find_ngons_slow(self.parent.data)  # format of [f"{mesh_name}.f[{i}]",...]
        cmds.select(ngon_faces, replace=True)


class NgonValidator(Validator):
    child_actions = [SelectNgons]
    required_type = datafix_maya.types.mesh  # long mesh name

    def validate(self, data):
        ngon_faces = find_ngons_slow(data)

        if ngon_faces:
            raise Exception(f"{data} has n-gons: {len(ngon_faces)} faces found")

        # long_mesh_name = data
        # dag_path = om.MSelectionList().add(long_mesh_name).getDagPath(0)
        # ngons =



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




