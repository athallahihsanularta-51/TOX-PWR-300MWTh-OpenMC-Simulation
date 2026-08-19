import openmc
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot
import openmc.deplete
import pandas as pd
import numpy as np

UO2 = openmc.Material (1, "UO2")
UO2.add_nuclide('U234', 6.2342e-06)
UO2.add_nuclide('U235', 2.3090e-03)
UO2.add_nuclide('U238', 2.0774e-02)
UO2.add_nuclide('O16', 4.6119e-02)
UO2.add_nuclide('O17', 1.7517e-05)
UO2.add_nuclide('O18', 9.2459e-05)
UO2.set_density('g/cc',10.3440)

ThO2 = openmc.Material (1, "ThO2")
ThO2.add_element('O', 0.121191)
ThO2.add_element('Th', 0.878809)
ThO2.set_density('g/cc', 10.0000)

TOX = openmc.Material.mix_materials ([UO2, ThO2], [0.60, 0.40], 'wo')
TOX.temperature = 900
TOX.volume = math.pi*0.56437**2*100

clads = openmc.Material(name='Clad')
clads.set_density('g/cc', 6.56)
clads.add_element('O', 0.000295)
clads.add_element('Cr', 0.000076)
clads.add_element('Fe', 0.000141)
clads.add_element('Zr', 0.042520)
clads.add_element('Sn', 0.000464)

water = openmc.Material(name='Water')
water.set_density('g/cm3', 0.76)
water.add_element('H', 2)
water.add_element('O', 1)
water.add_s_alpha_beta('c_H_in_H2O')

materials = openmc.Materials([TOX, clads, water])
materials.export_to_xml() 
materials = openmc.Materials()
materials.append(TOX)
materials += [clads, water]

s1 = openmc.ZCylinder(r=0.56437)
s2 = openmc.ZCylinder(r=0.57224)
s3 = openmc.ZCylinder(r=0.62137)

fuel_region = -s1
gap_region = +s1 & -s2
clad_region = +s2 & -s3

fuel = openmc.Cell(name='fuel')
fuel.fill = TOX
fuel.region = fuel_region

gap = openmc.Cell(name='water gap')
gap.fill = water
gap.region = gap_region

clad = openmc.Cell(name='clad')
clad.fill = clads
clad.region = clad_region

pitch = 1.4
left = openmc.XPlane(-pitch/2, boundary_type='reflective')
right = openmc.XPlane(pitch/2, boundary_type='reflective')
bottom = openmc.YPlane(-pitch/2, boundary_type='reflective')
top = openmc.YPlane(pitch/2, boundary_type='reflective')

water_region = +left & -right & +bottom & -top & +s3
moderator = openmc.Cell(name='moderator')
moderator.fill = water
moderator.region = water_region

box = openmc.model.RectangularPrism(width=pitch, height=pitch,
                                    boundary_type='reflective')
water_region = -box & +s3

root_universe = openmc.Universe(cells=(fuel, gap, clad, moderator))
geometry = openmc.Geometry(root_universe)
geometry.export_to_xml()

# Create a point source
point = openmc.stats.Point((0, 0, 0))
source = openmc.IndependentSource(space=point)
settings = openmc.Settings()
settings.source = source
settings.batches = 100
settings.inactive = 30
settings.particles = 50000
settings.export_to_xml()

cell_filter = openmc.CellFilter(fuel)
tally = openmc.Tally(1)
tally.filters = [cell_filter]
tally.nuclides = ['U235']
tally.scores = ['total', 'fission', 'absorption', '(n,gamma)']
tallies = openmc.Tallies([tally])
tallies.export_to_xml()

plot = openmc.Plot()
plot.filename = 'pin-1'
plot.origin = (0, 0, 0)
plot.width = (2, 2)
plot.pixels = (4000, 4000)
plot.color = 'material'
plot.basis = 'xy'
plots = openmc.Plots([plot])
plots.export_to_xml()

openmc.plot_geometry()
openmc.run()

chain = openmc.deplete.Chain.from_xml("./chain_endf_b8.0_pwr.xml")

model = openmc.Model(geometry=geometry, settings=settings)
operator = openmc.deplete.CoupledOperator(model, "./chain_endf_b8.0_pwr.xml")
power = 150
time_steps = [30]*24
integrator = openmc.deplete.PredictorIntegrator(operator, time_steps, power, timestep_units='d')

integrator.integrate()
