import os
from pybfsw.gse.gsequery import GSEQuery  
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
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

def Tracker_T_vector():
    table_names = []

    T_tracker = np.empty(shape=(0,))
    T_average = np.empty(shape=(0,))
    x = []
    y = []
    z = []
    Real_Time = []
    for l in range(7):  # Assuming the range is from l=0 to l=6
        T_L = np.empty(shape=(0,))
        for r in range(6):  # Assuming the range is from r=0 to r=5
            T_R = np.empty(shape=(0,))
            for m in range(6):  # Assuming the range is from m=0 to m=5
                module_name = f"@asictemp_l{l}r{r}m{m}"
                table_names.append(module_name)
                print(module_name, end='\r', flush=True)
                Read_Out = get_data_from_table(module_name, ti, tf)
                if(Read_Out == None):
                    T_R = np.append(T_R, None)
                elif(float(Read_Out[1][0]) > -50 and float(Read_Out[1][0] < 30)):
                    T_R = np.append(T_R, Read_Out[1][0])
                    x.append(r)
                    y.append(m)
                    z.append(9-l)
            T_L = np.append(T_L, T_R)
        if(T_L != []):
            T_average = np.append(T_average, np.average(T_L))
        else:
            T_average = np.append(T_average, None)
        Real_Time = Read_Out[0][0]
        T_tracker = np.concatenate((T_tracker, T_L.reshape(-1)), axis=0)
    print(T_average)
    print(T_tracker)
    return T_tracker, T_average, Real_Time, x, y, z

def Plot_3d(tracker_temp, T_average, Real_Time, x, y, z, save_path='./tracker_temperature.png'):
    print("Making plot...")

    fig = plt.figure(figsize=(8, 10))
    ax = fig.add_subplot(111, projection='3d')

    colmap = cm.ScalarMappable(cmap=cm.winter)
    colmap.set_array([-40, -15])

    # reference for cmap. note cmap and c are different!
    # http://matplotlib.org/examples/color/colormaps_reference.html
    ax.scatter(x, y, z, marker='s',s = 200, alpha = 0.9, c=T_TRACKER, cmap='winter', vmin = -40, vmax = -15)
    cb = fig.colorbar(colmap, cax=fig.add_axes([0.05, 0.1, 0.03, 0.8]), label='\N{DEGREE SIGN}C')

    # Convert Unix timestamp to datetime object
    dt_object = datetime.utcfromtimestamp(Real_Time)

    # Format the datetime object as a string
    formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S.%f")

    ax.set_zlim(0, 10)
    ax.set_xlabel('BOM side')
    ax.set_ylabel('Sun panel side')
    ax.set_zlabel('vertical direction')
    ax.set_title('tracker temperature at ' + str(formatted_time))

    # Iterate over the indices of T_average
    for i, temperature in enumerate(T_average):
        if temperature is not None:
            # If the value is not None, plot the temperature
            plt.text(0.5, -0.1 - i * 0.03, f'Layer{i} average temperature {temperature:.2f}\N{DEGREE SIGN}C\n', ha='center', va='center', transform=ax.transAxes)
        else:
            # If the value is None, display a message indicating missing data
            plt.text(0.5, -0.1 - i * 0.03, f'Layer{i} data not available\n', ha='center', va='center', transform=ax.transAxes)

    ax.set_zticks([])
    save_path = f"./ASIC_T_{formatted_time}.png"
    #plt.savefig('./tracker_temperature1.png')
    plt.savefig(save_path)
    #Plot_3d(T_tracker)
    # change view angle 
    # http://infamousheelfilcher.blogspot.com/2013/02/changing-viewing-angle-of-matplotlib.html
    #ax.view_init(azim = 0,elev = 0)

if __name__ == "__main__": 
    # Prompt the user to enter a datetime value
    user_input = input("Please enter a datetime value in the format 'YYYY-MM-DD HH:mm:ss.SSS': ")

    try:
        # Parse the user input to a datetime object
        ti_timestamp = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S.%f")
        print(f"You entered: {ti_timestamp}")
    except ValueError:
        print("Invalid datetime format. Please enter the value in the format 'YYYY-MM-DD HH:mm:ss.SSS'")

    ti = ti_timestamp.timestamp()
    tf = int(time.time())

    T_TRACKER, T_AVERAGE, REAL_TIME, x, y, z = Tracker_T_vector()

    Plot_3d(T_TRACKER, T_average=T_AVERAGE, Real_Time=REAL_TIME, x = x, y = y, z = z)