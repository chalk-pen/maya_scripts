from maya import cmds

SUFFIXES = {
    "mesh" = "geo",
    "joint" = "jnt",
    "camera" = None
}

DEFAULT_SUFFIX = "grp"

selection = cmds.ls(sl=True)

if len(selection) == 0:
    selection = cmds.ls(dag=True, long=True)

selection.sort(key=len, reverse=True)

for obj in selection:
    short_name = obj.split("|")[-1]

    children = cmds.listRelatives(obj, children=True, fullPath=True) or []

    if len(children) == 1:
        child = children[0]
        objType = cmds.objectType(child)
    else:
        objType = cmds.objectType(obj)

    if objType == "mesh":
        suffix = "geo"
    elif objType == "joint":
        suffix == "jnt"
    elif objType == "camera":
        print "Skipping camera"
        continue
    else:
        suffix = "grp"

    suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)

    if not suffix:
        continue

    if obj.endswith(suffix):
        continue

    newName = short_name + "_" + suffix

    cmds.rename(obj, newName)