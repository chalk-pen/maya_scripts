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

    column = cmds.columnLayout()
    cmds.frameLayout(label="Choose an object type")

    cmds.columnLayout()
    cmds.radioCollection("objectCreationType")
    cmds.radioButton(label="Sphere")
    cmds.radioButton(label="Cube", select=True)
    cmds.radioButton(label="Cone")
    cmds.radioButton(label="Cylinder")

    cmds.intField("numObjects", value=4)

    cmds.setParent(column)
    frame = cmds.frameLayout("Choose your max range")

    cmds.gridLayout(numberOfColumns=2, cellWidth=100)

    for axis in 'xyz':
        cmds.text(label="%s axis" % axis)
        cmds.floatField("%sAxisField" % axis, value=random.uniform(0, 10))

    cmds.setParent(frame)
    cmds.rowLayout(numberOfColumns=2)

    cmds.radioCollection("randomMode")
    cmds.radioButton(label="Absolute", select=True)
    cmds.radioButton(label="Relative")

    cmds.setParent(column)
    cmds.rowLayout(numberOfColumns=2)
    cmds.button(label="Create", command=onCreateClick)
    cmds.button(label="Randomize")

def onCreateClick(*args):
    print ("Create button clicked")
    print ("hi")
    'hi'