from maya import cmds

materials = cmds.ls(mat=True)

mat_list = []

for material in materials:
    
    if material != "blinn1" and material != "particleCloud1":
        type = cmds.objectType(material)
        
        if type != "lambert":
            mat_list.append(material)

            print('*' * (len(material)+6))
            print("Incorrect material type: %s" % material)


cmds.select(mat_list)