import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd

#Simulation 1
#1: Simulation1 initial tolerance
filenames_1_i = ["Processed/Simulation1/logs/p_0", "Processed/Simulation1/logs/p_1", "Processed/Simulation1/logs/Ux_0", "Processed/Simulation1/logs/Uy_0", "Processed/Simulation1/logs/Uz_0", "Processed/Simulation1/logs/k_0", "Processed/Simulation1/logs/epsilon_0"]
filenames_1_f = ["Processed/Simulation1/logs/pFinalRes_0", "Processed/Simulation1/logs/pFinalRes_1", "Processed/Simulation1/logs/UxFinalRes_0", "Processed/Simulation1/logs/UyFinalRes_0", "Processed/Simulation1/logs/UzFinalRes_0", "Processed/Simulation1/logs/kFinalRes_0", "Processed/Simulation1/logs/epsilonFinalRes_0"]
initial_tolerance_df_1 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1_i]
final_tolerance_df_1 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1_f]

#Simulation 2
#2: Simulation1 initial tolerance
filenames_2_i = ["Processed/Simulation2/logs/p_0", "Processed/Simulation2/logs/p_1", "Processed/Simulation2/logs/Ux_0", "Processed/Simulation2/logs/Uy_0", "Processed/Simulation2/logs/Uz_0", "Processed/Simulation2/logs/k_0", "Processed/Simulation2/logs/epsilon_0"]
filenames_2_f = ["Processed/Simulation2/logs/pFinalRes_0", "Processed/Simulation2/logs/pFinalRes_1", "Processed/Simulation2/logs/UxFinalRes_0", "Processed/Simulation2/logs/UyFinalRes_0", "Processed/Simulation2/logs/UzFinalRes_0", "Processed/Simulation2/logs/kFinalRes_0", "Processed/Simulation2/logs/epsilonFinalRes_0"]
initial_tolerance_df_2 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2_i]
final_tolerance_df_2 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2_f]

#Simulation 3
#3: Simulation1 initial tolerance
filenames_3_i = ["Processed/Simulation3/logs/p_0", "Processed/Simulation3/logs/p_1", "Processed/Simulation3/logs/Ux_0", "Processed/Simulation3/logs/Uy_0", "Processed/Simulation3/logs/Uz_0", "Processed/Simulation3/logs/k_0", "Processed/Simulation3/logs/epsilon_0"]
filenames_3_f = ["Processed/Simulation3/logs/pFinalRes_0", "Processed/Simulation3/logs/pFinalRes_1", "Processed/Simulation3/logs/UxFinalRes_0", "Processed/Simulation3/logs/UyFinalRes_0", "Processed/Simulation3/logs/UzFinalRes_0", "Processed/Simulation3/logs/kFinalRes_0", "Processed/Simulation3/logs/epsilonFinalRes_0"]
initial_tolerance_df_3 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_3_i]
final_tolerance_df_3 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_3_f]

#Simulation 4
#4: Simulation1 initial tolerance
filenames_4_i = ["Processed/Simulation4/logs/p_0", "Processed/Simulation4/logs/p_1", "Processed/Simulation4/logs/Ux_0", "Processed/Simulation4/logs/Uy_0", "Processed/Simulation4/logs/Uz_0", "Processed/Simulation4/logs/k_0", "Processed/Simulation4/logs/epsilon_0"]
filenames_4_f = ["Processed/Simulation4/logs/pFinalRes_0", "Processed/Simulation4/logs/pFinalRes_1", "Processed/Simulation4/logs/UxFinalRes_0", "Processed/Simulation4/logs/UyFinalRes_0", "Processed/Simulation4/logs/UzFinalRes_0", "Processed/Simulation4/logs/kFinalRes_0", "Processed/Simulation4/logs/epsilonFinalRes_0"]
initial_tolerance_df_4 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_4_i]
final_tolerance_df_4 = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_4_f]

# Combine the dataframes
initial_combined_1 = pd.concat(initial_tolerance_df_1, ignore_index=False, axis=1)
initial_combined_2 = pd.concat(initial_tolerance_df_2, ignore_index=False, axis=1)
initial_combined_3 = pd.concat(initial_tolerance_df_3, ignore_index=False, axis=1)
initial_combined_4 = pd.concat(initial_tolerance_df_4, ignore_index=False, axis=1)
final_combined_1 = pd.concat(final_tolerance_df_1, ignore_index=False, axis=1)
final_combined_2 = pd.concat(final_tolerance_df_2, ignore_index=False, axis=1)
final_combined_3 = pd.concat(final_tolerance_df_3, ignore_index=False, axis=1)
final_combined_4 = pd.concat(final_tolerance_df_4, ignore_index=False, axis=1)


#relative tolerance calculations
#Simulation 1
#!!!Change range to fit number of simulations!!!
relative_combined_1 = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined_1), len(final_combined_1)), 7)), columns=filenames_1_i)
relative_combined_1.index = np.arange(1,len(relative_combined_1)+1)

for i in range(0, len(initial_tolerance_df_1)):
    relative_combined_1.iloc[:, i] = final_combined_1.iloc[:, i] / initial_combined_1.iloc[:, i]


#Simulation 2
#!!!Change range to fit number of simulations!!!
relative_combined_2 = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined_2), len(final_combined_2)), 7)), columns=filenames_1_i)
relative_combined_2.index = np.arange(1,len(relative_combined_2)+1)

for i in range(0, len(initial_tolerance_df_2)):
    relative_combined_2.iloc[:, i] = final_combined_2.iloc[:, i] / initial_combined_2.iloc[:, i]

#Simulation 3
#!!!Change range to fit number of simulations!!!
relative_combined_3 = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined_3), len(final_combined_3)), 7)), columns=filenames_1_i)
relative_combined_3.index = np.arange(1,len(relative_combined_3)+1)

for i in range(0, len(initial_tolerance_df_3)):
    relative_combined_3.iloc[:, i] = final_combined_3.iloc[:, i] / initial_combined_3.iloc[:, i]

#Simulation 4
#!!!Change range to fit number of simulations!!!
relative_combined_4 = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined_4), len(final_combined_4)), 7)), columns=filenames_1_i)
relative_combined_4.index = np.arange(1,len(relative_combined_4)+1)

for i in range(0, len(initial_tolerance_df_4)):
    relative_combined_4.iloc[:, i] = final_combined_4.iloc[:, i] / initial_combined_4.iloc[:, i]

# define a figure, with subplots as an array "ax" 
fig, ax = plt.subplots(2,2)
fig.suptitle("Relative Tolerances vs. Iteration")

#Generate plots:
ax[0, 0].plot(relative_combined_1)
ax[0, 1].plot(relative_combined_2)
ax[1, 0].plot(relative_combined_3)
ax[1, 1].plot(relative_combined_4)


# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_1_i:
    # desired name in legend
    new_string = string.replace("Processed/Simulation1/logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)

# plot 1 - relative tol time series Simulation 1

# title of plot
ax[0, 0].set_title("Simulation 1")
# x axis label
ax[0, 0].set_xlabel("Iteration")
# y axis label
ax[0, 0].set_ylabel("Relative Tolerances")
# log scale on y axis since skewed to small residuals
ax[0, 0].set_yscale("log")
# only plot to data range
ax[0, 0].set_xlim(1, len(relative_combined_1))

# add legend to the plot
ax[0, 0].legend(legend_1)


# plot 2 - relative tol time series Simulation 2

# title of plot
ax[0, 1].set_title("Simulation 2")
# x axis label
ax[0, 1].set_xlabel("Iteration")
# y axis label
ax[0, 1].set_ylabel("Relative Tolerances")
# log scale on y axis since skewed to small residuals
ax[0, 1].set_yscale("log")
# only plot to data range
ax[0, 1].set_xlim(1, len(relative_combined_2))

# add legend to the plot
ax[0, 1].legend(legend_1)

# plot 3 - relative tol time series Simulation 3

# title of plot
ax[1, 0].set_title("Simulation 3")
# x axis label
ax[1, 0].set_xlabel("Iteration")
# y axis label
ax[1, 0].set_ylabel("Relative Tolerances")
# log scale on y axis since skewed to small residuals
ax[1, 0].set_yscale("log")
# only plot to data range
ax[1, 0].set_xlim(1, len(relative_combined_3))

# add legend to the plot
ax[1, 0].legend(legend_1)

# plot 4 - relative tol time series Simulation 4

# title of plot
ax[1, 1].set_title("Simulation 4")
# x axis label
ax[1, 1].set_xlabel("Iteration")
# y axis label
ax[1, 1].set_ylabel("Relative Tolerances")
# log scale on y axis since skewed to small residuals
ax[1, 1].set_yscale("log")
# only plot to data range
ax[1, 1].set_xlim(1, len(relative_combined_4))

# add legend to the plot
ax[1, 1].legend(legend_1)


# force plot to display in full-screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# display plot until closed
plt.show()

