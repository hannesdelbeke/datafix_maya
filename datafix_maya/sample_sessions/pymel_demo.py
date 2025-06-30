from datafix.core import Session, Validator, Collector, NodeState
from datafix_maya.nodes.pymel.collectors.pynodes import MeshCollector, MaterialCollector
from pymel import core as pm


# make a cube and a sphere if not exist yet
if not pm.objExists("myCube"):
    pm.polyCube(name="myCube")
if not pm.objExists("mySphere"):
    pm.polySphere(name="mySphere")

# create 3 materials and assign to the cube
if not pm.objExists("myMat1"):
    pm.shadingNode('lambert', asShader=True, name="myMat1")
if not pm.objExists("myMat2"):
    pm.shadingNode('lambert', asShader=True, name="myMat2")
if not pm.objExists("myMat3"):
    pm.shadingNode('lambert', asShader=True, name="myMat3")

# assign materials
pm.select("myCube")
pm.hyperShade(assign="myMat1")
pm.select("myCube.f[0:2]")  # select first 3 faces from cube
pm.hyperShade(assign="myMat2")
pm.select("mySphere")
pm.hyperShade(assign="myMat3")

# delete a edge from the sphere to create a ngon
pm.select("mySphere.e[0]")
pm.delete()

# create a session
session = Session()
collector = MeshCollector(parent=session)
MaterialCollector(parent=session)
session.run()

