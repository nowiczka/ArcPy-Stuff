"""
This script set relative paths property of all mxd files in a specific dict (subdict included)
"""

import arcpy, os


def get_rutes(rutes = [], ruta_global):
     # get all rutes with mxd files
    for root, dirs, files in os.walk(ruta_global):
        for file in files:
            if file.endswith(".mxd"):
                 rutes.append(root)
    return list(set(rutes)) # return only unique rutes
    
""" INPUT DATA """
ruta_global = r"\\global\\path"

# find all *mxd file
     
rutes = get_rutes(ruta_global):
                
for Workspace in rutes[1:]: # there was an error when trying to open the first fill (probably somneone has opened it in the same time)

    #workspace to search for MXDs
    arcpy.env.workspace = Workspace

    #list map documents in folder
    mxdList = arcpy.ListFiles("*.mxd")

    #set relative path setting for each MXD in list.
    for file in mxdList:
        #set map document to change
        filePath = os.path.join(Workspace, file)
        mxd = arcpy.mapping.MapDocument(filePath)
        #set relative paths property
        mxd.relativePaths = True
        #save map doucment change
        mxd.save()
        
