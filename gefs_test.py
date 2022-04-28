import s3fs
import xarray as xar
import os
import matplotlib.pyplot as plt

gefs_s3_path = 's3://noaa-gefs-pds' #path to the PUBLIC bucket reanalysis-data, and the mapbox token within it

year_issued=2022
month_issued='04'
day_issued='27'
time_issued='00'

forecast_date=f'gefs.{year_issued}{month_issued}{day_issued}'#/{time_issued}/pgrb2a/'

full_path = f'{gefs_s3_path}/{forecast_date}/{time_issued}/atmos/pgrb2ap5/gec00.t00z.pgrb2a.0p50.f000'

fs = s3fs.S3FileSystem(anon=True)

# fs.ls(f'{gefs_s3_path}/gefs.20220425')
# available_forecasts_issued_on_specified_date = fs.ls(full_path)

if not os.path.isfile('gec00.t00z.pgrb2a.0p50.f000'):
    fs.get(full_path,"gec00.t00z.pgrb2a.0p50.f000")
# store = s3fs.S3Map(root=full_path, s3=fs, check=False) #sets up the map to the object

# ds_gcs = xar.open_dataset(
#     full_path,
#     backend_kwargs={
#         "storage_options": {"project": "<project-name>", "token": None}
#     },
#     engine="zarr",
# )

dataset = xar.open_dataset('./gec00.t00z.pgrb2a.0p50.f000', engine="cfgrib")

# dataset.to_zarr('./gec00.t00z.pgrb2a.0p50.f000.zarr')

# print(forecast_date=='gefs.20220425')
# print(forecast_date)
# type(full_path

