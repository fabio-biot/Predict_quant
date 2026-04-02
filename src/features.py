import pandas as pd
from .data import stock_data_analysis

data = stock_data_analysis(ticker='AAPL',
                           start_date="2020-01-01",
                           end_date="2024-01-01")
serie_to_compute = data['Close']


def compute_rsi(window: int, serie: pd.Series):
    delta = serie.diff()
    loss = -delta.clip(upper=0)
    gain = delta.clip(lower=0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def hist_data(data: pd.DataFrame):
    data['RSI'] = compute_rsi(14, serie_to_compute)
    return data


def main():
    a = hist_data(data)
    print("SIU")
    print("===" * 50)
    print(a.tail(10))
    print("===" * 50)


if __name__ == "__main__":
    main()
