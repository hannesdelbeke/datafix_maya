from datafix.nodes.my_app.validators.my_validator import GreetingsValidator
from datafix.nodes.my_app.collectors.my_collector import HelloWorldCollector
from datafix.core import active_session, NodeState


def test_my_validator():
    """
    some demo code of a validator for a datafix node
    we are testing some core datafix logic here for demo purposes,
    usually you only need to test your own logic
    """
    active_session.add(HelloWorldCollector)  # the validator needs a collector to validate
    active_session.add(GreetingsValidator)
    active_session.run()
    validator_node: GreetingsValidator = active_session.node_instances[1]
    validation_states = [result_node.state for result_node in validator_node.children]
    # ['hello', 'world'] is the output of the collector.
    # hello is a greeting, world is not. So the validator results should be [Success, Fail]
    assert validation_states == [NodeState.SUCCEED, NodeState.FAIL], f"Expected [NodeState.SUCCEED, NodeState.FAIL], got {validation_states}"
    # since there was a fail, the validator node should be in a fail state
    assert validator_node.state == NodeState.FAIL


if __name__ == '__main__':
    test_my_validator()
    print(active_session.report())
