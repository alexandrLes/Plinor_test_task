import pandas as pd
import matplotlib.pyplot as plt
import io
from app.database import data_store

def aggregate_data(timeframe: str):
    df = pd.DataFrame(data_store)
    df['ts'] = pd.to_datetime(df['ts'], unit='s')
    if timeframe == 'hour':
        df = df.set_index('ts').resample('H').sum()
    elif timeframe == 'day':
        df = df.set_index('ts').resample('D').sum()
    elif timeframe == 'week':
        df = df.set_index('ts').resample('W').sum()
    elif timeframe == 'year':
        df = df.set_index('ts').resample('Y').sum()
    else:
        df = df.sum()
    return df

def generate_plot(df):
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    return img_buf
