import inspect
from pathlib import Path
from datafix_maya import types


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
