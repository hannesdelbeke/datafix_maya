from datafix.core import Validator
from maya import cmds


class ValidateEnsureMesh(Validator):
    """ensure we have at least 1 mesh in scene"""
    def run(self):
        meshes = cmds.ls(type='mesh')
        if not meshes:
            raise ValueError("No meshes found in the scene. Please create or import a mesh before proceeding.")
