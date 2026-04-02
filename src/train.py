from .data import stock_data_analysis, import_stock_data
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split


def siu():
    X_test, X_train, y_test, y_train = train_test_split()
    train_size = int(len(df) * 0.8)
    train = df[:train_size]
    test = df[train_size:]
    X_train = train[['Close', 'Return', 'MA10', 'MA50']]
    y_train = train['Target']
    X_test = test[['Close', 'Return', 'MA10', 'MA50']]
    y_test = test['Target']


def main():
    AAPL_data = stock_data_analysis("AAPL", "2020-01-01", "2024-01-01")
    print(AAPL_data)


if __name__ == "__main__":
    main()
