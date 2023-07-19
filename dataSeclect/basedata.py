import pandas as pd


def create_df() -> list:
    #samples = 20
    allfiles = ["dataset2.csv"]
    dataframes = []
    for filename in allfiles:
        db_list = pd.read_csv('data/%s' % (filename), sep=',',
                         dtype={
                             'name': str,
                             'price': float,
                             'profit': float,
                             'benefits': float
                         })
        db_list = db_list[db_list.price > 0]
        db_list['benefits'] = (db_list['profit'] / 100) * db_list['price']
        db_list = db_list.sort_values(by='profit', ascending=False).reset_index().drop(columns="index")
        dataframes.append(db_list)
    result = pd.concat(dataframes)
    #print(result)
    return result


#k = create_df()
#print(k)