#Libraries
from re import A
from tkinter import Y
import ifcopenshell
import pandas
import os
import gmsh


#IfcFiles
ifc_file = ifcopenshell.open('modellobase.ifc')

#Converting ifc to step
cmd = '.\IfcConvert modellobase.ifc modellobase.stp'
os.system(cmd)

gmsh.initialize()
SetFactory("OpenCASCADE")