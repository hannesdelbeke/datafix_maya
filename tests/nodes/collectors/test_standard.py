
# creat a mock for the maya cmds module

from unittest.mock import MagicMock, patch
import types
import sys

maya = types.ModuleType('maya')
maya_cmds = types.ModuleType('maya.cmds')
maya_api_open_maya = types.ModuleType('maya.api.OpenMaya')
maya_api = types.ModuleType('maya.api')

# hook up the modules so we can do e.g. 'import maya.cmds'
maya.cmds = maya_cmds
maya.api = maya_api
maya.api.OpenMaya = maya_api_open_maya

# Inject into sys.modules
sys.modules['maya'] = maya
sys.modules['maya.cmds'] = maya_cmds
sys.modules['maya.api'] = maya_api
sys.modules['maya.api.OpenMaya'] = maya_api_open_maya


@patch("maya.cmds", new_callable=MagicMock)
def test_maya_cmds_mock(mock_cmds):
    """ Test to ensure that the maya.cmds module is mocked correctly. """
    import maya.cmds
    mock_cmds.polySphere.return_value = ["pSphere1"]
    result = maya.cmds.polySphere()
    assert result == ["pSphere1"]


@patch("maya.cmds", new_callable=MagicMock)
def test_collector(mock_cmds):
    """ Test to ensure that the collector works as expected.
    a simple test to check a random collector (MeshCollector)"""
    from datafix.core import Collector, Session
    from datafix_maya.nodes.collectors import MeshCollector

    # mock_cmds.ls.return_value = ["mesh1", "mesh2"]
    # mock cmds.ls() so it returns a list of mesh names, if it's pass type= 'mesh'
    mock_cmds.ls.side_effect = lambda *args, **kwargs: ["mesh1", "mesh2"] if kwargs.get('type') == 'mesh' else []

    session = Session()
    collector = MeshCollector(session)
    session.run()

    assert [x.data for x in collector.children] == ["mesh1", "mesh2"]
