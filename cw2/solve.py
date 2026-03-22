import pandas as pd


def label_sale_price(amount):
    if amount <= 100000:
        return 0
    elif amount > 350000:
        return 2
    else:
        return 1


if __name__ == '__main__':
    train_data, test_data = (
        pd.read_csv('train_data.csv'),
        pd.read_csv('test_data.csv'),
    )

    train_data['Target'] = train_data['SalePrice'].apply(label_sale_price)

    train_data = train_data.drop('SalePrice', axis=1)
    