from re import A
import ifcopenshell
import pandas

ifc_file = ifcopenshell.open('modello base.ifc')

#Getting all types of an IFC class, and listing what they are:

products = ifc_file.by_type('IfcProduct')
for product in products:
    print(product.is_a())

# use the converter 