# import PySAM.Battwatts as bw
import pandas as pd
import PySAM.Battwatts as bw
from pprint import pprint
from matplotlib.backends.backend_pdf import PdfPages
import lyraplot

Battery = {
  'batt_simple_chemistry': 1,
  'batt_simple_enable': 1,
  'batt_simple_kw': 200,
  'batt_simple_kwh': 400,
  'inverter_efficiency': 96
}

communities = {
  "Lasqueti Island": ["Lasqueti Island_42_Solar_0.0Loss_200kWh_AC=True_LatAsTilt=True.csv", "Lasqueti Island_42_Wind_0.0Loss_fps_fw24_100_x2.csv", "Lasqueti Island_42_Solar_0.0Loss_500kWh_AC=True_LatAsTilt=True.csv", "Lasqueti Island_42_Wind_0.0Loss_rrb_energy_v39_500_x1.csv"],
  "Fort Hope": ["Fort Hope_881_Solar_0.0Loss_400kWh_AC=True_LatAsTilt=True.csv", "Fort Hope_881_Wind_0.0Loss_fps_fw24_100_x4.csv", "Fort Hope_881_Solar_0.0Loss_1000kWh_AC=True_LatAsTilt=True.csv", "Fort Hope_881_Wind_0.0Loss_ewt_dw61_1000_x1.csv"],
  "Rankin Inlet": ["Rankin Inlet_319_Solar_0.0Loss_800kWh_AC=True_LatAsTilt=True.csv", "Rankin Inlet_319_Wind_0.0Loss_enercon_e53_800_x1.csv", "Rankin Inlet_319_Solar_0.0Loss_2300kWh_AC=True_LatAsTilt=True.csv", "Rankin Inlet_319_Wind_0.0Loss_enercon_e82_2300_x1.csv"]
}

def createAndExecuteModel(input_data, load_data, modelName, pdf):
  model = bw.default("PVWattsBatteryCommercial")
  # set battery configuration
  model.Battery.assign(Battery)

  # convert the input data from kWh to W since the ac parameter is in W
  input_data_watts = [x * 1000 for x in input_data]
  model.Battery.ac = input_data_watts
  model.Battery.load = load_data
  model.execute()

  # batt_q0 is battery total charge
  batt_total_charge = model.Outputs.export()["batt_q0"]
  
  # graph the first numDays of the battery total charge (batt_q0) for each simulated model and output to pdf
  numDays = 90
  numDataPts = numDays*24
  lyraplot.create_graph(f"{modelName} Energy, Load, and Battery Charge vs Time", batt_total_charge[:numDataPts], "Energy", "Battery Charge (Ah)", load_data[:numDataPts], "Load (kWh)", input_data[:numDataPts], "Energy Produced (kWh)", pdf = pdf)

pdf = PdfPages('RemoteCommunitiesBatteryAnalysis.pdf')

for community in communities.keys():
  solar_df_lo = pd.read_csv(communities[community][0])
  wind_df_lo = pd.read_csv(communities[community][1])
  solar_df_hi = pd.read_csv(communities[community][2])
  wind_df_hi = pd.read_csv(communities[community][3])

  solar_input_data_lo  = solar_df_lo['Useable Solar Output (kWh)'].tolist()
  solar_load_data_lo  = solar_df_lo['Load (kWh)'].tolist()
  wind_input_data_lo  = wind_df_lo['Useable Wind Output (kWh)'].tolist()
  wind_load_data_lo  = wind_df_lo['Load (kWh)'].tolist()

  solar_input_data_hi = solar_df_hi['Useable Solar Output (kWh)'].tolist()
  solar_load_data_hi = solar_df_hi['Load (kWh)'].tolist()
  wind_input_data_hi = wind_df_hi['Useable Wind Output (kWh)'].tolist()
  wind_load_data_hi = wind_df_hi['Load (kWh)'].tolist()

  createAndExecuteModel(solar_input_data_lo, solar_load_data_lo, f"{community} Low: Solar", pdf)
  createAndExecuteModel(wind_input_data_lo, wind_load_data_lo, f"{community} Low: Wind", pdf)

  createAndExecuteModel(solar_input_data_hi, solar_load_data_hi, f"{community} High: Solar", pdf)
  createAndExecuteModel(wind_input_data_hi, wind_load_data_hi, f"{community} High: Wind", pdf)

pdf.close()
