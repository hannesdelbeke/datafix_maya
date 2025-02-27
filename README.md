# datafix_nodes_template

example repos that use this template
- maya
- blender
- windows
- perforce
- git
- svn

## dev notes
feel free to delete these dev notes once you copied this repo template

1. To prevent clashing with the core datafix import handling., it's important to not use `__init__.py` files in your python packages.  
To create datafix nodes within the datafix namespace, simply use the following folder structure, and Python should auto pick it up.

example for maya. replace maya with unreal/blender/... or your company/user name
```
datafix
    nodes
        maya
            validators
            collectors
            actions
            other  # for the rare special nodes
```
if using this folder structure, it appends the nodes to the exisitng datafix imports.
ensure you do not clash with default datafix node names & import paths.

2. add unittest instructions

