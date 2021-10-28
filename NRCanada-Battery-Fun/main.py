# import PySAM.Battwatts as bw
import pandas as pd
import PySAM.Battwatts as bw
from pprint import pprint
import lyraplot

#Get input data as a pandas dataframe
lasqueti_solar_df = pd.read_csv("Lasqueti Island_42_Solar_0.0Loss_200kWh_AC=True_LatAsTilt=True.csv")
lasqueti_wind_df = pd.read_csv("Lasqueti Island_42_Wind_0.0Loss_fps_fw24_100_x2.csv")

solar_input_data = lasqueti_solar_df['Useable Solar Output (kWh)'].tolist()
solar_load_data = lasqueti_solar_df['Load (kWh)'].tolist()

wind_input_data = lasqueti_wind_df['Useable Wind Output (kWh)'].tolist()
wind_load_data = lasqueti_wind_df['Load (kWh)'].tolist()

#FORT HOPE
forthope_solar_df = pd.read_csv("Lasqueti Island_42_Solar_0.0Loss_200kWh_AC=True_LatAsTilt=True.csv")
forthope_wind_df = pd.read_csv("Lasqueti Island_42_Wind_0.0Loss_fps_fw24_100_x2.csv")

solar_input_data = forthope_solar_df['Useable Solar Output (kWh)'].tolist()
solar_load_data = forthope_solar_df['Load (kWh)'].tolist()

wind_input_data = forthope_wind_df['Useable Wind Output (kWh)'].tolist()
wind_load_data = forthope_wind_df['Load (kWh)'].tolist()

#RANKIN
rankin_solar_df = pd.read_csv("Lasqueti Island_42_Solar_0.0Loss_200kWh_AC=True_LatAsTilt=True.csv")
rankin_wind_df = pd.read_csv("Lasqueti Island_42_Wind_0.0Loss_fps_fw24_100_x2.csv")

solar_input_data = rankin_solar_df['Useable Solar Output (kWh)'].tolist()
solar_load_data = rankin_solar_df['Load (kWh)'].tolist()

wind_input_data = rankin_wind_df['Useable Wind Output (kWh)'].tolist()
wind_load_data = rankin_wind_df['Load (kWh)'].tolist()


energy_produced_kWh = 21.768262405219

#solar_model =bw.new()
solar_model = bw.default("PVWattsBatteryCommercial")
#print(type(solar_model))
#print(solar_model.export())

#24 * 365 = 8760 is the minimum list size for ac- at LEAST 1 year of data. 

#Set battery configuration
solar_model.Battery.ac = solar_input_data
#solar_model.Battery.dc = [12,4,5]
solar_model.Battery.batt_simple_chemistry = 0
solar_model.Battery.batt_simple_enable = 1
solar_model.Battery.batt_simple_kw = 5 # battery size - depends on solar system - abt half
solar_model.Battery.batt_simple_kwh = 10
solar_model.Battery.inverter_efficiency = 96 

## this is the same code for the wind model 
wind_model = bw.default("PVWattsBatteryCommercial") 
wind_model.Battery.ac = wind_input_data
wind_model.Battery.batt_simple_chemistry = 0 #idk what these mean
wind_model.Battery.batt_simple_enable = 1
wind_model.Battery.batt_simple_kw = 5 #battery size, for wind idk what this depends on maybe change this lasqueti_solar_df
wind_model.Battery.batt_simple_kwh = 10
wind_model.Battery.inverter_efficiency = 96

## end wind model setup

#Get output data
for i in solar_model.Outputs.export().keys():
  print(i)

#solar_model.Battery.load = solar_load_data
#wind_model.Battery.load = wind_load_data
wind_model.execute()
solar_model.execute()

sum_q0 = sum(solar_model.Outputs.export()["batt_q0"])
len_q0 = len(solar_model.Outputs.export()["batt_q0"])
sum_q1 = sum(solar_model.Outputs.export()["batt_q1"])
len_q1 = len(solar_model.Outputs.export()["batt_q1"])

#---------------------


# lyraplot.create_graph("test", solar_model.Outputs.export()["batt_q0"][day*24:(day+1)*24], "Battery Q0")

#function definition: create_graph(plot_name, y_vals, y_label, y_legend=None, y_vals2=None, y_legend2=None, x_vals=None, x_label=None, ):

#function definition: create_graph_avg(plot_name, data, data_label, time_period, time_label, data2=None, y_legend=None, y_legend2=None):

#lyraplot.create_graph_avg("Average battery total charge (q0) per month for a year", solar_model.Outputs.export()["batt_q0"], "Battery total charge [Ah]", 24, "Day", wind_model.Outputs.export()["batt_q0"], "solar model", "wind model")

#lyraplot.create_graph("Average battery total charge (q0) per day for first 100 hours", solar_model.Outputs.export()["batt_q0"][:100], "Battery total charge [Ah]", "Solar model", wind_model.Outputs.export()["batt_q0"][:100], "Wind model")

#lyraplot.create_graph("Average battery total charge (q0) per day for first 100 hours", solar_model.Outputs.export()["batt_q0"][:100], "Battery total charge [Ah]", "Solar model", solar_input_data[:100], "Input")

#def create_graph(plot_name, y_vals, y_label, y_legend=None, y_vals2=None, y_legend2=None, x_vals=None, x_label=None):

lyraplot.create_graph("Load and Solar output vs time", solar_load_data[:100], "Energy", "Load", solar_input_data[:100], "Solar")

sum_load_q0 = sum(solar_model.Outputs.export()["batt_q0"])
len_load_q0 = len(solar_model.Outputs.export()["batt_q0"])
sum_load_q1 = sum(solar_model.Outputs.export()["batt_q1"])
len_load_q1 = len(solar_model.Outputs.export()["batt_q1"])

print(f'Q0: {sum_q0/len_q0}')
print(f'Q1: {sum_q1/len_q1}')
print(f'Q0_load: {sum_load_q0/len_load_q0}')
print(f'Q1_load: {sum_load_q1/len_load_q1}')
#for i in solar_model.Outputs.export()["batt_q0"]:
#  print(i)