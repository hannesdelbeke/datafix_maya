from datafix.core import Validator, active_session, NodeState, Action
from maya import cmds


class FrozenTransformsValidator(Validator):
    def validate(self, data):
        """
        Validates whether the given mesh has n-gons.
        Raises an exception if n-gons are found.
        """
        # Get the number of faces in the mesh
        num_faces = cmds.polyEvaluate(data, face=True)

        # Iterate through all faces
        for i in range(num_faces):
            # Get the vertices of the face (ignoring UV or split normals issues)
            face_vertices = cmds.polyListComponentConversion(f"{data}.f[{i}]", fromFace=True, toVertex=True)
            vertex_count = len(cmds.ls(face_vertices, flatten=True))

            # If a face has more than 4 vertices, it's an n-gon
            if vertex_count > 4:
                self.state = NodeState.ERROR
                self.error_message = f"{data} has n-gons: {vertex_count} found ({', '.join(face_vertices[:5])}...)"
                raise Exception(self.error_message)

        return True