import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
scoreslist=df["reading score"].to_list()
mean=statistics.mean(scoreslist)
median=statistics.median(scoreslist)
mode=statistics.mode(scoreslist)
stdeviation=statistics.stdev(scoreslist)
print("Mean, Median, Mode, and Standard Deviation of the list respectively: {}, {}, {} and {}".format(mean, median, mode, stdeviation))

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean-stdeviation, mean+stdeviation
second_std_deviation_start, second_std_deviation_end = mean-(2*stdeviation), mean+(2*stdeviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdeviation), mean+(3*stdeviation)
#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([scoreslist], ["Reading Scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()
#Printing the findings
list_of_data_within_1_std_deviation = [result for result in scoreslist if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in scoreslist if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in scoreslist if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(stdeviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(scoreslist)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(scoreslist)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(scoreslist)))