"""
This script update workpath of layers in all mxd files in a specific dict (subdict included)
"""

import arcpy, os

def get_rutes(rutes = [], ruta_global):
     # get all rutes with mxd files
    for root, dirs, files in os.walk(ruta_global):
        for file in files:
            if file.endswith(".mxd"):
                 rutes.append(root)
    return list(set(rutes)) # return only unique rutes
       
def update_dict(mxd):

    df = arcpy.mapping.ListDataFrames(mxd, '')[0] # Chooses the first dataframe

    for lyr in arcpy.mapping.ListLayers(mxd, '', df): # Loop through layers
        if lyr.supports("DATASOURCE"):
            try:
                source_layer_old = lyr.workspacePath # ruta de la capa
                new_source_string = source_layer_old.replace(r'\proyectos2','')
                source_layer_new = os.path.normpath(new_source_string)
                lyr.findAndReplaceWorkspacePath(lyr.workspacePath, new_source_string)
                lyr.save
            except:
                pass
    return

ruta_global = r"\\ruta\global"

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
        #actualizar rutas
        update_dict(mxd)
        #save map doucment change
        mxd.save()
