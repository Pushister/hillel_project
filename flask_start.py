from flask import Flask
from flask import request, render_template
from database_function import DBManager
from worker import add

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login_user():
    return "OK"


@app.route("/logout", methods=['GET'])
def logout():
    add.apply_async(args=(1, 2))
    return "Logout"


@app.route("/register", methods=['GET', 'POST'])
def register():
    return "OK"


@app.route("/user_page", methods=['GET'])
def user_page():
    return "OK"


@app.route("/currency", methods=['GET', 'POST'])
def currency_converter():

    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        with DBManager() as db:
            buy_rate_1, sale_rate_1 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE '
                                                    f'bank = "{user_bank}" and date_excange = '
                                                    f'"{user_date}" and currency = "{user_currency_1}"')
            buy_rate_2, sale_rate_2 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE '
                                                    f'bank = "{user_bank}" and date_excange = '
                                                    f'"{user_date}" and currency = "{user_currency_2}"')

        cur_exchange_buy = float(buy_rate_2) / float(buy_rate_1)
        cur_exchange_sale = float(sale_rate_2) / float(sale_rate_1)

        return render_template('data_form.html',
                               cur_excange_buy=cur_exchange_buy,
                               cur_excange_sale=cur_exchange_sale,
                               user_currency_1=user_currency_1,
                               user_currency_2=user_currency_2
                               )
    else:
        return render_template('data_form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


