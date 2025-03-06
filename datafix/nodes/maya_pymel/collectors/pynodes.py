from datafix.core.collector import Collector
from maya import cmds
import pymel.core as pm
from datafix.nodes.maya_pymel.actions.select_pynode import SelectNode


class _PynodeCollector(Collector):
    def __init__(self):
        self.child_actions = [SelectNode]

    def collect(self):
        raise NotImplementedError


class MeshCollector(SelectNode):
    def collect(self):
        return pm.ls(type='mesh')


class MaterialCollector(SelectNode):
    def collect(self):
        return pm.ls(type='shadingEngine')


class TransformCollector(SelectNode):
    def collect(self):
        return pm.ls(type='transform')


class CameraCollector(SelectNode):
    def collect(self):
        return pm.ls(type='camera')


class LightCollector(SelectNode):
    def collect(self):
        return pm.ls(type='light')


class JointCollector(SelectNode):
    def collect(self):
        return pm.ls(type='joint')


class CurveCollector(SelectNode):
    def collect(self):
        return pm.ls(type='nurbsCurve')


class SurfaceCollector(SelectNode):
    def collect(self):
        return pm.ls(type='nurbsSurface')


class DeformerCollector(SelectNode):
    def collect(self):
        return pm.ls(type='deformer')


class ConstraintCollector(SelectNode):
    def collect(self):
        return pm.ls(type='constraint')


class LocatorCollector(SelectNode):
    def collect(self):
        return pm.ls(type='locator')

