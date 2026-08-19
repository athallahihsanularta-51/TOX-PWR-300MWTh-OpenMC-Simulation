import openmc
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot
import openmc.deplete
import pandas as pd
import numpy as np

#Material definition
UO2 = openmc.Material (1, "UO2")
UO2.add_nuclide('U234', 6.2342e-06)
UO2.add_nuclide('U235', 2.3090e-03)
UO2.add_nuclide('U238', 2.0774e-02)
UO2.add_nuclide('O16', 4.6119e-02)
UO2.add_nuclide('O17', 1.7517e-05)
UO2.add_nuclide('O18', 9.2459e-05)
UO2.set_density('g/cc',10.3440)

ThO2 = openmc.Material (99, "ThO2")
ThO2.add_element('O', 0.121191)
ThO2.add_element('Th', 0.878809)
ThO2.set_density('g/cc', 10.0000)

TOX = openmc.Material.mix_materials ([UO2, ThO2], [0.60, 0.40], 'wo')
TOX.temperature = 900
TOX.volume = math.pi*0.56437**2*150*264*100 #phi x r^2 x h x total cel dalam assembly x total assembly dalam teras

clads = openmc.Material(88, name='Zircaloy-4')
clads.set_density('g/cc', 6.56)
clads.add_element('O', 0.000295)
clads.add_element('Cr', 0.000076)
clads.add_element('Fe', 0.000141)
clads.add_element('Zr', 0.042520)
clads.add_element('Sn', 0.000464)
#clad.temperature = 800.0

water = openmc.Material(77, name='Water')
water.set_density('g/cm3', 0.76)
water.add_element('H', 2)
water.add_element('O', 1)
water.add_s_alpha_beta('c_H_in_H2O')

water2 = openmc.Material(66, name='Water Vapor')
water2.set_density('g/cm3', 0.000756)
water2.add_element('H', 0.111894, 'wo')
water2.add_element('O', 0.888106, 'wo')

#coolant.temperature = 750.0
'''
ref = openmc.Material( name = 'Berilium Oksida')
ref.set_density( 'sum' )
ref.add_element( 'Be' , 0.072473  )
ref.add_element( 'O' , 0.072473  )
'''
ref = openmc.Material (3, name='Stainless Steel 316') 
ref.set_density('g/cm3', 8.000000)
ref.add_element('C', 0.000410, 'wo')
ref.add_element('Si', 0.005070, 'wo')
ref.add_element('P', 0.000230, 'wo')
ref.add_element('S', 0.000150, 'wo')
ref.add_element('Cr', 0.170000, 'wo')
ref.add_element('Mn', 0.010140, 'wo')
ref.add_element('Fe', 0.669000, 'wo')
ref.add_element('Ni', 0.120000, 'wo')
ref.add_element('Mo', 0.025000, 'wo')

cr = openmc.Material (4, name='ControlRod B4C')
cr.set_density('g/cm3', 1.76)
cr.add_nuclide('B10', 1.5206E-02)
cr.add_nuclide('B11', 6.1514E-02)
cr.add_nuclide('C12', 1.8972E-02)
cr.add_nuclide('C13', 2.1252E-04)

mat = openmc.Materials([ TOX , clads , water, water2, ref, cr])
mat.export_to_xml()

#Geometry
##arah radial
pitch = 1.4
s1 = openmc.ZCylinder(r=0.56437, surface_id=1) 
s2 = openmc.ZCylinder(r=0.57224, surface_id=2) 
s3 = openmc.ZCylinder(r=0.65312, surface_id=3)  
s4 = openmc.ZCylinder(r=0.7, surface_id=4)
s5 = openmc.ZCylinder(r=119 , surface_id = 69)
s6 = openmc.ZCylinder(r=130.9 , surface_id = 79, boundary_type ='vacuum')

#CR
c1 = openmc.ZCylinder(r=0.41491, surface_id=11) 
c2 = openmc.ZCylinder(r=0.42761, surface_id=12) 
c3 = openmc.ZCylinder(r=0.52540, surface_id=13)
c4 = openmc.ZCylinder(r=0.60287, surface_id=14) 
c5 = openmc.ZCylinder(r=0.64351, surface_id=15)

#WV
g1 = openmc.ZCylinder(r=0.62379, surface_id=21)
g2 = openmc.ZCylinder(r=0.66443, surface_id=31)

##arah axial
asmbly_reg = openmc.model.RectangularPrism(width=23.8, height=23.8, origin=(0,0))
box = openmc.model.RectangularPrism(width=238, height=238, origin=(0,0))
o_box = openmc.model.RectangularPrism(width=261.8, height=261.8, boundary_type ='vacuum')
top = openmc.ZPlane(z0=150, surface_id=37, boundary_type ='vacuum')
bottom = openmc.ZPlane(z0=-150, surface_id=38, boundary_type ='vacuum')
#a3 = openmc.ZPlane(z0=-161.9, surface_id=9)
#a4 = openmc.ZPlane(z0= 161.9, surface_id=10)

#Empty Space
mod_cell = openmc.Cell ( cell_id = 1 , fill = water )
mod_cell_all = openmc.Universe( universe_id = 1 , cells = (mod_cell,))


fuel_cell = openmc.Cell( cell_id = 2 , fill = TOX , region = -s1 )
gap_cell = openmc.Cell( cell_id = 3 , fill = water , region = +s1 & -s2 )
clad_cell = openmc.Cell( cell_id = 4 , fill = clads , region = +s2 & -s3 )
coolant_cell = openmc.Cell( cell_id = 5 , fill = water , region = +s3 )
outer_coolant = openmc.Cell( cell_id = 6 , fill = water , region =+s4 )
fpincell = openmc.Universe(universe_id=2, cells=(fuel_cell , gap_cell , clad_cell , coolant_cell, outer_coolant))

c11 = openmc.Cell( cell_id = 11 , fill = cr , region = -c1 )
c12 = openmc.Cell( cell_id = 12 , fill = water , region = +c1 & -c2 )
c13 = openmc.Cell( cell_id = 13 , fill = ref , region = +c2 & -c3 )
c14 = openmc.Cell( cell_id = 14 , fill = water , region = +c3 & -c4 )
c15 = openmc.Cell( cell_id = 15 , fill = clads , region =+c4 & -c5 )
c16 = openmc.Cell( cell_id = 16 , fill = water , region =+c5 )
cpincell = openmc.Universe(universe_id=3, cells=(c11, c12, c13, c14, c15, c16))

g11 = openmc.Cell( cell_id = 21 , fill = water2 , region = -g1 )
g12 = openmc.Cell( cell_id = 22 , fill = clads , region = +g1 & -g2 )
g13 = openmc.Cell( cell_id = 23 , fill = water , region = +g2 )
gpincell = openmc.Universe(universe_id=4, cells=(g11, g12, g13))

#Set positions occupied by guide tubes
tube_x1 = np.array([5, 8, 11, 3, 13, 2, 5, 8, 11, 14, 2, 5, 11, 14, 2, 5, 8, 11, 14, 3, 13, 5, 8, 11])
tube_y1 = np.array([2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 8, 8 , 8, 8, 11, 11, 11, 11, 11, 13, 13, 14, 14, 14])
#Set positions occupied by Control Rod
tube_x2 = np.array([8])
tube_y2 = np.array([8])	

#Define fuel lattices	
lat = openmc.RectLattice( lattice_id = 100 , name = 'assembly')
lat. lower_left = (-11.9, -11.9)
lat.pitch = (1.4, 1.4)
lat.universes = np.tile(fpincell, (17, 17))
lat.universes[tube_x1, tube_y1] = gpincell
lat.universes[tube_x2, tube_y2] = cpincell 
lat.outer = mod_cell_all

#lat.universes = [[fpincell]*36,[fpincell]*30,[fpincell]*24,[fpincell]*18,[fpincell]*12,[fpincell]*6,[fpincell]*1]
assembly = openmc.Cell(cell_id=7, fill=lat, region= -asmbly_reg)
#out_in_assembly  = openmc.Cell(cell_id= 8, fill=water, region=-a4 & +a3)
fuel_assembly_universe = openmc.Universe(universe_id= 5, cells=[assembly])

# Membuat kisi teras
core_lat = openmc.RectLattice(lattice_id = 900 , name = 'teras')
core_lat.lower_left = (-119,-119)
core_lat.pitch = (23.8, 23.8)
core_lat.outer = mod_cell_all

core_lat.universes = [
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10,
[fuel_assembly_universe]*10]

''' core_u = openmc.Universe(universe_id=1000, "root universe")
    t1 = openmc.Cell(cell_id=58, fill=core_lat, region= -s5 & -a4 & +a3)
    t2 = openmc.Cell(cell_id = 59 , fill = water, region =  -s5 & -top & +bottom )
    t3 = openmc.Cell(cell_id =60 , fill = ref, region =  +s5 & -s6  & -top & +bottom)
 core_u.add_cells((t1, t2, t3))  
geom = openmc.Geometry (core_u)
geom.export_to_xml() 
'''
core = openmc.Cell(cell_id=58, fill=core_lat, region= -box)
#out_core = openmc.Cell(cell_id=20, fill=helium_cell_all, region=+s5 & -a8 & +a7)

coolant_r_s = openmc.Cell (cell_id = 59 , fill = water, region =  -box & -top & +bottom)

ref_r = openmc.Cell (cell_id =60 , fill = ref, region =  +box & -o_box)

core_u = openmc.Universe(universe_id=1000, cells=[core,coolant_r_s,ref_r])

geom = openmc.Geometry (core_u)
geom.export_to_xml()

H =261.8  
D = 323.8
point=openmc.stats.Point((0,0,0))
src= openmc.IndependentSource(space=point)

settings = openmc.Settings()
settings.source = src
settings.batches = 100
settings.inactive = 30
settings.particles = 50000
settings.export_to_xml()

plot = openmc.Plot()
plot.filename = 'Teras'
plot.origin = (0,0,0)
plot.width = (400,400)
plot.pixels = (4000, 4000)
plot.color = 'material'
plot.basis = 'xy'
plots = openmc.Plots([plot])
plots.export_to_xml()

openmc.plot_geometry()
openmc.run()

model = openmc.Model(geometry=geom, settings=settings)
power = 300e6
chain = openmc.deplete.Chain.from_xml("./chain_endf_b8.0_pwr.xml")
operator = openmc.deplete.CoupledOperator(model, "./chain_endf_b8.0_pwr.xml")
time_steps = [30]*24

###############################################################################################################################################################################################
############################################################################################### Tallies.xml ###################################################################################
###############################################################################################################################################################################################
#Define surface used to construct region
zmin, zmax, radius = -H/2.,H/2.,D/2.

#create filter
#energy filter 
energy_filter = openmc.EnergyFilter([1,10e6])
#u_filter
u_filter = openmc.UniverseFilter(core_u)
#Spatial Legendre Filter
legendre_filter =openmc.SpatialLegendreFilter(10,'z',zmin,zmax)
#Zernike Filter
zernike_filter = openmc.ZernikeFilter(order=10,x=0.0,y=0.0,r=radius)
#Zernike Radial Filter
zer_radial_filter =openmc.ZernikeRadialFilter(order=10,x=0.0,y=0.0,r=radius)

#Create fission tally using spatial filter
fis_tally_legendre = openmc.Tally(name = "fis_tally_legendre")
fis_tally_legendre.scores=['fission']
fis_tally_legendre.filters =[u_filter,legendre_filter,energy_filter]

#Create Zernike azimuthal polinominal expansion filter and add to tally
fis_tally_zernike = openmc.Tally(name = "fis_tally_zernike")
fis_tally_zernike.scores=['fission']
fis_tally_zernike.filters =[u_filter,zernike_filter,energy_filter]

#Create Zernike radial polinominal expansion filter and add to tally
fis_tally_zernike_radial = openmc.Tally(name = "fis_tally_zernike_radial")
fis_tally_zernike_radial.scores=['fission']
fis_tally_zernike_radial.filters =[u_filter,zer_radial_filter,energy_filter]

#Create fission tally using spatial filter
flux_tally_legendre = openmc.Tally(name = "flux_tally_legendre")
flux_tally_legendre.scores=['flux']
flux_tally_legendre.filters =[u_filter,legendre_filter,energy_filter]

#Create Zernike azimuthal polinominal expansion filter and add to tally
flux_tally_zernike = openmc.Tally(name = "flux_tally_zernike")
flux_tally_zernike.scores=['flux']
flux_tally_zernike.filters =[u_filter,zernike_filter,energy_filter]

#Create Zernike radial polinominal expansion filter and add to tally
flux_tally_zernike_radial = openmc.Tally(name = "flux_tally_zernike_radial")
flux_tally_zernike_radial.scores=['flux']
flux_tally_zernike_radial.filters =[u_filter,zer_radial_filter,energy_filter]
#Create Heating Tally with Universe and energy filter
heating_tally = openmc.Tally(name = "heating_tally ")
heating_tally.scores = ['heating']
heating_tally.filters = [u_filter , energy_filter ]
#Ceate tally
tallies = openmc.Tallies([flux_tally_legendre,flux_tally_zernike,flux_tally_zernike_radial,fis_tally_legendre,fis_tally_zernike,fis_tally_zernike_radial,heating_tally])
tallies.export_to_xml()

integrator = openmc.deplete.PredictorIntegrator(operator, time_steps, power, timestep_units='d')
integrator.integrate()

                                                              
