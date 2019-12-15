import glob
import os
import numpy as np
import numba
import geopandas as gpd
import pandas as pd


@numba.jit
def np_within_circle(pt_x, pt_y, pt_center_x, pt_center_y, radius):
    if (pt_x - pt_center_x) ** 2 + (pt_y - pt_center_y) ** 2 < radius ** 2:
        return 1
    else:
        return 0

@numba.jit
def np_find_pts(np_df):
    tmp_one_pt = []
    for i in np_df:
        pt_center_x = i[0]
        pt_center_y = i[1]

        tmp = []
        for j in np_df:
            pt_x = j[0]
            pt_y = j[1]
            tmp.append(np_within_circle(pt_x, pt_y, pt_center_x, pt_center_y, 25))
        
        if sum(tmp) >5:
            tmp_one_pt.append(1)
        else:
            tmp_one_pt.append(0)

    return tmp_one_pt

@numba.jit
def np_make_stoppt(stop_pt, np_df):
    se_pt = []
    for i, r_np_pt in enumerate(np_df):
        print(i)
        if i == len(stop_pt) - 2:
            duration = i - start_time + 1
            tmp = [start_time, duration, r_np_pt[0], r_np_pt[1]]
            se_pt.append(tmp)
            break
        elif i == 0 or stop_pt[i] - stop_pt[i+1] < 0:
            start_time = i

        elif stop_pt[i] - stop_pt[i+1] > 0:
            duration = i - start_time + 1
            tmp = [start_time, duration, r_np_pt[0], r_np_pt[1]]
            se_pt.append(tmp)

    return se_pt

files = glob.glob("D:pflow/through-pt-2449/*.csv")
print(files)
all_sample = []
for i, filename in enumerate(files):
    np_gdf = np.loadtxt(filename, delimiter=",", usecols=[6, 7], skiprows=1)
    stop_np_df = np_find_pts(np_gdf)
    try:
        flatten_se_pt = np_make_stoppt(stop_np_df, np_gdf)

        if len(flatten_se_pt) > 2:
            flatten_se_pt.pop(0)
            flatten_se_pt.pop(-1)
            path = "D:pflow/stop-pt/" + filename[-12:-4]  +".csv"
            print(filename)
            np.savetxt(path, flatten_se_pt, delimiter=',')
        else:
            pass
    except IndexError:
        print(i, "ERROR")
        pass




