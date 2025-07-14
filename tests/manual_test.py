import sys
import os

path = r"D:\repos\datafix"
if path not in sys.path:
    sys.path.append(path)
path = r"/"
if path not in sys.path:
    sys.path.append(path)

import datafix
from datafix_maya.nodes.collectors import MeshCollector
from datafix_maya.nodes.validators.ngons import NgonValidator
from datafix.core import Session
from importlib import reload
reload(datafix.nodes.maya.collectors.long_name)
import datafix.core.session
reload(datafix.core.session)
import datafix.core
reload(datafix.core)
reload(datafix.nodes.maya.validators.ngons)
from maya import cmds

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