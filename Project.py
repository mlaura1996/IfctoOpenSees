#Libraries
from re import A
import ifcopenshell
import pandas
import os
import gmsh


#IfcFiles
ifc_file = ifcopenshell.open('modellobase.ifc')

#Converting ifc to step
cmd = '.\IfcConvert modellobase.ifc modellobase.stp'
os.system(cmd)

#UseIfctoStepfile
gmsh.initialize()
gmsh.model.add("modellobase.stp")


gmsh.model.mesh.generate(3)

gmsh.model.geo.synchronize()
gmsh.fltk.run()
gmsh.write("modellobase.msh")
gmsh.finalize()










