import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)
    df = df.dropna(subset=['Date'])
    df.set_index('Date', inplace=True)

    df.ffill(inplace=True)
    df.bfill(inplace=True)

    power_cols = [col for col in df.columns if 'kW' in col]
    df_power = df[power_cols]

    df_power = df_power.dropna(axis=1, how='all')

    df_power.fillna(0, inplace=True)

    df_hourly = df_power.resample('H').sum()

    return df_hourly

def aggregate_building_data(directory, file_structure):
    building_data_combined = pd.DataFrame()

    for floor, files in file_structure.items():
        for file in files:
            file_path = os.path.join(directory, file)
            df_hourly = preprocess(file_path)

            total_power_building = df_hourly.sum(axis=1)
            total_power_building.name = f'{floor}_total_building_kW'

            if building_data_combined.empty:
                building_data_combined = pd.DataFrame(total_power_building)
            else:
                building_data_combined = pd.concat([building_data_combined, total_power_building], axis=1)

    start_date = '2018-07-01'
    end_date = '2019-12-31'
    complete_date_range = pd.date_range(start=start_date, end=end_date, freq='H')

    building_data_combined = building_data_combined.reindex(complete_date_range)

    building_data_combined.fillna(0, inplace=True)

    building_data_combined['total_building_kW'] = building_data_combined.sum(axis=1)

    #print("Aggregated building data before normalization:\n", building_data_combined.head())

    # Z-score normalization
    scaler = StandardScaler()
    building_data_combined_scaled = scaler.fit_transform(building_data_combined[['total_building_kW']])
    building_data_combined_scaled = pd.DataFrame(building_data_combined_scaled, columns=['total_building_kW'], index=building_data_combined.index)

    building_data_combined_scaled['hour'] = building_data_combined.index.hour
    building_data_combined_scaled['weekday'] = building_data_combined.index.weekday
    building_data_combined_scaled['month'] = building_data_combined.index.month

    return building_data_combined_scaled, scaler



directory = '/content/drive/MyDrive/CU_BEMS_Dataset'
file_structure = {
    'Floor1': ['2018Floor1.csv', '2019Floor1.csv'],
    'Floor2': ['2018Floor2.csv', '2019Floor2.csv'],
    'Floor3': ['2018Floor3.csv', '2019Floor3.csv'],
    'Floor4': ['2018Floor4.csv', '2019Floor4.csv'],
    'Floor5': ['2018Floor5.csv', '2019Floor5.csv'],
    'Floor6': ['2018Floor6.csv', '2019Floor6.csv'],
    'Floor7': ['2018Floor7.csv', '2019Floor7.csv'],
}

building_hourly_consumption, scaler = aggregate_building_data(directory, file_structure)
print(f"Total rows in aggregated data: {len(building_hourly_consumption)}")
print(building_hourly_consumption.head())
