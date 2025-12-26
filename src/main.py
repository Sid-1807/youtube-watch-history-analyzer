import matplotlib.pyplot as plt
from load_data import load_watch_history
from clean_data import extract_watch_data,clean_time

raw_data = load_watch_history("data/watch-history.json")
df = extract_watch_data(raw_data)
df=clean_time(df)
df["month"] = df["time"].dt.to_period("M")


#print(df.head())
#print(df.info())

monthly_counts = (
    df.groupby(["month", "channel"])
      .size()
      .reset_index(name="count")
)

#print(monthly_counts.head())

top_channel_per_month = (
    monthly_counts
    .sort_values(["month", "count"], ascending=[True, False])
    .groupby("month")
    .head(1)
)

#print(top_channel_per_month.head())

plt.figure(figsize=(12, 6))

labels = top_channel_per_month["channel"] + " (" + top_channel_per_month["count"].astype(str) + ")"

plt.bar(top_channel_per_month["month"].astype(str),
        top_channel_per_month["count"])

plt.xticks(rotation=45)
plt.title("Most Watched YouTube Channel per Month")
plt.xlabel("Month")
plt.ylabel("Watch Count")

for i, label in enumerate(labels):
    plt.text(i, top_channel_per_month["count"].iloc[i],
             label, ha="center", va="bottom", fontsize=8, rotation=90)

plt.tight_layout()
plt.show()



