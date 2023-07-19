from dataSeclect.basedata import create_df
from rich.progress import track
import time


def optimize(create_df):
    db = create_df
    total_cost = 0  # coût total des actions selectionné qui à Zero
    total_profit = 0  # le profit total des actions selectionné qui à zero
    actions = []  # les actions selectionné (liste vide)
    cost_maximum = 500

    for i, j in track(enumerate(db.price)):  # passons tout les coûts en revue
        total_cost += j  # à chaque tour de boucle on incremente le compteur total_cost
        total_profit += db['benefits'][i] # on incrémente le compteur total_profit aussi
        actions.append(db['name'][i])  # on ajoute le nom indice i de l'élément j dans actions

        if total_cost >= cost_maximum: # on determine à partir de quel j le compteur dépasse 500
            total_cost -= j  # On retire le dernier élément j a partir duquel le compteur est > 500
            total_profit -= db['benefits'][i] # même chose pour le compteur total_profit
            actions = actions[:-1]

            for k, l in enumerate(db.price[i:]):

                if l <= (cost_maximum - total_cost):

                    actions.append(db['name'][k + i])
                    total_profit += db['benefits'][k + i]
                    total_cost += l

    return print("OPTIMIZED \n", "liste", actions, "\n" "Coût total :", total_cost,
                 "\nProfit total :", round(total_profit, 2),
                 "\n")



optimize(create_df())
