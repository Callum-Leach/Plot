import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd

#!!!Change these file names to suit variable!!!#

#1: initial tolerance files
filenames_1 = ["Processed/Simulation1/logs/p_0", "Processed/Simulation2/logs/p_0", "Processed/Simulation3/logs/p_0", "Processed/Simulation4/logs/p_0", "Processed/Simulation5/logs/p_0"]
#2: final tolerance files
filenames_2 = ["Processed/Simulation1/logs/pFinalRes_0", "Processed/Simulation2/logs/pFinalRes_0", "Processed/Simulation3/logs/pFinalRes_0", "Processed/Simulation4/logs/pFinalRes_0", "Processed/Simulation5/logs/pFinalRes_0"]

#read and generate dataframe from txt files:
initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1]
final_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2]

# Combine the dataframes
initial_combined = pd.concat(initial_tolerance_df, ignore_index=False, axis=1)
final_combined = pd.concat(final_tolerance_df, ignore_index=False, axis=1)

#percentage change tolerance calculations
#!!!Change range to fit number of simulations!!!
percentage_combined = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined), len(final_combined)), 5)), columns=filenames_1)
percentage_combined.index = np.arange(1,len(percentage_combined)+1)

for i in range(0, len(initial_tolerance_df)):
    percentage_combined.iloc[:, i] = ((initial_combined.iloc[:, i] - final_combined.iloc[:, i]) / initial_combined.iloc[:, i]) * 100

#Generate the Plot
plt.plot(percentage_combined)

# plot 4 - % change in initial to final tolerance time series.

legend_1 = ['Sim1', 'Sim2', 'Sim3', 'Sim4', 'Sim5']
# obtain legend names from file names
#for string in legend_1:
#    legend_1.append(': p_0')

# title of plot
plt.title("Percentage change")
# x axis label
plt.xlabel("Iteration")
# y axis label
plt.ylabel("Percentage Change")
# only plot to data range
plt.xlim(1, len(percentage_combined))

# add legend to the plot
plt.legend(legend_1)


# force plot to display in full-screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# display plot until closed
plt.show()
