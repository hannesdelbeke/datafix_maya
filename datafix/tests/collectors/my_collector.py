from datafix.nodes.my_app.collectors.my_collector import HelloWorldCollector
from datafix.core import active_session


def test_my_collector():
    """setup a session with our collector, run it, and verify it gives the expected result"""
    active_session.add(HelloWorldCollector)
    active_session.run()
    collector_node: "datafix.Node" = active_session.node_instances[0]
    assert [x.data for x in collector_node.children] == ['hello', 'world']


if __name__ == '__main__':
    """some debug code to run this sample in the IDE"""
    test_my_collector()
    print(active_session.report())
