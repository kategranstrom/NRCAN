import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages

def create_graph_avg(plot_name, data, data_label, time_period, time_label, data2=None, y_legend=None, y_legend2=None):
  avg_arr = [0] * int(len(data)/time_period)
  for i in range(len(avg_arr)):
    avg_arr[i] = np.average( data[time_period * i: time_period * (i+1)] ) 

  if(data2):
    avg_arr2 = [0] * int(len(data2)/time_period)
    for i in range(len(avg_arr2)):
      avg_arr2[i] = np.average( data2[time_period * i: time_period * (i+1)] ) 

  create_graph(plot_name, avg_arr, data_label, x_label=time_label, y_vals2=avg_arr2,y_legend=y_legend, y_legend2=y_legend2)
  


def create_graph(plot_name, y_vals, y_label, y_legend=None, y_vals2=None, y_legend2=None, y_vals3=None, y_legend3=None, x_vals=None, x_label=None, pdf=None):
  
  plt.title(plot_name)
  # plt.figure(figsize=(20,15))
  if(x_vals != None):
    plt.plot(x_vals, y_vals)
    plt.xlabel(x_label)
  else:
    plt.plot(y_vals)
    legendArray = [y_legend]
    if (y_vals3):
      # print("test")
      plt.plot(y_vals3)
      legendArray.append(y_legend3)
    if(y_vals2):
      plt.plot(y_vals2)
      legendArray.append(y_legend2)
    # else:
    #   plt.legend([y_legend])
    plt.legend(legendArray)
    plt.xticks(np.arange(len(y_vals)), np.arange(1, len(y_vals)+1))
    if(x_label == None):
      plt.xlabel("Hours") #Default val
    else:
      plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.locator_params(axis='x', nbins=10)
  # plt.axes([0, 0.6, 1, 1])
  pdf.savefig()
  plt.close()

