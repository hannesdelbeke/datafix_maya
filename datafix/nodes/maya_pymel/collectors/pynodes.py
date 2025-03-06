from datafix.core.collector import Collector
from maya import cmds
import pymel.core as pm
from datafix.nodes.maya_pymel.actions.select_pynode import SelectNode


class _PynodeCollector(Collector):
    def __init__(self, *args, **kwargs):
        super(_PynodeCollector, self).__init__(*args, **kwargs)
        self.child_actions = [SelectNode]

    def collect(self):
        raise NotImplementedError


class MeshCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='mesh')


class MaterialCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='shadingEngine')


class TransformCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='transform')


class CameraCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='camera')


class LightCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='light')


class JointCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='joint')


class CurveCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='nurbsCurve')


class SurfaceCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='nurbsSurface')


class DeformerCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='deformer')


class ConstraintCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='constraint')


class LocatorCollector(_PynodeCollector):
    def collect(self):
        return pm.ls(type='locator')

