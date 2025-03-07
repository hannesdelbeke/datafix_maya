from datafix.core import Validator
import maya.cmds as cmds


class HistoryValidator(Validator):
    """check if the node has deleted it's construction history"""

    def validate(self, data):
        """data: long meshname"""
        if len(cmds.listHistory(data)) > 1:
            raise Exception('Node has construction history')