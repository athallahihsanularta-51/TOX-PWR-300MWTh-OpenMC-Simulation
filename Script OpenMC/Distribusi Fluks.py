import openmc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

P = 30e7 #Watt
Q = 1.602 * 1.0e-19 #J/eV
V = 1.48*1.0e7 # cm3
##################################################### LEGENDRE ##########################################################
H = 320.8
D = 323.8
zmin, zmax, radius = -H/2., H/2, D/2
id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

axial = []
flux_legendre = []
for i in id:
    sp = openmc.StatePoint('openmc_simulation_n'+str(i)+'.h5')
    legendre_flux = sp.get_tally(name = 'flux_tally_legendre').get_pandas_dataframe()
    heat_flux = sp.get_tally(id = 7).get_pandas_dataframe()
    h_mean = np.array(heat_flux['mean'])
    flux_norm = np.array(((P/(Q*h_mean))/V))
    legendre_flux_mean = legendre_flux['mean']*flux_norm
    legendre_exponential = openmc.legendre_from_expcoef(legendre_flux_mean, domain=(zmin, zmax))
    z = np.linspace(zmin,zmax, 100)
    flux_legendre_z = legendre_exponential(z)
    flux_legendre.append(flux_legendre_z)
    axial.append(z)

import openpyxl
axial_data =  pd.DataFrame(list(map(np.ravel, axial)))

flux_legendre_data =  pd.DataFrame(list(map(np.ravel, flux_legendre)))
flux_legendre_data._append(axial_data[0])
flux_legendre_data.to_excel('data distribusi fluks legendre.xlsx')

fig, ax = plt.subplots()
for i in range (0,24):
    label = "Step ke-"+str(i)
    x = flux_legendre[i]
    y = axial[i]
    ax.plot(x,y, label =label)
    ax.set_xlabel('flux [neutron/cm2.s]')
    ax.set_ylabel('Core Height Position [cm]')
ax.legend(loc='upper right', bbox_to_anchor=(1.31, 1),
          fancybox=True, shadow=True, ncol=1)
plt.title('Distribusi Fluks Aksial (Legendre) ', y = 1.08)
plt.savefig('Distribusi Fluks Aksial Legendre.jpg',dpi = 1000, bbox_inches = 'tight')
#fig.show()

##################################################### ZERNIKE RADIAL ##########################################################
radial = []
flux_zernikerad = []
for i in id:
    sp = openmc.StatePoint('openmc_simulation_n'+str(i)+'.h5')
    zernikerad_flux = sp.get_tally(name = 'flux_tally_zernike_radial').get_pandas_dataframe()
    heat_flux = sp.get_tally(id = 7).get_pandas_dataframe()
    h_mean = np.array(heat_flux['mean'])
    flux_norm = np.array(((P/(Q*h_mean))/V))
    zernikerad_flux_mean = zernikerad_flux['mean']*flux_norm
    zernikerad_exponential = openmc.ZernikeRadial(zernikerad_flux_mean, radius=radius)
    r = np.linspace(-radius, radius, 100)
    flux_zernikerad_r = zernikerad_exponential(r)
    flux_zernikerad.append(flux_zernikerad_r)
    radial.append(r)

import openpyxl
radial_data =  pd.DataFrame(list(map(np.ravel, radial)))

flux_zernikerad_data =  pd.DataFrame(list(map(np.ravel, flux_zernikerad)))
flux_zernikerad_data._append(radial_data[0])
flux_zernikerad_data.to_excel('data distribusi fluks zernikerad.xlsx')

fig, ax = plt.subplots()
for i in range (0,24):
    label = "Step ke-"+str(i)
    y = flux_zernikerad[i]
    x = radial[i]
    ax.plot(x,y, label =label)
    ax.set_ylabel('flux [neutron/cm2.s]')
    ax.set_xlabel('Core Diamater Position [cm]')
ax.legend(loc='upper right', bbox_to_anchor=(1.31, 1),
          fancybox=True, shadow=True, ncol=1)
plt.title('Distribusi Fluks Aksial (zernikerad) ', y = 1.08)
plt.savefig('Distribusi Fluks Aksial zernikerad.jpg',dpi = 1000, bbox_inches = 'tight')
#fig.show()

##################################################### AKSIAL RADIAL ##########################################################
for i in range (1):
    	sp = openmc.StatePoint('openmc_simulation_n'+str(i)+'.h5')
    	legendre_flux = sp.get_tally(name = 'flux_tally_legendre').get_pandas_dataframe()
    	legendre_flux_mean = legendre_flux['mean']
    	legendre_exponential = openmc.legendre_from_expcoef(legendre_flux_mean, domain=(zmin, zmax))
    	z = np.linspace(zmin,zmax, 100)
    	zernikerad_flux = sp.get_tally(name = 'flux_tally_zernike_radial').get_pandas_dataframe()
    	zernikerad_flux_mean = zernikerad_flux['mean']
    	zernikerad_exponential = openmc.ZernikeRadial(zernikerad_flux_mean, radius=radius)
    	r = np.linspace(-radius, radius, 100)
    	flux_zernikerad_r = zernikerad_exponential(r)
    	flux = np.array([legendre_exponential(z)]).T  @ np.array([zernikerad_exponential(r)])
heat_flux = sp.get_tally(id = 7).get_pandas_dataframe()
h_mean = np.array(heat_flux['mean'])
flux_norm = np.array(((P/(Q*h_mean))/V))
fig = plt.figure()
plt.title('Fluks BOC')
plt.xlabel('Radial Position [cm]')
plt.ylabel('Axial Height [cm]')
plt.pcolor(r, z, flux*flux_norm, cmap='jet')
plt.colorbar()
plt.savefig('Distribusi Fluks Aksial Radial BOC .jpg',dpi = 1000, bbox_inches = 'tight')
#fig.show()

for i in range (25):
    	sp = openmc.StatePoint('openmc_simulation_n'+str(i)+'.h5')
    	legendre_flux = sp.get_tally(name = 'flux_tally_legendre').get_pandas_dataframe()
    	legendre_flux_mean = legendre_flux['mean']
    	legendre_exponential = openmc.legendre_from_expcoef(legendre_flux_mean, domain=(zmin, zmax))
    	z = np.linspace(zmin,zmax, 100)
    	zernikerad_flux = sp.get_tally(name = 'flux_tally_zernike_radial').get_pandas_dataframe()
    	zernikerad_flux_mean = zernikerad_flux['mean']
    	zernikerad_exponential = openmc.ZernikeRadial(zernikerad_flux_mean, radius=radius)
    	r = np.linspace(-radius, radius, 100)
    	flux_zernikerad_r = zernikerad_exponential(r)
    	flux = np.array([legendre_exponential(z)]).T  @ np.array([zernikerad_exponential(r)])
heat_flux = sp.get_tally(id = 7).get_pandas_dataframe()
h_mean = np.array(heat_flux['mean'])
flux_norm = np.array(((P/(Q*h_mean))/V))
fig = plt.figure()
plt.title('Fluks EOC')
plt.xlabel('Radial Position [cm]')
plt.ylabel('Axial Height [cm]')
plt.pcolor(r, z, flux*flux_norm, cmap='jet')
plt.colorbar()
plt.savefig('Distribusi Fluks Aksial Radial EOC .jpg',dpi = 1000, bbox_inches = 'tight')
#fig.show()

