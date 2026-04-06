#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:23:46 2026

@author: hossein
"""




import numpy as np
import sys
import os
import subprocess
import time
import shutil
import json


def init_numbers_maker():
    
    try:
        n_init_samples = np.loadtxt('n_init_samples.csv', dtype=int, delimiter=',')
        n_org = np.shape(n_init_samples)[0]
    except:
        n_org = int(np.loadtxt("n_org.csv", delimiter=' '))
        mixed_sample_bank = np.loadtxt("mixed_sample_bank.csv", delimiter=',', dtype=int)
        size = np.shape(mixed_sample_bank)[0]
        sample_indices_mix = np.random.randint(0,size,n_org)
        np.savetxt('sample_indices_mix.csv', X=sample_indices_mix, delimiter=',', fmt='%d')
        
        n_init_samples = np.zeros((n_org,2), dtype=int)
        for org_c in range(n_org):
            n_init_samples[org_c,0] = mixed_sample_bank[sample_indices_mix[org_c],0]
            n_init_samples[org_c,1] = mixed_sample_bank[sample_indices_mix[org_c],1]
        
        np.savetxt('n_init_samples.csv', X=n_init_samples, fmt='%d', delimiter=',')
    
    return n_init_samples

# bc = 1.48
# lc = 33.0
# lw = 10.0

bc = float(np.loadtxt("bc.csv"))
lc = float(np.loadtxt("lc.csv"))
lw = float(np.loadtxt("lw.csv"))

bw_middle = -1
tau_w_middle = -1
fitted_bw_vals = np.loadtxt("b_w_tot_avg.csv", delimiter=' ')
fitted_tau_w_vals = np.loadtxt("tau_w_data_avg.csv", delimiter=',')[1:,1:]
fitted_tau_w_vals = np.mean(fitted_tau_w_vals, axis=1)
lw_vals = np.loadtxt("lw_list.csv", delimiter=' ')
for i in range(len(lw_vals)):
    if lw == lw_vals[i]:
        bw_middle = fitted_bw_vals[i]
        tau_w_middle = fitted_tau_w_vals[i]
if bw_middle<0:
    print("Error! bw_middle not found!")
    sys.exit()

bw_list_hm = np.array(list(2**np.linspace(-1,0,10)) + list(2**np.linspace(0,1,10))[1:])*bw_middle
tau_w_list_hm = np.array(list(2**np.linspace(-1,0,10)) + list(2**np.linspace(0,1,10))[1:])*tau_w_middle

# np.savetxt("bc.csv", [bc], fmt='%.5f')
# np.savetxt("lc.csv", [lc], fmt='%.5f')
# np.savetxt("lw.csv", [lw], fmt='%.5f')
np.savetxt("bw_list_hm.csv", bw_list_hm, fmt='%.7f')
np.savetxt("tau_w_list_hm.csv", tau_w_list_hm, fmt='%.7f')

# making folders and copying files
folders_names = []
for i in range(len(bw_list_hm)):
    for j in range(len(tau_w_list_hm)):
        folder_name = 'b'+str(i)+'_t'+str(j)
        folders_names.append(folder_name)
        os.makedirs(folder_name, exist_ok=True)

with open("folder_names.txt", "w") as f:
    for folder in folders_names:
        f.write(folder + "\n")
    f.close()
    
subprocess.run(["./copier.sh"])
time.sleep(5)
# making folders and copying files

# making sample numbers, copying, and params modification
n_init_samples = init_numbers_maker()
n_org = np.shape(n_init_samples)[0]
for i in range(len(bw_list_hm)):
    bw = bw_list_hm[i]
    for j in range(len(tau_w_list_hm)):
        tau_w = tau_w_list_hm[j]
        folder_name = 'b'+str(i)+'_t'+str(j)
        shutil.copy("n_init_samples.csv", folder_name+"/")
        
        filepath = folder_name+"/params.txt"
        # Open + load
        with open(filepath, "r") as f:
            data = json.load(f)
        data["l_w_0"] = lw   # <-- your new value
        data["l_c_0"] = lc   # <-- your new value
        data["b_w"] = bw     # <-- your new value
        data["b_c"] = bc     # <-- your new value
        data["tau_w"] = tau_w     # <-- your new value
        # Save changes
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
# making sample numbers, copying, and params modification









