import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd

#!!!Change these file names to suit variable!!!#

#1: initial tolerance files
filenames_1 = ["Processed/Simulation1/logs/p_0", "Processed/Simulation2/logs/p_0", "Processed/Simulation3/logs/p_0", "Processed/Simulation4/logs/p_0", "Processed/Simulation5/logs/p_0"]
#2: final tolerance files
filenames_2 = ["Processed/Simulation1/logs/pFinalRes_0", "Processed/Simulation2/logs/pFinalRes_0", "Processed/Simulation3/logs/p_0", "Processed/Simulation4/logs/pFinalRes_0", "Processed/Simulation5/logs/pFinalRes_0"]
#3: number of iterations files
filenames_3 = ["Processed/Simulation1/logs/pIters_0", "Processed/Simulation2/logs/pIters_0", "Processed/Simulation3/logs/pIters_0", "Processed/Simulation4/logs/pIters_0", "Processed/Simulation5/logs/pIters_0"]

#read and generate dataframe from txt files:
initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1]
final_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2]
num_iterations_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_3]

# Combine the dataframes
initial_combined = pd.concat(initial_tolerance_df, ignore_index=False, axis=1)
final_combined = pd.concat(final_tolerance_df, ignore_index=False, axis=1)
num_iterations_combined = pd.concat(num_iterations_df, ignore_index=False, axis=1)

#percentage change tolerance calculations
#!!!Change range to fit number of simulations!!!
percentage_combined_sim1 = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined), len(final_combined)), 7)), columns=filenames_1)
percentage_combined.index = np.arange(1,len(percentage_combined)+1)

for i in range(0, len(initial_tolerance_df)):
    percentage_combined.iloc[:, i] = ((initial_combined.iloc[:, i] - final_combined.iloc[:, i]) / initial_combined.iloc[:, i]) * 100

#Generate the Plot
plt.plot(percentage_combined)

# plot 1 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
plt.axhline(y=1.0e-05, color="black", linestyle='--')
plt.axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_1:
    # desired name in legend
    new_string = string.replace("Processed/Simulation1/logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)
# title of plot
plt.title("Residual vs. Iteration")
# x axis label
plt.xlabel("Iteration")
# y axis label
plt.ylabel("Residual")
# log scale on y axis since skewed to small residuals
plt.yscale("log")
# only plot to data range
#!!! fix label issues with starting x axis!!!
plt.xlim(1, len(initial_combined))

# add legend to the plot
plt.legend(legend_1)


# force plot to display in full-screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# display plot until closed
plt.show()
