#Libraries
from re import A
from tkinter import Y
import ifcopenshell
import pandas
import os
import gmsh
import sys 


# #IfcFiles
# ifc_file = ifcopenshell.open('modellobase.ifc')
# # ifc_file = ifcopenshell.open('aggregate.ifc')

# # #Converting ifc to step
# cmd = '.\IfcConvert modellobase.ifc --use-element-guids teste.stp'
# # cmd = '.\IfcConvert aggregate.ifc --use-element-guids modellobase.stp '

# os.system(cmd)

#UseIfctoStepfile
gmsh.initialize()

gmsh.model.mesh.setOrder(2)
gmsh.option.setNumber("General.Terminal", 1)
gmsh.model.add("modellobasep")
gmsh.merge("modellobase.stp")

#coherence between solid
gmsh.model.occ.fragment(gmsh.model.occ.getEntities(3), [])
gmsh.model.occ.synchronize()


#Get dimension tag

x = gmsh.model.getEntities(dim = -1)

gmsh.model.mesh.setSize(x, 150)

gmsh.model.mesh.generate(3)

#gmsh.model.geo.synchronize()
gmsh.fltk.run()
gmsh.write("modellobase.msh")


gmsh.finalize()











