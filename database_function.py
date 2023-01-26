import datetime
import sqlite3


class DBManager:
    def __enter__(self):
        self.con = sqlite3.connect("currency.db")
        self.cursor = self.con.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()

    def get_result(self, query):
        res_1 = self.cursor.execute(query)
        result = res_1.fetchone()
        return result

    def write_data(self, query):
        self.cursor.execute(query)
        self.con.commit()


def generate_data():
    data = [
        {'bank': 'a1', 'currency': 'UAH', 'buy_rate': 1.05, 'sale_rate': 0.95},
        {'bank': 'a1', 'currency': 'USD', 'buy_rate': 1.05, 'sale_rate': 0.95},
        {'bank': 'a1', 'currency': 'EUR', 'buy_rate': 1.05, 'sale_rate': 0.95},
        {'bank': 'a1', 'currency': 'GPB', 'buy_rate': 1.05, 'sale_rate': 0.95},
    ]
    date_exchange = datetime.datetime.now().strftime('%Y-%m-%d')
    with DBManager() as db:
        for line in data:
            bank = line['bank']
            currency = line['currency']
            buy_rate = line['buy_rate']
            sale_rate = line['sale_rate']
            query = f'INSERT INTO currency(bank, currency, date_exchange, buy_rate, sale_rate)' \
                    f'VALUES ("{bank}","{currency}","{date_exchange}",{buy_rate},{sale_rate})'
            db.write_data(query)
