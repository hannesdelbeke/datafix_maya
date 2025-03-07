from datafix.core import Validator, Action
import maya.cmds as cmds


class ClearHistory(Action):
    """delete construction history"""
    # todo a bool to say if running this action triggers revalidation
    def action(self):
        """data: long meshname"""
        cmds.delete(self.parent.data, constructionHistory=True)


class HistoryValidator(Validator):
    """check if the node has deleted it's construction history"""
    child_actions = [ClearHistory]

    def validate(self, data):
        """data: long meshname"""
        if len(cmds.listHistory(data)) > 1:
            raise Exception('Node has construction history')