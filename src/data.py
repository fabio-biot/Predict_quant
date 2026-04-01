try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import yfinance as yf
except ImportError as e:
    print(f"Error importing module: {e}")
    exit()


def import_stock_data(ticker: str, start_date: str, end_date: str):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data


def stock_data_analysis(ticker: str, start_date: str, end_date: str):
    hist_data = import_stock_data(ticker, start_date, end_date)
    if isinstance(hist_data.columns, pd.MultiIndex):
        hist_data.columns = hist_data.columns.get_level_values(0)
    hist_data = hist_data.reset_index()
    hist_data['MA20'] = hist_data['Close'].rolling(window=20).mean()
    hist_data['MA50'] = hist_data['Close'].rolling(window=50).mean()
    rolling_std = hist_data['Close'].rolling(20).std()
    hist_data['BB_upper'] = hist_data['MA20'] + 2 * rolling_std
    hist_data['BB_lower'] = hist_data['MA20'] - 2 * rolling_std
    hist_data = hist_data.dropna()
    return hist_data


def list_tickers():
    Matrix_data = ['AAPL']
    return Matrix_data


def plot_stock_data(ticker: str, hist_data: pd.DataFrame):

    print(f"{ticker} data: {hist_data.head()}")
    print(f"{ticker} data: {hist_data.columns}")
    plt.plot(hist_data['Date'], hist_data['Close'], label=ticker, color='blue')
    plt.plot(hist_data['Date'], hist_data['MA20'], label=ticker, color='blue', linestyle='--')
    plt.plot(hist_data['Date'], hist_data['MA50'], label=ticker, color='blue', linestyle=':')
    plt.plot(hist_data['Date'], hist_data['BB_upper'], label=ticker, color='red', linestyle=':')
    plt.plot(hist_data['Date'], hist_data['BB_lower'], label=ticker, color='red', linestyle=':')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Price Analysis')
    plt.legend()
    # plt.savefig("matrix_analysis.png")
    plt.show()


def main():
    print("\nUsing Pandas to analyse Stock data:")
    tickers = list_tickers()
    for ticker in tickers:
        hist_data = stock_data_analysis(ticker, "2020-01-01", "2021-01-01")
        # plot_stock_data(ticker, hist_data)
        print(f"{ticker} data: {hist_data.head()}")
    print("Analysis complete!")


if __name__ == "__main__":
    main()
