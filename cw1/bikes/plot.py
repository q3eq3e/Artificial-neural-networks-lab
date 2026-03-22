import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("cw1/bikes/data.csv")
df = df[["hr", "cnt"]]

# Compute average cnt for each hour
avg_cnt_per_hr = df.groupby("hr")["cnt"].mean()

# Plot
plt.figure(figsize=(8, 5))
avg_cnt_per_hr.plot(kind="bar")

plt.xlabel("Hour of Day")
plt.ylabel("Average Count (cnt)")
plt.title("Average Count per Hour")
plt.xticks(rotation=0)

plt.show()
