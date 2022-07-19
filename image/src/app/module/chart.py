#!/usr/bin/env python
#
import matplotlib.pyplot as plt
from os import path

outpath = "/app/image/src/app/save_image"

def plot_graph(
	data=[], 
	timestamp=[], 
	x_lable='timestamp',
	y_lable='data',
	graph_title='Sensor Data Graph',
	chart_filename='data_graph.png'):

	# plotting the points
	plt.plot(
		timestamp,
		data,
		color='green',
		linestyle='dashed',
		linewidth = 3,
		marker='o',
		markerfacecolor='blue',
		markersize=5
		)

	# naming the x axis
	plt.xlabel(x_lable)
	# naming the y axis
	plt.ylabel(y_lable)

	# giving a title to my graph
	plt.title(graph_title)

	# function to show the plot
	plt.savefig(path.join(outpath,chart_filename))