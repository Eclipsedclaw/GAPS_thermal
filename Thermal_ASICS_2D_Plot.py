"""
Display tracker temperature by layers
Aur: Jiancheng Zeng
Date: Jan 17, 2024
"""

import os
from pybfsw.gse.gsequery import GSEQuery  
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import time

def get_data_from_table(table_name, ti, tf):
    # Fetch the database path from the environment variable
    path = os.environ.get("GSE_DB_PATH")

    if not path:
        print("Error: GSE_DB_PATH environment variable is not set.")
        return

    # Create a GSEQuery object
    q = GSEQuery(project="gaps", path=path)

    try:
        # Get the data from the specified table
        table_data = q.time_query3(table_name, ti = ti, tf = tf)  

        # Print the data
        #print(f"Data from table '{table_name}':")
        # print(datetime.utcfromtimestamp(table_data[0][0]))
        #print(table_data[0])

        return table_data

    except Exception as e:
        print(f"Error: {e}")

def Tracker_T_vector_layer():
    Real_Time = np.empty(shape=(0,))

    '''
    Even layer = [[05, 04, 03, 02, 01, 00], [15, 14, 13, 12, 11, 10], [25, 24, 23, 22, 21, 20], [35, 34, 33, 32, 31, 30], [45, 44, 43, 42, 41, 40], [55, 54, 53, 52, 51, 50]]
    Odd layer = [[05, 15, 25, 35, 45, 55], [04, 14, 24, 34, 44, 54], [03, 13, 23, 33, 43, 53], [02, 12, 22, 32, 42, 52], [01, 11, 21, 31, 41, 51], [00, 10, 20, 30, 40, 50]]
    '''

    T_0 = np.array([[float(get_data_from_table('@asictemp_l0r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r0m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l0r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r1m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l0r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r2m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l0r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r3m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l0r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r4m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l0r5m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r5m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r5m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r5m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r5m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l0r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l0r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_0 temperature: \n" + str(T_0))

    T_1 = np.array([[float(get_data_from_table('@asictemp_l1r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r5m5', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l1r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r5m4', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l1r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r5m3', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l1r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r5m2', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l1r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r5m1', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l1r0m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r1m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r2m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r3m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r4m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l1r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l1r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_1 temperature: \n" + str(T_1))

    T_2 = np.array([[float(get_data_from_table('@asictemp_l2r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r0m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l2r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r1m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l2r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r2m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l2r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r3m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l2r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r4m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l2r5m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r5m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r5m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r5m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r5m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l2r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l2r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_2 temperature: \n" + str(T_2))

    T_3 = np.array([[float(get_data_from_table('@asictemp_l3r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r5m5', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l3r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r5m4', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l3r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r5m3', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l3r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r5m2', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l3r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r5m1', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l3r0m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r1m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r2m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r3m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r4m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l3r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l3r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_3 temperature: \n" + str(T_3))

    T_4 = np.array([[float(get_data_from_table('@asictemp_l4r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r0m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l4r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r1m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l4r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r2m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l4r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r3m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l4r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r4m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l4r5m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r5m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r5m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r5m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r5m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l4r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l4r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_4 temperature: \n" + str(T_4))

    T_5 = np.array([[float(get_data_from_table('@asictemp_l5r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r5m5', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l5r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r5m4', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l5r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r5m3', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l5r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r5m2', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l5r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r5m1', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l5r0m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r1m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r2m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r3m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r4m0', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l5r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l5r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_5 temperature: \n" + str(T_5))

    T_6 = np.array([[float(get_data_from_table('@asictemp_l6r0m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r0m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r0m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r0m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r0m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r0m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l6r1m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r1m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r1m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r1m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r1m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r1m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l6r2m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r2m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r2m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r2m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r2m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r2m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l6r3m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r3m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r3m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r3m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r3m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r3m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l6r4m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r4m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r4m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r4m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r4m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r4m0', ti, tf)[1][0])], [float(get_data_from_table('@asictemp_l6r5m5', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r5m4', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r5m3', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r5m2', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r5m1', ti, tf)[1][0]), float(get_data_from_table('@asictemp_l6r5m0', ti, tf)[1][0])]])
    Real_Time = np.append(Real_Time, get_data_from_table('@asictemp_l6r0m5', ti, tf)[0][0] - 5 * 3600)
    print("Layer_6 temperature: \n" + str(T_6))

    return T_0, T_1, T_2, T_3, T_4, T_5, T_6, Real_Time

def Plot_2d(T_0, T_1, T_2, T_3, T_4, T_5, T_6, Real_Time, save_path='./tracker_temperature.png'):
    print("Making plot...")

    # Convert Unix timestamps to datetime objects and format as strings
    formatted_time = [datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f") for timestamp in Real_Time]

    fig, axs = plt.subplots(4, 2, figsize=(15,30))
    fig.suptitle('Temperature profile')

    lower_limit = -50
    upper_limit = 30

    # Create a custom colormap with black for out-of-range values
    cmap = plt.cm.get_cmap('winter')
    custom_cmap = cmap.copy()
    custom_cmap.set_bad(color='black')

    # Set out-of-range values to np.nan
    T_0[np.logical_or(T_0 < lower_limit, T_0 > upper_limit)] = np.nan
    img_0 = axs[0, 0].imshow(T_0, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_0, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[0, 0].set_title('Layer-0 at '+ str(formatted_time[0]) + ' \n Radiator Side')
    axs[0 ,0].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_0[ np.logical_and(T_0 >= -50, T_0 <= 30)])) + 'C')

    # Set out-of-range values to np.nan
    T_1[np.logical_or(T_1 < lower_limit, T_1 > upper_limit)] = np.nan
    img_1 = axs[0, 1].imshow(T_1, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_1, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[0, 1].set_title('Layer-1 at '+ str(formatted_time[1]) + ' \n Radiator Side')
    axs[0 ,1].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_1[ np.logical_and(T_1 >= -50, T_1 <= 30)])) + 'C')

    # Set out-of-range values to np.nan
    T_2[np.logical_or(T_2 < lower_limit, T_2 > upper_limit)] = np.nan
    img_2 = axs[1, 0].imshow(T_2, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_2, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[1, 0].set_title('Layer-2 at '+ str(formatted_time[2]) + ' \n Radiator Side')
    axs[1 ,0].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_2[ np.logical_and(T_2 >= -50, T_2 <= 30)])) + 'C')

    # Set out-of-range values to np.nan
    T_3[np.logical_or(T_3 < lower_limit, T_3 > upper_limit)] = np.nan
    img_3 = axs[1, 1].imshow(T_3, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_3, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[1, 1].set_title('Layer-3 at '+ str(formatted_time[3]) + ' \n Radiator Side')
    axs[1 ,1].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_3[ np.logical_and(T_3 >= -50, T_3 <= 30)])) + 'C')

    # Set out-of-range values to np.nan
    T_4[np.logical_or(T_4 < lower_limit, T_4 > upper_limit)] = np.nan
    img_4 = axs[2, 0].imshow(T_4, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_4, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[2, 0].set_title('Layer-4 at '+ str(formatted_time[4]) + ' \n Radiator Side')
    axs[2 ,0].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_4[ np.logical_and(T_4 >= -50, T_4 <= 30)])) + 'C')

    # Set out-of-range values to np.nan
    T_5[np.logical_or(T_5 < lower_limit, T_5 > upper_limit)] = np.nan
    img_5 = axs[2, 1].imshow(T_5, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_5, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[2, 1].set_title('Layer-5 at '+ str(formatted_time[5]) + ' \n Radiator Side')
    axs[2 ,1].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_5[ np.logical_and(T_5 >= -50, T_5 <= 30)])) + 'C')

    # Set out-of-range values to np.nan
    T_6[np.logical_or(T_6 < lower_limit, T_6 > upper_limit)] = np.nan
    img_6 = axs[3, 0].imshow(T_6, cmap = custom_cmap, vmin = -40, vmax = -30)
    plt.colorbar(img_6, orientation='vertical', label='\N{DEGREE SIGN}C')
    axs[3, 0].set_title('Layer-6 at '+ str(formatted_time[6]) + ' \n Radiator Side')
    axs[3 ,0].set_xlabel('SUN Side \n average temperature: ' + str(np.average(T_6[ np.logical_and(T_6 >= -50, T_6 <= 30)])) + 'C')

    axs[3, 1].axis('off')

    for (j,i),label in np.ndenumerate(T_0):
        if(-50 < round(T_0[j, i],1) < 100):
            axs[0, 0].text(i,j,round(T_0[j, i],1), c='k', ha='center',va='center')
        if(-50 < round(T_1[j, i],1) < 100):
            axs[0, 1].text(i,j,round(T_1[j, i],1), c='k', ha='center',va='center')
        if(-50 < round(T_2[j, i],1) < 100):
            axs[1, 0].text(i,j,round(T_2[j, i],1), c='k', ha='center',va='center')
        if(-50 < round(T_3[j, i],1) < 100):
            axs[1, 1].text(i,j,round(T_3[j, i],1), c='k', ha='center',va='center')
        if(-50 < round(T_4[j, i],1) < 100):
            axs[2, 0].text(i,j,round(T_4[j, i],1), c='k', ha='center',va='center')
        if(-50 < round(T_5[j, i],1) < 100):
            axs[2, 1].text(i,j,round(T_5[j, i],1), c='k', ha='center',va='center')
        if(-50 < round(T_6[j, i],1) < 100):
            axs[3, 0].text(i,j,round(T_6[j, i],1), c='k', ha='center',va='center')
    

    save_path = f"./2D_{formatted_time[0]}.png"
    # Replace whitespaces and backslashes with underscores
    save_path = save_path.replace(' ', '_').replace(':', '')

    #plt.savefig('./tracker_temperature1.png')
    plt.savefig(save_path)
    plt.show()

if __name__ == "__main__": 
    # Prompt the user to enter a datetime value
    user_input = input("Please enter a datetime value in the format 'YYYY-MM-DD HH:mm:ss.SSS'(Eastern time): ")

    try:
        # Parse the user input to a datetime object
        ti_timestamp = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S.%f")
        print(f"You entered: {ti_timestamp} ET")
    except ValueError:
        print("Invalid datetime format. Please enter the value in the format 'YYYY-MM-DD HH:mm:ss.SSS'")

    ti = ti_timestamp.timestamp()
    tf = int(time.time())

    T_0, T_1, T_2, T_3, T_4, T_5, T_6, Real_Time = Tracker_T_vector_layer()

    Plot_2d(T_0=T_0, T_1=T_1, T_2=T_2, T_3=T_3, T_4=T_4, T_5=T_5, T_6=T_6, Real_Time=Real_Time)
