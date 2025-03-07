from datafix.core import Validator, active_session, NodeState, Action
from maya import cmds


class ZeroTransformsAction(Action):
    """ An action that sets the transforms of a transform node to zero."""
    def action(self):
        """Sets the translation, rotation, and scale values of the transform node to zero."""
        cmds.xform(self.parent.data, translation=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))


# TODO this works on transforms, not shapes!
class ZeroTransformsValidator(Validator):
    """
    A validator that checks if a transform node has zeroed out transforms.
    """
    child_actions = [ZeroTransformsAction]
    def validate(self, data):
        """
        Validates whether the transform node has zeroed out transforms.
        Raises an exception if the transforms are not zeroed out.
        """
        if not cmds.objExists(data):
            raise Exception(f"{data} does not exist in the scene.")

        print("data", data)

        # Get the translation, rotation, and scale values of the transform node
        translate_values = cmds.xform(data, query=True, translation=True, worldSpace=True)
        rotate_values = cmds.xform(data, query=True, rotation=True, worldSpace=True)
        scale_values = cmds.xform(data, query=True, scale=True, worldSpace=True)

        # Check if any of the values are not zero (scale is 1 1 1
        if any(translate_values) or any(rotate_values) or scale_values != [1, 1, 1]:
            raise Exception(f"{data} has non-zero transforms: {translate_values}, {rotate_values}, {scale_values}")

