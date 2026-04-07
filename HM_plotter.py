#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:29:10 2026

@author: hossein
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import re
import subprocess
import os
import time as timetime
from scipy.optimize import newton
import copy
from scipy.optimize import fsolve
from matplotlib.lines import Line2D


bw_list_hm = np.loadtxt("bw_list_hm.csv", delimiter=' ')
tau_w_list_hm = np.loadtxt("tau_w_list_hm.csv", delimiter=' ')

cost_0d_w_array = np.zeros(( len(bw_list_hm) , len(tau_w_list_hm)  ))
cost_1d_w_array = np.zeros(( len(bw_list_hm) , len(tau_w_list_hm)  ))
cost_2d_w_array = np.zeros(( len(bw_list_hm) , len(tau_w_list_hm)  ))

cost_0d_c_array = np.zeros(( len(bw_list_hm) , len(tau_w_list_hm)  ))
cost_1d_c_array = np.zeros(( len(bw_list_hm) , len(tau_w_list_hm)  ))
cost_2d_c_array = np.zeros(( len(bw_list_hm) , len(tau_w_list_hm)  ))

for i in range(len(bw_list_hm)):
    for j in range(len(tau_w_list_hm)):
        folder_name = 'b'+str(i)+'_t'+str(j)
        
        cost_mat_load = np.loadtxt(folder_name+"/cost_mat_final.txt", delimiter=',')
        
        cost_0d_w_array[i,j] = cost_mat_load[0,0]
        cost_1d_w_array[i,j] = cost_mat_load[0,1] 
        cost_2d_w_array[i,j] = cost_mat_load[0,2] 

        cost_0d_c_array[i,j] =  cost_mat_load[1,0]
        cost_1d_c_array[i,j] =  cost_mat_load[1,1]
        cost_2d_c_array[i,j] =  cost_mat_load[1,2]

cost_0d_w_plot = cost_0d_w_array.transpose()
cost_1d_w_plot = cost_1d_w_array.transpose()
cost_2d_w_plot = cost_2d_w_array

cost_0d_c_plot = cost_0d_c_array
cost_1d_c_plot = cost_1d_c_array
cost_2d_c_plot = cost_2d_c_array


b, t = np.meshgrid(bw_list_hm, tau_w_list_hm)

# plot cost_0d_w
contour_levels_cost = np.linspace(np.nanmin(cost_0d_w_plot), 1.05*np.nanmin(cost_0d_w_plot), 2)
plt.figure()
plt.pcolormesh(b, t, np.log10(cost_0d_w_plot) , shading='auto', cmap='viridis')
plt.xlabel(r'$b_W$', fontsize=15)
plt.ylabel(r'$\tau_W$', fontsize=15)
plt.colorbar(label="log10(cost_0d_w)")
plt.xscale("log")
plt.yscale("log")
# contours = plt.contour(V, S, np.log10(cost), levels=contour_levels_cost, colors='w', linewidths=1)
contours = plt.contour(b, t, cost_0d_w_plot, levels=contour_levels_cost, colors='w', linewidths=2, label=['min'])
plt.savefig("cost_0d_w.PNG", dpi = 400)
# plot cost_0d_w


# plot cost_1d_w
contour_levels_cost = np.linspace(np.nanmin(cost_1d_w_plot), 1.05*np.nanmin(cost_1d_w_plot), 2)
plt.figure()
plt.pcolormesh(b, t, np.log10(cost_1d_w_plot) , shading='auto', cmap='viridis')
plt.xlabel(r'$b_W$', fontsize=15)
plt.ylabel(r'$\tau_W$', fontsize=15)
plt.colorbar(label="log10(cost_1d_w)")
plt.xscale("log")
plt.yscale("log")
# contours = plt.contour(V, S, np.log10(cost), levels=contour_levels_cost, colors='w', linewidths=1)
contours = plt.contour(b, t, cost_1d_w_plot, levels=contour_levels_cost, colors='w', linewidths=2, label=['min'])
plt.savefig("cost_1d_w.PNG", dpi = 400)
# plot cost_1d_w
