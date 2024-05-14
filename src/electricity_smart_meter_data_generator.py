import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_datetime = datetime(2024, 5, 1, 0, 0, 0)
end_datetime = start_datetime + timedelta(days=7)
timestamps = pd.date_range(start=start_datetime, end=end_datetime, freq="1min")

num_data_points = len(timestamps)
power_data = np.random.uniform(0, 4000.01, size=num_data_points)  # W
voltage_data = np.random.uniform(220, 240, size=num_data_points)  # 1-phase voltage

data = {"timestamp": timestamps, "power": power_data, "voltage": voltage_data}
df = pd.DataFrame(data)
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")

smart_meter_data = df.to_dict(orient="records")
with open("artificial-data/electricity-meterings.json", "w") as f:
    json.dump(smart_meter_data, f)
print(smart_meter_data[:5])
