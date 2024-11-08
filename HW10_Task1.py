import pulp


if __name__ == '__main__':

    model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

    lemonade = pulp.LpVariable('lemonade', 0, cat='Integer')
    juice = pulp.LpVariable('juice', 0, cat='Integer')

    model += pulp.lpSum([lemonade, juice]), "Maximize_production"

    model += (2 * lemonade + 1* juice <= 100, "Water_constraint")
    model += (1 * lemonade <= 50, "Sugar_constraint")
    model += (1* lemonade <= 30, "Juice_constraint")
    model += (2 * juice <= 40, "Puree_constraint")

    model.solve()

    print(f"Status: {model.status}")
    print(f"Lemonade production: {lemonade.value()}")
    print(f"Juice production: {juice.value()}")
    print(f"Maximum Number of Products = {model.objective.value()}")
