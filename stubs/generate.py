import inspect
from pathlib import Path
from datafix_maya import types


def generate_node_type_code():
    """run this in maya to get a list of all node types"""
    import maya.cmds as cmds  # noqa
    node_types = cmds.ls(nt=True)  # 'AISEnvFacade', 'AlembicNode', ...
    for name in node_types:
        print(f"{name} = NewType('{name}', str)")
    # now copy the code from the console, and paste it in types.py


def generate_collector_stubs():
    stub_file = Path(r"D:\repos\datafix_maya\nodes\collectors\datafix_maya\collectors.pyi")
    output_lines = [
        "from typing import List",
        "from datafix.core.collector import Collector",
        "from datafix_maya.nodes.actions.select_node import SelectNodeByName",
        "from datafix_maya import types",
        "",
        "class _NodeCollector(Collector):",
        "    child_actions: list = [SelectNodeByName]",
        "    def run(self): ...",
        "",
    ]

    for name, obj in inspect.getmembers(types):
        if hasattr(obj, '__supertype__') and isinstance(obj.__supertype__, type):
            output_lines.append(f"class {name}Collector(_NodeCollector):")
            output_lines.append(f"    def collect(self) -> List[types.{name}]: ...")
            output_lines.append("")

    stub_file.write_text("\n".join(output_lines))
    print(f"✅ Stub written to: {stub_file.resolve()}")
