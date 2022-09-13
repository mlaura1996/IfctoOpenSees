import gmsh
import pandas
import ifcopenshell


gmsh.initialize()
gmsh.option.setNumber("General.Terminal", 1)
gmsh.model.add("test")

#geometry

#cube
point0 = gmsh.model.geo.add_point(0, 0, 0, 1e-1)
point1 = gmsh.model.geo.add_point(1, 0, 0, 1e-1)
point2 = gmsh.model.geo.add_point(1, 5, 0, 1e-1)
point3 = gmsh.model.geo.add_point(0, 5, 0, 1e-1)
point4 = gmsh.model.geo.add_point(0, 5, 3, 1e-1)
point5 = gmsh.model.geo.add_point(1, 5, 3, 1e-1)
point6 = gmsh.model.geo.add_point(1, 0, 3, 1e-1)
point7 = gmsh.model.geo.add_point(0, 0, 3, 1e-1)
point8 = gmsh.model.geo.add_point(4, 5, 0, 1e-1)
point9 = gmsh.model.geo.add_point(4, 4, 0, 1e-1)
point10 = gmsh.model.geo.add_point(1, 4, 0, 1e-1)
point11 = gmsh.model.geo.add_point(1, 4, 3, 1e-1)
point13 = gmsh.model.geo.add_point(4, 4, 3, 1e-1)
point14 = gmsh.model.geo.add_point(4, 5, 3, 1e-1)

#edge
line0 = gmsh.model.geo.add_line(point0, point1)
line1 = gmsh.model.geo.add_line(point1, point2)
line2 = gmsh.model.geo.add_line(point2, point3)
line3 = gmsh.model.geo.add_line(point3, point0)
line4 = gmsh.model.geo.add_line(point3, point4)
line5 = gmsh.model.geo.add_line(point4, point5)
line6 = gmsh.model.geo.add_line(point2, point5)
line7 = gmsh.model.geo.add_line(point5, point6)
line8 = gmsh.model.geo.add_line(point1, point6)
line9 = gmsh.model.geo.add_line(point6, point7)
line10 = gmsh.model.geo.add_line(point7, point0)
line11 = gmsh.model.geo.add_line(point7, point4)
line12 = gmsh.model.geo.add_line(point2, point8)
line13 = gmsh.model.geo.add_line(point8, point14)
line14 = gmsh.model.geo.add_line(point14, point5)
line15 = gmsh.model.geo.add_line(point14, point13)
line16 = gmsh.model.geo.add_line(point13, point9)
line17 = gmsh.model.geo.add_line(point9, point10)
line18 = gmsh.model.geo.add_line(point13, point11)
line19 = gmsh.model.geo.add_line(point8, point9)
line20 = gmsh.model.geo.add_line(point10, point11)
line21 = gmsh.model.geo.add_line(point10, point2)
line22 = gmsh.model.geo.add_line(point11, point5)

#faces
face1 = gmsh.model.geo.add_curve_loop([line0, line1, line2, line3])
gmsh.model.geo.add_plane_surface([face1])
face2 = gmsh.model.geo.add_curve_loop([line2, line4, line5, -line6])
gmsh.model.geo.add_plane_surface([face2])
face3 = gmsh.model.geo.add_curve_loop([-line1, line8, -line7, -line6])
gmsh.model.geo.add_plane_surface([face3])
face4 = gmsh.model.geo.add_curve_loop([-line0, -line10, -line9, -line8])
gmsh.model.geo.add_plane_surface([face4])
face5 = gmsh.model.geo.add_curve_loop([-line3, line4, -line11, line10])
gmsh.model.geo.add_plane_surface([face5])
face6 = gmsh.model.geo.add_curve_loop([line7, line9, line11, line5])
gmsh.model.geo.add_plane_surface([face6])
face7 = gmsh.model.geo.add_curve_loop([line12, line13, line14, -line6])
gmsh.model.geo.add_plane_surface([face7])
face8 = gmsh.model.geo.add_curve_loop([line13, line15, line16, -line19])
gmsh.model.geo.add_plane_surface([face8])
face9 = gmsh.model.geo.add_curve_loop([line21, line12, line19, line17])
gmsh.model.geo.add_plane_surface([face9])
face10 = gmsh.model.geo.add_curve_loop([line22, -line6, -line21, line20])
gmsh.model.geo.add_plane_surface([face10])
face11 = gmsh.model.geo.add_curve_loop([line20, -line18, line16, line17])
gmsh.model.geo.add_plane_surface([face11])
face12 = gmsh.model.geo.add_curve_loop([line15, line18, line22, -line14])
gmsh.model.geo.add_plane_surface([face12])

#volume
surface1 = gmsh.model.geo.add_surface_loop([face1, face2, face3, face4, face5, face6])
surface2 = gmsh.model.geo.add_surface_loop([face7, face8, face9, face10, face11, face12])
vol1 = gmsh.model.geo.add_volume([surface1])
vol2 = gmsh.model.geo.add_volume([surface2])

#physical group
gmsh.model.geo.add_physical_group([vol1,vol2])

#meshing
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("test.msh")
gmsh.fltk.run()
gmsh.finalize()



