#!/usr/bin/env python
#
import matplotlib.pyplot as plt


def plot_graph(
	data=None, 
	timestamp=None, 
	x_lable='timestamp',
	y_lable='data',
	graph_title='Sensor Data Graph',
	chart_filename='data_graph.png'):

	if isinstance(data, (None)):
		data = []
	if isinstance(timestamp, (None)):
		timestamp = []
	
	# plotting the points
	plt.plot(data, timestamp, color='green', linestyle='dashed', linewidth = 3,
			marker='o', markerfacecolor='blue', markersize=1)

	# naming the x axis
	plt.xlabel(x_lable)
	# naming the y axis
	plt.ylabel(y_lable)

	# giving a title to my graph
	plt.title(graph_title)

	# function to show the plot

	plt.savefig(chart_filename)
