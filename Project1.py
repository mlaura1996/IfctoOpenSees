import gmsh
import pandas
import ifcopenshell


y = pandas.DataFrame(columns=['coluna'])
gmsh.initialize()
gmsh.fltk.run()
gmsh.finalize()
