import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd
import sys
from subprocess import call
import shlex
import os

#Main menu function
def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
    1: Individual Simulation Plots
    2: Initial Tolerance vs Simulations
    3: Process Files
    4: Unprocess Files
    5: Quit/Log Out

    Please enter your choice: """)

    if choice == "1":
        multi(data_process())
    elif choice == "2":
        initial_sim(data_process())
    elif choice == "3":
        print("Processing Files")
        call("./process.sh")
    elif choice=="4":
        print("Unprocessing Files")
        call("./unprocess.sh")
    elif choice=="5":
        sys.exit
    else:
        print("Invalid input")
        print("Please try again")
        menu()

def data_process():

    filepathlist = []
    sims = []
    for subdir, dirs, files in os.walk(r'Processed/'):
        files.sort()
        dirs.sort()
        sims.append(dirs)
        for filename in files:
            filepath = subdir + os.sep + filename
            filepathlist.append(filepath)
    sims = sims[0]

    #1: initial tolerance files
    filenames_1 = ["p_0", "p_1", "Ux_0", "Uy_0", "Uz_0", "k_0", "epsilon_0"]

    #2: final tolerance files
    filenames_2 = ["pFinalRes_0", "pFinalRes_1", "UxFinalRes_0", "UyFinalRes_0", "UzFinalRes_0", "kFinalRes_0", "epsilonFinalRes_0"]

    #3: number of iterations files
    filenames_3 = ["pIters_0", "pIters_1", "UxIters_0", "UyIters_0", "UzIters_0", "kIters_0", "epsilonIters_0"]
    
    #Initialise dictionary for simulation files
    path_dict = {}

    
    for i in sims:
        for j in filepathlist:
            if j.find(i) != -1:
                path_dict.setdefault(i, []).append(j)

    #Return the constructed dataframes
    return path_dict

def multi(path_dict):

    #1: initial tolerance files
    filenames_1 = ["p_0", "p_1", "Ux_0", "Uy_0", "Uz_0", "k_0", "epsilon_0"]

    #2: final tolerance files
    filenames_2 = ["pFinalRes_0", "pFinalRes_1", "UxFinalRes_0", "UyFinalRes_0", "UzFinalRes_0", "kFinalRes_0", "epsilonFinalRes_0"]

    #3: number of iterations files
    filenames_3 = ["pIters_0", "pIters_1", "UxIters_0", "UyIters_0", "UzIters_0", "kIters_0", "epsilonIters_0"]
    
    #Choose the simulation to graph
    sim_choice = input("Enter the simulation to graph, i.e 'Simulation1' : ")

    #Initialise data segments.
    initial_path = []
    final_path = []
    niterations_path = []

    #Split the chosen simulation data into initial tolerance, final, n.o interations.
    for i in path_dict.get(sim_choice):
        for x, y, z in zip(filenames_1, filenames_2, filenames_3):
            if i.find(x) != -1:
                initial_path.append(i)
            elif i.find(y) != -1:
                final_path.append(i)
            elif i.find(z) != -1:
                niterations_path.append(i)

    #read and generate dataframe from txt files:
    initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in initial_path]
    final_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in final_path]
    num_iterations_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in niterations_path]

    # Combine the dataframes
    initial_combined = pd.concat(initial_tolerance_df, ignore_index=False, axis=1)
    final_combined = pd.concat(final_tolerance_df, ignore_index=False, axis=1)
    num_iterations_combined = pd.concat(num_iterations_df, ignore_index=False, axis=1)

    #relative tolerance calculations
    #!!!Change range to fit number of simulations!!!
    relative_combined = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined), len(final_combined)), 7)), columns=filenames_1)
    relative_combined.index = np.arange(1,len(relative_combined)+1)

    for i in range(0, len(initial_tolerance_df)):
        relative_combined.iloc[:, i] = final_combined.iloc[:, i] / initial_combined.iloc[:, i]

    #percentage change tolerance calculations
    #!!!Change range to fit number of simulations!!!
    percentage_combined = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined), len(final_combined)), 7)), columns=filenames_1)
    percentage_combined.index = np.arange(1,len(percentage_combined)+1)

    for i in range(0, len(initial_tolerance_df)):
        percentage_combined.iloc[:, i] = ((initial_combined.iloc[:, i] - final_combined.iloc[:, i]) / initial_combined.iloc[:, i]) * 100

    # define a figure, with subplots as an array "ax" 
    fig, ax = plt.subplots(2,2)

    #Set figure Title
    fig.suptitle(sim_choice)

    #Generate plots:
    ax[0, 0].plot(initial_combined)
    ax[0, 1].plot(relative_combined)
    ax[1, 0].plot(num_iterations_combined)
    ax[1, 1].plot(percentage_combined)

    # plot 1 - (initial) residuals time series

    # (optional) add horizontal lines to plot for idea of residuals relaxations.
    ax[0, 0].axhline(y=1.0e-05, color="black", linestyle='--')
    ax[0, 0].axhline(y=1.0e-04, color="black", linestyle='-')

    # title of plot
    ax[0, 0].set_title("Residual vs. Iteration")
    # x axis label
    ax[0, 0].set_xlabel("Iteration")
    # y axis label
    ax[0, 0].set_ylabel("Residual")
    # log scale on y axis since skewed to small residuals
    ax[0, 0].set_yscale("log")
    # only plot to data range
    #!!! fix label issues with starting x axis!!!
    ax[0, 0].set_xlim(1, len(initial_combined))

    # add legend to the plot
    ax[0, 0].legend(filenames_1)


    # plot 2 - relative tol time series

    # title of plot
    ax[0, 1].set_title("Relative Tolerances vs. Iteration")
    # x axis label
    ax[0, 1].set_xlabel("Iteration")
    # y axis label
    ax[0, 1].set_ylabel("Relative Tolerances")
    # log scale on y axis since skewed to small residuals
    ax[0, 1].set_yscale("log")
    # only plot to data range
    ax[0, 1].set_xlim(1, len(relative_combined))

    # add legend to the plot
    ax[0, 1].legend(filenames_1)


    # plot 3 - number iterations at each timestep time series

    # title of plot
    ax[1, 0].set_title("Number Inner Iterations In SIMPLE Loop vs. Outer Iteration")
    # x axis label
    ax[1, 0].set_xlabel("Outer Iteration")
    # y axis label
    ax[1, 0].set_ylabel("Number Inner Iterations")
    # log scale on y axis since skewed to small residuals
    #ax[1, 0].set_yscale("log")
    # only plot to data range
    ax[1, 0].set_xlim(1, len(num_iterations_combined))


    # add legend to the plot
    ax[1, 0].legend(filenames_1)

    # plot 4 - % change in initial to final tolerance time series.

    # title of plot
    ax[1, 1].set_title("Percentage change")
    # x axis label
    ax[1, 1].set_xlabel("Iteration")
    # y axis label
    ax[1, 1].set_ylabel("Percentage Change")
    # only plot to data range
    ax[1, 1].set_xlim(1, len(percentage_combined))

    # add legend to the plot
    ax[1, 1].legend(filenames_1)


    # force plot to display in full-screen
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())

    # display plot until closed
    plt.show()

def initial_sim(path_dict):

    #DOES THIS NEED TO BE DYNAMIC?

    #1: initial tolerance files
    filenames_1 = ["p_0", "p_1", "Ux_0", "Uy_0", "Uz_0", "k_0", "epsilon_0"]
    sim1 = []
    sim2 = []
    sim3 = []
    sim4 = []
    
    for i in path_dict.get('Simulation1'):
        result = any(elem in i for elem in filenames_1)
        if result:
            sim1.append(i)
    for i in path_dict.get('Simulation2'):
        result = any(elem in i for elem in filenames_1)
        if result:
            sim2.append(i)
    for i in path_dict.get('Simulation3'):
        result = any(elem in i for elem in filenames_1)
        if result:
            sim3.append(i)
    for i in path_dict.get('Simulation4'):
        result = any(elem in i for elem in filenames_1)
        if result:
            sim4.append(i)
    
    
    #read amnd generate dataframe from txt files:
    sim1_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in sim1]
    sim2_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in sim2]
    sim3_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in sim3]
    sim4_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in sim4]

    # Combine the dataframes
    sim1_initial_combined = pd.concat(sim1_initial_tolerance_df, ignore_index=False, axis=1)
    sim2_initial_combined = pd.concat(sim2_initial_tolerance_df, ignore_index=False, axis=1)
    sim3_initial_combined = pd.concat(sim3_initial_tolerance_df, ignore_index=False, axis=1)
    sim4_initial_combined = pd.concat(sim4_initial_tolerance_df, ignore_index=False, axis=1)

    # define a figure, with subplots as an array "ax" 
    fig, ax = plt.subplots(2,2)
    fig.suptitle("Residual vs. Iteration")

    #Generate plots:
    ax[0, 0].plot(sim1_initial_combined)
    ax[0, 1].plot(sim2_initial_combined)
    ax[1, 0].plot(sim3_initial_combined)
    ax[1, 1].plot(sim4_initial_combined)

    # plot 1 - (initial) residuals time series

    # (optional) add horizontal lines to plot for idea of residuals relaxations.
    ax[0, 0].axhline(y=1.0e-05, color="black", linestyle='--')
    ax[0, 0].axhline(y=1.0e-04, color="black", linestyle='-')
    
    # title of plot
    ax[0, 0].set_title("Simulation1")
    # x axis label
    ax[0, 0].set_xlabel("Iteration")
    # y axis label
    ax[0, 0].set_ylabel("Residual")
    # log scale on y axis since skewed to small residuals
    ax[0, 0].set_yscale("log")
    # only plot to data range
    #!!! fix label issues with starting x axis!!!
    ax[0, 0].set_xlim(1, len(sim1_initial_combined))

    # add legend to the plot
    ax[0, 0].legend(filenames_1)

    # plot 2 - (initial) residuals time series

    # (optional) add horizontal lines to plot for idea of residuals relaxations.
    ax[0, 1].axhline(y=1.0e-05, color="black", linestyle='--')
    ax[0, 1].axhline(y=1.0e-04, color="black", linestyle='-')
    
    # title of plot
    ax[0, 1].set_title("Simulation2")
    # x axis label
    ax[0, 1].set_xlabel("Iteration")
    # y axis label
    ax[0, 1].set_ylabel("Residual")
    # log scale on y axis since skewed to small residuals
    ax[0, 1].set_yscale("log")
    # only plot to data range
    #!!! fix label issues with starting x axis!!!
    ax[0, 1].set_xlim(1, len(sim2_initial_combined))

    # add legend to the plot
    ax[0, 1].legend(filenames_1)

    # plot 3 - (initial) residuals time series

    # (optional) add horizontal lines to plot for idea of residuals relaxations.
    ax[1, 0].axhline(y=1.0e-05, color="black", linestyle='--')
    ax[1, 0].axhline(y=1.0e-04, color="black", linestyle='-')
    
    # title of plot
    ax[1, 0].set_title("Simulation3")
    # x axis label
    ax[1, 0].set_xlabel("Iteration")
    # y axis label
    ax[1, 0].set_ylabel("Residual")
    # log scale on y axis since skewed to small residuals
    ax[1, 0].set_yscale("log")
    # only plot to data range
    #!!! fix label issues with starting x axis!!!
    ax[1, 0].set_xlim(1, len(sim3_initial_combined))

    # add legend to the plot
    ax[1, 0].legend(filenames_1)



    # plot 4 - (initial) residuals time series

    # (optional) add horizontal lines to plot for idea of residuals relaxations.
    ax[1, 1].axhline(y=1.0e-05, color="black", linestyle='--')
    ax[1, 1].axhline(y=1.0e-04, color="black", linestyle='-')
    
    # title of plot
    ax[1, 1].set_title("Simulation4")
    # x axis label
    ax[1, 1].set_xlabel("Iteration")
    # y axis label
    ax[1, 1].set_ylabel("Residual")
    # log scale on y axis since skewed to small residuals
    ax[1, 1].set_yscale("log")
    # only plot to data range
    #!!! fix label issues with starting x axis!!!
    ax[1, 1].set_xlim(1, len(sim4_initial_combined))

    # add legend to the plot
    ax[1, 1].legend(filenames_1)



    # force plot to display in full-screen
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())

    # display plot until closed
    plt.show()
    

if __name__ == '__main__':
    menu()