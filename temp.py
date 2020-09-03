import shutil
import glob

class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        #print ("Hi to All! My name is, {} and i am {} color".format(self.name, self.color))
        print("Hi to All! My name is, %s and i am %s color " % (self.name, self.color))

robot_first = Robot("R2D2", "grey")
print (robot_first.name)
print (robot_first.color)

robot_first.say()

from maya import cmds
import pymel.core as pm
cmds.polyCube()

