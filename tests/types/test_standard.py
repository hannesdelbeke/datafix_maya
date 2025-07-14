"""
test that the maya standard types are working correctly with validators and collectors.
"""

from datafix.core import Collector, Validator, Session, NodeState
from datafix_maya.types import Mesh, Transform


class CollectDummyMeshes(Collector):
    def collect(self):
        return [Mesh(name) for name in ["mesh1", "mesh2", "mesh3"]]


class CollectDummyTransforms(Collector):
    def collect(self):
        return [Transform(name) for name in ["transform1", "transform2"]]


class ValidateMeshes(Validator):
    required_type = Mesh

    def validate(self, data: Mesh):
        # if not, raise exception
        if not data.startswith("mesh"):
            raise ValueError(f"Invalid mesh name: {data}")


def test_required_type():
    # create pipeline
    session = Session(name="test_required_types")
    mesh_collector = CollectDummyMeshes(parent=session)
    transform_collector = CollectDummyTransforms(parent=session)
    mesh_validator = ValidateMeshes(parent=session)

    session.run()

    assert mesh_collector.state == NodeState.SUCCEED
    assert transform_collector.state == NodeState.SUCCEED
    assert len(transform_collector.children) == 2  # ensure we collected transforms
    validated_nodes = [result.data_node for result in mesh_validator.children]
    # check the mesh validator doesn't validate collected transforms
    assert validated_nodes == mesh_collector.children

