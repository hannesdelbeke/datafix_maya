from datafix.core import Validator, Action
from maya import cmds
from datafix_maya.types import transform


class ZeroTransformsAction(Action):
    name = "Reset Transforms"
    def action(self):
        """Sets the translation, rotation, and scale values of the transform node to zero."""
        cmds.xform(self.parent.data, translation=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))


# TODO this works on transforms, not shapes!
class ZeroTransformsValidator(Validator):
    """Check if a transform node has zeroed-out transforms."""
    child_actions = [ZeroTransformsAction]
    required_type = transform

    def validate(self, data):
        translate_values = cmds.xform(data, query=True, translation=True, worldSpace=True)
        rotate_values = cmds.xform(data, query=True, rotation=True, worldSpace=True)
        scale_values = cmds.xform(data, query=True, scale=True, worldSpace=True)

        if translate_values != [0, 0, 0]:
            raise Exception(f"{data} has non-zero translation: {translate_values}")
        if rotate_values != [0, 0, 0]:
            raise Exception(f"{data} has non-zero rotation: {rotate_values}")
        if scale_values != [1, 1, 1]:
            raise Exception(f"{data} has non-default scale: {scale_values}")

