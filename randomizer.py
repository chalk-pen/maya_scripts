from maya import cmds
import random


def createObjects(mode, numObjects=5):
    """This create objects. Supports Cubes, Spheres, Cylinder and Cones"""
    objList = []

    # create a number of objects of the given type
    for n in range(numObjects):
        if mode == 'Cube':
            obj = cmds.polyCube()
        elif mode == 'Sphere':
            obj = cmds.polySphere()
        elif mode == 'Cylinder':
            obj = cmds.polyCylinder()
        elif mode == 'Cone':
            obj = cmds.polyCone()
        else:
            cmds.error("I don't know what to create")

        objList.append(obj[0])

    return objList


def randomize(objList=None, minValue=0, maxValue=20):
    if objList is None:
        objList = cmds.ls(selection=True)

    for obj in objList:
        cmds.setAttr(obj + '.tx', random.randint(minValue, maxValue))
        cmds.setAttr(obj + '.ty', random.randint(minValue, maxValue))
        cmds.setAttr(obj + '.tz', random.randint(minValue, maxValue))


def showWindow():
    name = "RandomizerWindow"
    if cmds.window(name, query=True, exists=True):
        cmds.deleteUI(name)
    cmds.window(name, vis=True)
    cmds.showWindow()