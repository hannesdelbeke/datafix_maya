from datafix.core import Validator, Action
import maya.cmds as cmds


class ClearHistory(Action):
    """delete construction history"""
    # todo a bool to say if running this action triggers revalidation
    def action(self):
        cmds.delete(self.parent.data, constructionHistory=True)


class HistoryValidator(Validator):
    """check if the node has deleted its construction history"""
    child_actions = [ClearHistory]

    def validate(self, data):
        """data: long meshname, or long material name, or ..."""
        if len(cmds.listHistory(data)) > 1:
            raise Exception('Node has construction history')