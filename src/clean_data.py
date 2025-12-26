import pandas as pd

def extract_watch_data(raw_data):
    records = []

    for item in raw_data:
        try:
            time = item["time"]
            channel = item["subtitles"][0]["name"]

            records.append({
                "time": time,
                "channel": channel
            })
        except (KeyError, IndexError):
            # Skip entries like ads, deleted videos, or missing channel info
            continue

    df = pd.DataFrame(records)
    return df
def clean_time(df):
    df["time"] = pd.to_datetime(df["time"])
    return df
