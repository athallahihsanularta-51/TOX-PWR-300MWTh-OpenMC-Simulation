import numpy as np
import matplotlib.pyplot as plt
import openmc.deplete
import openmc
import pandas as pd

results = openmc.deplete.ResultsList.from_hdf5("./depletion_results.h5")
time,k = results.get_keff()

############# U233 ###########################
data_u233 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'U233 RING-'+str(i)
    _time, u233 = results.get_atoms( str(i),"U233","atom/b-cm")
    data_u233.append(u233)
    ax.plot(time,u233,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - U233 (atoms / barn-cm)")

ax.legend(loc= 'upper left', fontsize ='medium')
plt.show()
fig.savefig('U233.jpg',dpi = 1000)

data_U233 = pd.DataFrame(list(map(np.ravel, data_u233)) )
data_U233.to_excel('Data U233.xlsx')

### U235 / Tahun
data_u235 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'U235 RING-'+str(i)
    _time, u235 = results.get_atoms( str(i),"U235","atom/b-cm")
    data_u235.append(u235)
    ax.plot(time,u235,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - U235 (atoms / barn-cm)") #1 barn=10^-24 cm
ax.legend(loc= 'upper right', fontsize ='medium')
plt.show()
fig.savefig('U235.jpg',dpi = 1000)

data_U235 = pd.DataFrame(list(map(np.ravel, data_u235)) )
data_U235.to_excel('Data U235.xlsx')

### U238 / Tahun
data_u238 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'U238 RING-'+str(i)
    _time, u238 = results.get_atoms( str(i),"U238","atom/b-cm")
    data_u238.append(u238)
    ax.plot(time,u238,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - U238 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('U238.jpg',dpi = 1000)

data_U238 = pd.DataFrame(list(map(np.ravel, data_u238)) )
data_U238.to_excel('Data U238.xlsx')


### Pu239 / Tahun
data_pu239 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Pu239 RING-'+str(i)
    _time, pu239 = results.get_atoms( str(i),"Pu239","atom/b-cm")
    data_pu239.append(pu239)
    ax.plot(time,pu239,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Pu239 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Pu239.jpg',dpi = 1000)

data_Pu239 = pd.DataFrame(list(map(np.ravel, data_pu239)) )
data_Pu239.to_excel('Data Pu239.xlsx')


### Pu240 / Tahun
data_pu240 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Pu240 RING-'+str(i)
    _time, pu240 = results.get_atoms( str(i),"Pu240","atom/b-cm")
    data_pu240.append(pu240)
    ax.plot(time,pu240,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Pu240 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Pu240.jpg',dpi = 1000)

data_Pu240 = pd.DataFrame(list(map(np.ravel, data_pu240)) )
data_Pu240.to_excel('Data Pu240.xlsx')


### Pu241 / Tahun
data_pu241 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Pu241 RING-'+str(i)
    _time, pu241 = results.get_atoms( str(i),"Pu241","atom/b-cm")
    data_pu241.append(pu241)
    ax.plot(time,pu241,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Pu241 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Pu241.jpg',dpi = 1000)

data_Pu241 = pd.DataFrame(list(map(np.ravel, data_pu241)) )
data_Pu241.to_excel('Data Pu241.xlsx')

### Th232 / Tahun
data_th232 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Th232 RING-'+str(i)
    _time, th232 = results.get_atoms( str(i),"Th232","atom/b-cm")
    data_th232.append(th232)
    ax.plot(time,th232,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Th232 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Th232.jpg',dpi = 1000)

data_Th232 = pd.DataFrame(list(map(np.ravel, data_th232)) )
data_Th232.to_excel('Data Th232.xlsx')

### Th233 / Tahun
data_th233 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Th233 RING-'+str(i)
    _time, th233 = results.get_atoms( str(i),"Th233","atom/b-cm")
    data_th233.append(th233)
    ax.plot(time,th233,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Th233 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Th233.jpg',dpi = 1000)

data_Th233 = pd.DataFrame(list(map(np.ravel, data_th233)) )
data_Th233.to_excel('Data Th233.xlsx')

### Np239 / Tahun
data_np239 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Np239 RING-'+str(i)
    _time, np239 = results.get_atoms( str(i),"Np239","atom/b-cm")
    data_np239.append(np239)
    ax.plot(time,np239,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Np239 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Np239.jpg',dpi = 1000)

data_Np239 = pd.DataFrame(list(map(np.ravel, data_np239)) )
data_Np239.to_excel('Data Np239.xlsx')

### Sr94 / Tahun
data_Sr94 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Sr94 RING-'+str(i)
    _time, Sr94 = results.get_atoms( str(i),"Sr94","atom/b-cm")
    data_Sr94.append(Sr94)
    ax.plot(time,Sr94,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Sr94 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Sr94.jpg',dpi = 1000)

data_Sr94 = pd.DataFrame(list(map(np.ravel, data_Sr94)) )
data_Sr94.to_excel('Data Sr94.xlsx')

### Xe140 / Tahun
data_Xe140 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Xe140 RING-'+str(i)
    _time, Xe140 = results.get_atoms( str(i),"Xe140","atom/b-cm")
    data_Xe140.append(Xe140)
    ax.plot(time,Xe140,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Xe140 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Xe140.jpg',dpi = 1000)

data_Xe140 = pd.DataFrame(list(map(np.ravel, data_Xe140)) )
data_Xe140.to_excel('Data Xe140.xlsx')

### Ba141 / Tahun
data_Ba141 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Ba141 RING-'+str(i)
    _time, Ba141 = results.get_atoms( str(i),"Ba141","atom/b-cm")
    data_Ba141.append(Ba141)
    ax.plot(time,Ba141,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Ba141 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Ba141.jpg',dpi = 1000)

data_Ba141 = pd.DataFrame(list(map(np.ravel, data_Ba141)) )
data_Ba141.to_excel('Data Ba141.xlsx')

### Kr91 / Tahun
data_Kr91 =[]
id = [2]
fig,ax = plt.subplots()
for i in id :
    label = 'Kr91 RING-'+str(i)
    _time, Kr91 = results.get_atoms( str(i),"Kr91","atom/b-cm")
    data_Kr91.append(Kr91)
    ax.plot(time,Kr91,label =label)
    ax.set_xlabel('step')
    ax.set_ylabel("Number of atoms - Kr91 (atoms / barn-cm)")
ax.legend(loc= 'upper right', fontsize ='medium')
#plt.show()
fig.savefig('Kr91.jpg',dpi = 1000)

data_Kr91 = pd.DataFrame(list(map(np.ravel, data_Kr91)) )
data_Kr91.to_excel('Data Kr91.xlsx')

