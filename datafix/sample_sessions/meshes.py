import maya.cmds as cmds


def create_test_scene():
    cmds.file(new=True, force=True)  # Start a new scene

    test_meshes = []
    spacing = 5  # Distance between objects in the grid
    grid_size = 3  # Number of columns before starting a new row

    # Define test objects and their issues
    test_objects = [
        ("ngon_test", lambda: cmds.polyCreateFacet(p=[(-1, 0, -1), (1, 0, -1), (1.5, 0, 1), (0, 0, 2), (-1.5, 0, 1)])),
        # Ngon
        ("rotatedCube", lambda: cmds.polyCube()),  # Non-frozen rotation
        ("scaledSphere", lambda: cmds.polySphere()),  # Non-frozen scale
        ("historyPlane", lambda: cmds.polyPlane()),  # History not deleted
        ("toruz", lambda: cmds.polyTorus()),  # Misspelled name
        ("offsetCone", lambda: cmds.polyCone()),  # Transformed object
        ("extrudedCylinder", lambda: cmds.polyCylinder()),  # Extruded face history
    ]

    for i, (name, create_func) in enumerate(test_objects):
        obj = create_func()[0]

        # Apply specific issues
        if name == "ngon_test":
            cmds.move(3, 0, 0, obj)  # Offset transformation
        elif name == "rotatedCube":
            cmds.rotate(15, 30, 10, obj)
        elif name == "scaledSphere":
            cmds.scale(1.5, 2, 0.5, obj)
        elif name == "historyPlane":
            cmds.polyExtrudeFacet(obj + ".f[0]", ltz=1)  # Add history
        elif name == "extrudedCylinder":
            cmds.polyExtrudeFacet(obj + ".f[10]", ltz=1)  # Extrude a random face
        elif name == "offsetCone":
            cmds.move(-3, 2, 2, obj)  # Move it to a random offset

        # Grid positioning
        row = i // grid_size
        col = i % grid_size
        cmds.move(col * spacing, 0, -row * spacing, obj)

        test_meshes.append(obj)

    # Group everything together
    group = cmds.group(test_meshes, name="TestScene_Group")

    print("Test scene created with issues:")
    for mesh in test_meshes:
        print(f"- {mesh}")


def setup_datafix_session():
    # Create a new session
    active_session = Session()
    active_session.append(MeshLongNameCollector)  # Collect all meshes with long names
    active_session.append(NgonValidator)  # Validate all meshes for n-gons