from maya import cmds

SUFFIXES = {
    "mesh": "geo",
    "joint": "jnt",
    "camera": None,
    "ambientLight": "lgt"
}

DEFAULT_SUFFIX = "grp"

def rename(selection=False):
    """
    This function have rename any objects to have the correct suffix
    Args:
        selection: Wether or not we use current selection

    Returns:
        A list of all the objects we operated on
    """
    objects = cmds.ls(sl=selection, dag=True, long=True)

    if selection and not objects:
        raise RuntimeError("You don't have anything selected! How dare you?!")

    objects.sort(key=len, reverse=True)

    for obj in objects:
        short_name = obj.split("|")[-1]

        children = cmds.listRelatives(obj, children=True, fullPath=True) or []

        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(obj)

        suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)

        if not suffix:
            continue

        if obj.endswith('_'+suffix):
            continue

        newName = "%s_%s" % (short_name, suffix)     #short_name + "_" + suffix

        cmds.rename(obj, newName)

        index = objects.index(obj)
        objects[index] = obj.replace(short_name, newName)

    return objects