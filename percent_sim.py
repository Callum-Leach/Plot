import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd


#1: Simulation1 initial tolerance
filenames_1 = ["Processed/Simulation1/logs/p_0"]

#2: Simulation2 initial tolerance
filenames_2 = ["Processed/Simulation2/logs/p_0"]

#3: Simulation3 initial tolerance
filenames_3 = ["Processed/Simulation3/logs/p_0"]

#4: Simulation4 initial tolerance
filenames_4 = ["Processed/Simulation4/logs/p_0"]

#5: Simulation5 initial tolerance
filenames_4 = ["Processed/Simulation5/logs/p_0"]

#read amnd generate dataframe from txt files:
sim1_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1]
sim2_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2]
sim3_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_3]
sim4_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_4]
sim5_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_5]

# Combine the dataframes
sim_initial_combined = pd.concat([sim1_initial_tolerance_df, sim2_initial_tolerance_df, sim3_initial_tolerance_df, sim4_initial_tolerance_df, sim5_initial_tolerance_df], ignore_index=False, axis=1)

#Generate plots:
plt.plot(sim_initial_combined)

# plot 1 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
ax[0, 0].axhline(y=1.0e-05, color="black", linestyle='--')
ax[0, 0].axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_1:
    # desired name in legend
    new_string = string.replace("Processed/Simulation1/logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)
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
ax[0, 0].set_xlim(1, len(sim_initial_combined))

# add legend to the plot
ax[0, 0].legend(legend_1)