import pandas as pd

from rich.progress import track
from dataSeclect.basedata import create_df
import itertools




def bruteforce(create_df):
    csv_content = create_df
    budget = 500
    tmp_profit = 0
    price_list = ()
    action_bought = {}
    content = pd.DataFrame()

    db = csv_content
    for i in track(db.itertuples(), description='[bright_magenta]Progress...'):
        for p_list in itertools.combinations(db.price, i.Index + 1):
            total_price = sum(p_list)

            if 495 < total_price <= budget:
                res = db.loc[db['price'].isin(p_list)]
                total_profit = sum(res.profit)
                if tmp_profit < total_profit:
                    tmp_profit = total_profit
                    price_list = res.price
                    content = res

    for rec_index, rec in content.iterrows():
        action_bought[rec['name']] = rec['price']

    action_bought['Costs:'] = "{:.2f}".format(sum(price_list))
    action_bought['Profits:'] = "{:.2f}".format(tmp_profit)

    return print("BRUTE FORCE \n", "\nCoût total :",
                 action_bought['Costs:'], "\nProfit total :", action_bought['Profits:'], "\n")

d = bruteforce(create_df())
#print(d)