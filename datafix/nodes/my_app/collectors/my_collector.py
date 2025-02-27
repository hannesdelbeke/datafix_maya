from datafix.core.collector import Collector


class HelloWorldCollector(Collector):
    """Demo of a collector returning 2 strings"""
    def logic(self):
        return ["hello", "world"]
