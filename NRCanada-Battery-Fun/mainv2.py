import pandas as pd
import PySAM.Pvwattsv7 as pv

solar_model = pv.default("PVWattsBatteryCommercial")

solar_model.SolarResource.solar_resource_file = "community_42_env.csv"

weather = dict()
weather['lat'] = float(49.48)
weather['lon'] = float(-124.27)

#solar_model.SolarResource.solar_resource_data = weather

print(solar_model.SolarResource.export()  )


solar_model.execute()