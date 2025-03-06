import sys
import os

path = r"D:\repos\datafix"
if path not in sys.path:
    sys.path.append(path)
path = r"D:\repos\datafix_maya"
if path not in sys.path:
    sys.path.append(path)

import datafix
from datafix.nodes.maya.collectors.mesh_long_name import MeshLongNameCollector
from datafix.nodes.maya.validators.no_ngons import NgonValidator
from datafix.core import active_session, Session
from importlib import reload
reload(datafix.nodes.maya.collectors.mesh_long_name)
import datafix.core.session
reload(datafix.core.session)
import datafix.core
reload(datafix.core)
reload( datafix.nodes.maya.validators.no_ngons )
from maya import cmds
from datafix.nodes.maya.collectors.mesh_long_name import MeshLongNameCollector

# make a cube and a sphere if not exist yet
if not cmds.objExists("myCube"):
    cmds.polyCube(name="myCube")
if not cmds.objExists("mySphere"):
    cmds.polySphere(name="mySphere")

active_session = Session()
datafix.core.active_session = active_session
active_session.append(MeshLongNameCollector)  # the validator needs a collector to validate
active_session.append(NgonValidator)

## command line
# active_session.run()
# print(active_session.report())

# UI
import datafix.ui.validator as v
reload(v)
w = v.show()