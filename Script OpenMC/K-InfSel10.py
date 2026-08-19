import openmc
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot
import openmc.deplete
import pandas as pd
import numpy as np

results = openmc.deplete.ResultsList.from_hdf5("./depletion_results.h5")

time,k = results.get_keff()
data_k = pd.DataFrame(list(map(np.ravel,k)))
data_k.to_excel('Hasil Kinf 10%.xlsx')
"""
fig = plt.figure()
plt.errorbar(time, k[:,0], yerr = k[:,1])
plt.xlabel('time(years)')
plt.ylabel("$k_{inf}\pm\sigma$")
plt.show()
fig.savefig('Kinf vs burnup time.jpg', dpi=1000)
"""
