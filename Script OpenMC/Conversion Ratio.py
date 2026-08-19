import numpy as np
import matplotlib.pyplot as plt
import openmc.deplete
import openmc
import pandas as pd
results = openmc.deplete.Results("./depletion_results.h5")

time = []
for i in range (1,25):
	time_variable = 'time'+str(i)
	time.append(time_variable)
ax_fis_1 = []
for i in range(1,25):
	ax_fis_1_variable = 'moxf1_'+str(i)
	ax_fis_1.append(ax_fis_1_variable)
ax_fis_2 = []
for i in range(1,25):
	ax_fis_2_variable = 'moxf2_'+str(i)
	ax_fis_2.append(ax_fis_2_variable)
	
ax_fis_3 = []
for i in range(1,25):
	ax_fis_3_variable = 'moxf3_'+str(i)
	ax_fis_3.append(ax_fis_3_variable)
	
ax_fis_4 = []
for i in range(1,25):
	ax_fis_4_variable = 'moxf4_'+str(i)
	ax_fis_4.append(ax_fis_4_variable)
	
ax_fis_5 = []
for i in range(1,25):
	ax_fis_5_variable = 'moxf5_'+str(i)
	ax_fis_5.append(ax_fis_5_variable)
	
ax_fis_6 = []
for i in range(1,25):
	ax_fis_6_variable = 'moxf6_'+str(i)
	ax_fis_6.append(ax_fis_6_variable)
	
ax_fis_7 = []
for i in range(1,25):
	ax_fis_7_variable = 'moxf7_'+str(i)
	ax_fis_7.append(ax_fis_7_variable)

ax_capture_1 = []
for i in range(1,25):
	ax_capture_1_variable = 'moxc1_'+str(i)
	ax_capture_1.append(ax_capture_1_variable)
	
ax_capture_2 = []
for i in range(1,25):
	ax_capture_2_variable = 'moxc2_'+str(i)
	ax_capture_2.append(ax_capture_2_variable)
	
ax_capture_3 = []
for i in range(1,25):
	ax_capture_3_variable = 'moxc3_'+str(i)
	ax_capture_3.append(ax_capture_3_variable)
	
ax_capture_4 = []
for i in range(1,25):
	ax_capture_4_variable = 'moxc4_'+str(i)
	ax_capture_4.append(ax_capture_4_variable)
	
ax_capture_5 = []
for i in range(1,25):
	ax_capture_5_variable = 'moxc5_'+str(i)
	ax_capture_5.append(ax_capture_5_variable)
	
ax_capture_6 = []
for i in range(1,25):
	ax_capture_6_variable = 'moxc6_'+str(i)
	ax_capture_6.append(ax_capture_6_variable)
	
ax_capture_7 = []
for i in range(1,25):
	ax_capture_7_variable = 'moxc7_'+str(i)
	ax_capture_7.append(ax_capture_7_variable)
material_id = []
for i in range(1,25):
    id = str(i)
    material_id.append(id)
sum_ax_fis_1 = 0
sum_ax_fis_2 = 0
sum_ax_fis_3 = 0
sum_ax_fis_4 = 0
sum_ax_fis_5 = 0
sum_ax_fis_6 = 0
sum_ax_fis_7 = 0

sum_ax_capture_1 = 0
sum_ax_capture_2 = 0
sum_ax_capture_3 = 0
sum_ax_capture_4 = 0
sum_ax_capture_5 = 0
sum_ax_capture_6 = 0
sum_ax_capture_7 = 0
	
for i,j in zip(range(24),range(1,25)):
	time[i],ax_fis_1[i] = results.get_reaction_rate('2', 'U233', 'fission')
	time[i],ax_fis_2[i] = results.get_reaction_rate('2', 'U235', 'fission')
	time[i],ax_fis_3[i] = results.get_reaction_rate('2', 'U238', 'fission')
	time[i],ax_fis_4[i] = results.get_reaction_rate('2', 'Pu239', 'fission')
	time[i],ax_fis_5[i] = results.get_reaction_rate('2', 'Pu240', 'fission')
	time[i],ax_fis_6[i] = results.get_reaction_rate('2', 'Pu241', 'fission')
	time[i],ax_fis_7[i] = results.get_reaction_rate('2', 'Th232', 'fission')
	
	time[i],ax_capture_1[i] = results.get_reaction_rate('2', 'U233', '(n,gamma)')
	time[i],ax_capture_2[i] = results.get_reaction_rate('2', 'U235', '(n,gamma)')
	time[i],ax_capture_3[i] = results.get_reaction_rate('2', 'U238', '(n,gamma)')
	time[i],ax_capture_4[i] = results.get_reaction_rate('2', 'Pu239', '(n,gamma)')
	time[i],ax_capture_5[i] = results.get_reaction_rate('2', 'Pu240', '(n,gamma)')
	time[i],ax_capture_6[i] = results.get_reaction_rate('2', 'Pu241', '(n,gamma)')
	time[i],ax_capture_7[i] = results.get_reaction_rate('2', 'Th232', '(n,gamma)')
	
	sum_fis1 = sum_ax_fis_1 + ax_fis_1[i]
	sum_fis2 = sum_ax_fis_2 + ax_fis_2[i]
	sum_fis3 = sum_ax_fis_3 + ax_fis_3[i]
	sum_fis4 = sum_ax_fis_4 + ax_fis_4[i]
	sum_fis5 = sum_ax_fis_5 + ax_fis_5[i]
	sum_fis6 = sum_ax_fis_6 + ax_fis_6[i]
	sum_fis7 = sum_ax_fis_7 + ax_fis_7[i]
	
	sum_capture1 = sum_ax_capture_1 + ax_capture_1[i]
	sum_capture2 = sum_ax_capture_2 + ax_capture_2[i]
	sum_capture3 = sum_ax_capture_3 + ax_capture_3[i]
	sum_capture4 = sum_ax_capture_4 + ax_capture_4[i]
	sum_capture5 = sum_ax_capture_5 + ax_capture_5[i]
	sum_capture6 = sum_ax_capture_6 + ax_capture_6[i]
	sum_capture7 = sum_ax_capture_7 + ax_capture_7[i]
	
## capture
U233_capture = sum_capture1
U235_capture = sum_capture2
U238_capture = sum_capture3
Pu239_capture = sum_capture4
Pu240_capture = sum_capture5
Pu241_capture = sum_capture6
Th232_capture = sum_capture7

## absorption
U233_absorption = U233_capture + sum_fis1
U235_absorption = U235_capture + sum_fis2
U238_absorption = U238_capture + sum_fis3
Pu239_absorption = Pu239_capture + sum_fis4
Pu240_absorption = Pu240_capture + sum_fis5
Pu241_absorption = Pu241_capture + sum_fis6
Th232_absorption = Th232_capture + sum_fis7

CR = (	U238_capture + Pu240_capture + Th232_capture ) / ( U233_absorption + U235_absorption  + Pu239_absorption  + Pu241_absorption)


data_CR = pd.DataFrame(list(map(np.ravel, CR)))
data_CR.to_excel('Data CR 10% crd .xlsx')
