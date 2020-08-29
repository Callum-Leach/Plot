import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd


#1: Simulation1 initial tolerance
filenames_1 = ["Processed/Simulation1/logs/p_0", "Processed/Simulation1/logs/p_1", "Processed/Simulation1/logs/Ux_0", "Processed/Simulation1/logs/Uy_0", "Processed/Simulation1/logs/Uz_0", "Processed/Simulation1/logs/k_0", "Processed/Simulation1/logs/epsilon_0"]

#2: Simulation1 initial tolerance
filenames_2 = ["Processed/Simulation2/logs/p_0", "Processed/Simulation2/logs/p_1", "Processed/Simulation2/logs/Ux_0", "Processed/Simulation2/logs/Uy_0", "Processed/Simulation2/logs/Uz_0", "Processed/Simulation2/logs/k_0", "Processed/Simulation2/logs/epsilon_0"]

#3: Simulation1 initial tolerance
filenames_3 = ["Processed/Simulation3/logs/p_0", "Processed/Simulation3/logs/p_1", "Processed/Simulation3/logs/Ux_0", "Processed/Simulation3/logs/Uy_0", "Processed/Simulation3/logs/Uz_0", "Processed/Simulation3/logs/k_0", "Processed/Simulation3/logs/epsilon_0"]

#4: Simulation1 initial tolerance
filenames_4 = ["Processed/Simulation4/logs/p_0", "Processed/Simulation4/logs/p_1", "Processed/Simulation4/logs/Ux_0", "Processed/Simulation4/logs/Uy_0", "Processed/Simulation4/logs/Uz_0", "Processed/Simulation4/logs/k_0", "Processed/Simulation4/logs/epsilon_0"]


#read amnd generate dataframe from txt files:
sim1_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1]
sim2_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2]
sim3_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_3]
sim4_initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_4]

# Combine the dataframes
sim1_initial_combined = pd.concat(sim1_initial_tolerance_df, ignore_index=False, axis=1)
sim2_initial_combined = pd.concat(sim2_initial_tolerance_df, ignore_index=False, axis=1)
sim3_initial_combined = pd.concat(sim3_initial_tolerance_df, ignore_index=False, axis=1)
sim4_initial_combined = pd.concat(sim4_initial_tolerance_df, ignore_index=False, axis=1)

# define a figure, with subplots as an array "ax" 
fig, ax = plt.subplots(2,2)


#Generate plots:
ax[0, 0].plot(sim1_initial_combined)
ax[0, 1].plot(sim2_initial_combined)
ax[1, 0].plot(sim3_initial_combined)
ax[1, 1].plot(sim4_initial_combined)

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
ax[0, 0].set_xlim(1, len(sim1_initial_combined))

# add legend to the plot
ax[0, 0].legend(legend_1)

# plot 2 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
ax[0, 1].axhline(y=1.0e-05, color="black", linestyle='--')
ax[0, 1].axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_2:
    # desired name in legend
    new_string = string.replace("Processed/Simulation2/logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)
# title of plot
ax[0, 1].set_title("Residual vs. Iteration")
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
ax[0, 1].legend(legend_1)

# plot 3 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
ax[1, 0].axhline(y=1.0e-05, color="black", linestyle='--')
ax[1, 0].axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_3:
    # desired name in legend
    new_string = string.replace("Processed/Simulation3/logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)
# title of plot
ax[1, 0].set_title("Residual vs. Iteration")
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
ax[1, 0].legend(legend_1)



# plot 4 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
ax[1, 1].axhline(y=1.0e-05, color="black", linestyle='--')
ax[1, 1].axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_4:
    # desired name in legend
    new_string = string.replace("Processed/Simulation4/logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)
# title of plot
ax[1, 1].set_title("Residual vs. Iteration")
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
ax[1, 1].legend(legend_1)



# force plot to display in full-screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# display plot until closed
plt.show()