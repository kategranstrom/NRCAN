# import PySAM.Battwatts as bw
import pandas as pd
import PySAM.Battwatts as bw
from pprint import pprint
from matplotlib.backends.backend_pdf import PdfPages
import lyraplot

with PdfPages('RemoteCommunitiesBatteryAnalysis.pdf') as pdf:
  #LASQUETI
  lasqueti_solar_df_lo = pd.read_csv("Lasqueti Island_42_Solar_0.0Loss_200kWh_AC=True_LatAsTilt=True.csv")
  lasqueti_wind_df_lo = pd.read_csv("Lasqueti Island_42_Wind_0.0Loss_fps_fw24_100_x2.csv")

  lasqueti_solar_input_data_lo  = lasqueti_solar_df_lo['Useable Solar Output (kWh)'].tolist()
  lasqueti_solar_load_data_lo  = lasqueti_solar_df_lo['Load (kWh)'].tolist()

  lasqueti_wind_input_data_lo  = lasqueti_wind_df_lo['Useable Wind Output (kWh)'].tolist()
  lasqueti_wind_load_data_lo  = lasqueti_wind_df_lo['Load (kWh)'].tolist()


  lasqueti_solar_df_hi = pd.read_csv("Lasqueti Island_42_Solar_0.0Loss_500kWh_AC=True_LatAsTilt=True.csv")
  lasqueti_wind_df_hi = pd.read_csv("Lasqueti Island_42_Wind_0.0Loss_rrb_energy_v39_500_x1.csv")

  lasqueti_solar_input_data_hi = lasqueti_solar_df_hi['Useable Solar Output (kWh)'].tolist()
  lasqueti_solar_load_data_hi = lasqueti_solar_df_hi['Load (kWh)'].tolist()

  lasqueti_wind_input_data_hi = lasqueti_wind_df_hi['Useable Wind Output (kWh)'].tolist()
  lasqueti_wind_load_data_hi = lasqueti_wind_df_hi['Load (kWh)'].tolist()

  #FORT HOPE
  forthope_solar_df_lo = pd.read_csv("Fort Hope_881_Solar_0.0Loss_400kWh_AC=True_LatAsTilt=True.csv")
  forthope_wind_df_lo = pd.read_csv("Fort Hope_881_Wind_0.0Loss_fps_fw24_100_x4.csv")

  forthope_solar_input_data_lo = forthope_solar_df_lo['Useable Solar Output (kWh)'].tolist()
  forthope_solar_load_data_lo = forthope_solar_df_lo['Load (kWh)'].tolist()

  forthope_wind_input_data_lo = forthope_wind_df_lo['Useable Wind Output (kWh)'].tolist()
  forthope_wind_load_data_lo = forthope_wind_df_lo['Load (kWh)'].tolist()


  forthope_solar_df_hi = pd.read_csv("Fort Hope_881_Solar_0.0Loss_1000kWh_AC=True_LatAsTilt=True.csv")
  forthope_wind_df_hi = pd.read_csv("Fort Hope_881_Wind_0.0Loss_ewt_dw61_1000_x1.csv")

  forthope_solar_input_data_hi = forthope_solar_df_hi['Useable Solar Output (kWh)'].tolist()
  forthope_solar_load_data_hi = forthope_solar_df_hi['Load (kWh)'].tolist()

  forthope_wind_input_data_hi = forthope_wind_df_hi['Useable Wind Output (kWh)'].tolist()
  forthope_wind_load_data_hi = forthope_wind_df_hi['Load (kWh)'].tolist()

  #RANKIN
  rankin_solar_df_lo = pd.read_csv("Rankin Inlet_319_Solar_0.0Loss_800kWh_AC=True_LatAsTilt=True.csv")
  rankin_wind_df_lo = pd.read_csv("Rankin Inlet_319_Wind_0.0Loss_enercon_e53_800_x1.csv")

  rankin_solar_input_data_lo = rankin_solar_df_lo['Useable Solar Output (kWh)'].tolist()
  rankin_solar_load_data_lo = rankin_solar_df_lo['Load (kWh)'].tolist()

  rankin_wind_input_data_lo = rankin_wind_df_lo['Useable Wind Output (kWh)'].tolist()
  rankin_wind_load_data_lo = rankin_wind_df_lo['Load (kWh)'].tolist()


  rankin_solar_df_hi = pd.read_csv("Rankin Inlet_319_Solar_0.0Loss_2300kWh_AC=True_LatAsTilt=True.csv")
  rankin_wind_df_hi = pd.read_csv("Rankin Inlet_319_Wind_0.0Loss_enercon_e82_2300_x1.csv")

  rankin_solar_input_data_hi = rankin_solar_df_hi['Useable Solar Output (kWh)'].tolist()
  rankin_solar_load_data_hi = rankin_solar_df_hi['Load (kWh)'].tolist()

  rankin_wind_input_data_hi = rankin_wind_df_hi['Useable Wind Output (kWh)'].tolist()
  rankin_wind_load_data_hi = rankin_wind_df_hi['Load (kWh)'].tolist()


  solar_model = bw.default("PVWattsBatteryCommercial")
  #24 * 365 = 8760 is the minimum list size for ac- at LEAST 1 year of data. 

  #Set battery configuration
  solar_model.Battery.batt_simple_chemistry = 1
  solar_model.Battery.batt_simple_enable = 1
  solar_model.Battery.batt_simple_kw = 200 # battery size - depends on solar system - abt half
  solar_model.Battery.batt_simple_kwh = 400
  solar_model.Battery.inverter_efficiency = 96 

  ## this is the same code for the wind model 
  wind_model = bw.default("PVWattsBatteryCommercial")
  wind_model.Battery.batt_simple_chemistry = 1 #idk what these mean
  wind_model.Battery.batt_simple_enable = 1
  wind_model.Battery.batt_simple_kw = 200 #battery size, for wind idk what this depends on maybe change this lasqueti_solar_df
  wind_model.Battery.batt_simple_kwh = 400
  wind_model.Battery.inverter_efficiency = 96


  ## end wind model setup

  #Get output data
  for i in solar_model.Outputs.export().keys():
    print(i)

  #solar_model.Battery.load = solar_load_data
  #wind_model.Battery.load = wind_load_data
  # wind_model.execute()
  # solar_model.execute()

  # sum_q0 = solar_model.Outputs.export()["batt_q0"]
  # sum_q0 = sum(solar_model.Outputs.export()["batt_q0"])
  # len_q0 = len(solar_model.Outputs.export()["batt_q0"])
  # sum_q1 = sum(solar_model.Outputs.export()["batt_q1"])
  # len_q1 = len(solar_model.Outputs.export()["batt_q1"])

  #---------------------


  # lyraplot.create_graph("test", solar_model.Outputs.export()["batt_q0"][day*24:(day+1)*24], "Battery Q0")

  #function definition: create_graph(plot_name, y_vals, y_label, y_legend=None, y_vals2=None, y_legend2=None, x_vals=None, x_label=None, ):

  #function definition: create_graph_avg(plot_name, data, data_label, time_period, time_label, data2=None, y_legend=None, y_legend2=None):

  #lyraplot.create_graph_avg("Average battery total charge (q0) per month for a year", solar_model.Outputs.export()["batt_q0"], "Battery total charge [Ah]", 24, "Day", wind_model.Outputs.export()["batt_q0"], "solar model", "wind model")

  #lyraplot.create_graph("Average battery total charge (q0) per day for first 100 hours", solar_model.Outputs.export()["batt_q0"][:100], "Battery total charge [Ah]", "Solar model", wind_model.Outputs.export()["batt_q0"][:100], "Wind model")

  #lyraplot.create_graph("Average battery total charge (q0) per day for first 100 hours", solar_model.Outputs.export()["batt_q0"][:100], "Battery total charge [Ah]", "Solar model", solar_input_data[:100], "Input")

  #def create_graph(plot_name, y_vals, y_label, y_legend=None, y_vals2=None, y_legend2=None, x_vals=None, x_label=None):

#LASQUETI - 3 months
  lasqueti_solar_input_data_lo_watts = [x * 1000 for x in lasqueti_solar_input_data_lo]
  lasqueti_wind_input_data_lo_watts = [x * 1000 for x in lasqueti_wind_input_data_lo]
  solar_model.Battery.ac = lasqueti_solar_input_data_lo_watts
  wind_model.Battery.ac = lasqueti_wind_input_data_lo_watts
  wind_model.execute()
  solar_model.execute()
  q0_solar = solar_model.Outputs.export()["batt_q0"] #batt_q0 is battery total charge
  q0_wind = wind_model.Outputs.export()["batt_q0"]
  lyraplot.create_graph("Lasqueti Low: Solar Energy, Load, and Battery Charge vs Time", q0_solar[:2160], "Energy", "Battery Charge (Ah)", lasqueti_solar_load_data_lo[:2160], "Load (kWh)", lasqueti_solar_input_data_lo[:2160], "Solar Energy Produced (kWh)", pdf = pdf) #load: how much community uses per hour
  lyraplot.create_graph("Lasqueti Low: Wind Energy, Load, and Battery Charge vs Time", q0_wind[:2160], "Energy", "Battery Charge (Ah)", lasqueti_wind_load_data_lo[:2160], "Load (kWh)", lasqueti_wind_input_data_lo[:2160], "Wind Energy Produced (kWh)", pdf = pdf)

  lasqueti_solar_input_data_hi_watts = [x * 1000 for x in lasqueti_solar_input_data_hi]
  lasqueti_wind_input_data_hi_watts = [x * 1000 for x in lasqueti_wind_input_data_hi]
  solar_model.Battery.ac = lasqueti_solar_input_data_hi_watts
  wind_model.Battery.ac = lasqueti_wind_input_data_hi_watts
  wind_model.execute()
  solar_model.execute()
  q0_solar = solar_model.Outputs.export()["batt_q0"]
  q0_wind = wind_model.Outputs.export()["batt_q0"]
  lyraplot.create_graph("Lasqueti High: Solar Energy, Load, and Battery Charge vs Time", q0_solar[:2160], "Energy", "Battery Charge (Ah)", lasqueti_solar_load_data_hi[:2160], "Load (kWh)", lasqueti_solar_input_data_hi[:2160], "Solar Energy Produced (kWh)", pdf = pdf)
  lyraplot.create_graph("Lasqueti High: Wind Energy, Load, and Battery Charge vs Time", q0_wind[:2160], "Energy", "Battery Charge (Ah)", lasqueti_wind_load_data_hi[:2160], "Load (kWh)", lasqueti_wind_input_data_hi[:2160], "Wind Energy Produced (kWh)", pdf = pdf)

# #FORTHOPE
  forthope_solar_input_data_lo_watts = [x * 1000 for x in forthope_solar_input_data_lo]
  forthope_wind_input_data_lo_watts = [x * 1000 for x in forthope_wind_input_data_lo]
  solar_model.Battery.ac = forthope_solar_input_data_lo_watts
  wind_model.Battery.ac = forthope_wind_input_data_lo_watts
  wind_model.execute()
  solar_model.execute()
  q0_solar = solar_model.Outputs.export()["batt_q0"] #batt_q0 is battery total charge
  q0_wind = wind_model.Outputs.export()["batt_q0"]
  lyraplot.create_graph("Fort hope Low: Solar Energy, Load, and Battery Charge vs Time", q0_solar[:2160], "Energy", "Battery Charge (Ah)", forthope_solar_load_data_lo[:2160], "Load (kWh)", forthope_solar_input_data_lo[:2160], "Solar Energy Produced (kWh)", pdf = pdf)
  lyraplot.create_graph("Fort hope Low: Wind Energy, Load, and Battery Charge vs Time", q0_wind[:2160], "Energy", "Battery Charge (Ah)", forthope_wind_load_data_lo[:2160], "Load (kWh)", forthope_wind_input_data_lo[:2160], "Wind Energy Produced (kWh)", pdf = pdf)

  forthope_solar_input_data_hi_watts = [x * 1000 for x in forthope_solar_input_data_hi]
  forthope_wind_input_data_hi_watts = [x * 1000 for x in forthope_wind_input_data_hi]
  solar_model.Battery.ac = forthope_solar_input_data_hi_watts
  wind_model.Battery.ac = forthope_wind_input_data_hi_watts
  wind_model.execute()
  solar_model.execute()
  q0_solar = solar_model.Outputs.export()["batt_q0"]
  q0_wind = wind_model.Outputs.export()["batt_q0"]
  lyraplot.create_graph("Fort hope High: Solar Energy, Load, and Battery Charge vs Time", q0_solar[:2160], "Energy", "Battery Charge (Ah)", forthope_solar_load_data_hi[:2160], "Load (kWh)", forthope_solar_input_data_hi[:2160], "Solar Energy Produced (kWh)", pdf = pdf)
  lyraplot.create_graph("Fort hope High: Wind Energy, Load, and Battery Charge vs Time", q0_wind[:2160], "Energy", "Battery Charge (Ah)", forthope_wind_load_data_hi[:2160], "Load (kWh)", forthope_wind_input_data_hi[:2160], "Wind Energy Produced (kWh)", pdf = pdf)

# #RANKIN
  rankin_solar_input_data_lo_watts = [x * 1000 for x in rankin_solar_input_data_lo]
  rankin_wind_input_data_lo_watts = [x * 1000 for x in rankin_wind_input_data_lo]
  solar_model.Battery.ac = rankin_solar_input_data_lo_watts
  wind_model.Battery.ac = rankin_wind_input_data_lo_watts
  wind_model.execute()
  solar_model.execute()
  q0_solar = solar_model.Outputs.export()["batt_q0"] #batt_q0 is battery total charge
  q0_wind = wind_model.Outputs.export()["batt_q0"]
  lyraplot.create_graph("Rankin Low: Solar Energy, Load, and Battery Charge vs Time", q0_solar[:2160], "Energy", "Battery Charge (Ah)", rankin_solar_load_data_lo[:2160], "Load (kWh)", rankin_solar_input_data_lo[:2160], "Solar Energy Produced (kWh)", pdf = pdf)
  lyraplot.create_graph("Rankin Low: Wind Energy, Load, and Battery Charge vs Time", q0_wind[:2160], "Energy", "Battery Charge (Ah)", rankin_wind_load_data_lo[:2160], "Load (kWh)", rankin_wind_input_data_lo[:2160], "Wind Energy Produced (kWh)", pdf = pdf)

  rankin_solar_input_data_hi_watts = [x * 1000 for x in rankin_solar_input_data_hi]
  rankin_wind_input_data_hi_watts = [x * 1000 for x in rankin_wind_input_data_hi]
  solar_model.Battery.ac = rankin_solar_input_data_hi_watts
  wind_model.Battery.ac = rankin_wind_input_data_hi_watts
  wind_model.execute()
  solar_model.execute()
  q0_solar = solar_model.Outputs.export()["batt_q0"]
  q0_wind = wind_model.Outputs.export()["batt_q0"]
  lyraplot.create_graph("Rankin High: Solar Energy, Load, and Battery Charge vs Time", q0_solar[:2160], "Energy", "Battery Charge (Ah)", rankin_solar_load_data_hi[:2160], "Load (kWh)", rankin_solar_input_data_hi[:2160], "Solar Energy Produced (kWh)", pdf = pdf)
  lyraplot.create_graph("Rankin High: Wind Energy, Load, and Battery Charge vs Time", q0_wind[:2160], "Energy", "Battery Charge (Ah)", rankin_wind_load_data_hi[:2160], "Load (kWh)", rankin_wind_input_data_hi[:2160], "Wind Energy Produced (kWh)", pdf = pdf)

  # sum_load_q0 = sum(solar_model.Outputs.export()["batt_q0"])
  # len_load_q0 = len(solar_model.Outputs.export()["batt_q0"])
  # sum_load_q1 = sum(solar_model.Outputs.export()["batt_q1"])
  # len_load_q1 = len(solar_model.Outputs.export()["batt_q1"])

  # print(f'Q0: {sum_q0/len_q0}')
  # print(f'Q1: {sum_q1/len_q1}')
  # print(f'Q0_load: {sum_load_q0/len_load_q0}')
  # print(f'Q1_load: {sum_load_q1/len_load_q1}')
#for i in solar_model.Outputs.export()["batt_q0"]:
#  print(i)
