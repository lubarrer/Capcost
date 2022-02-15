import pandas as pd
import matplotlib.pyplot as plt
from numpy_financial import numpy_financial as npf


def annual(
    products,
    raw_materials,
    total_installed_cost,
    loan_interest,
    n_years,
    utilities,
    waste,
    credit_discount,
):
    def EAOC(product_byproduct, feed, cca, other_op_cost, op_cred):
        eaoc = -product_byproduct + feed + cca + other_op_cost - op_cred

        if eaoc < 0:
            print("Economic Potential: {:,.2f}\nProfitable!".format(eaoc))
        else:
            print("Economic Potential: {:,.2f}\nNot profitable!".format(eaoc))
            return eaoc

    def capital_cost_annuity(total_installed_cost, loan_interest, n):
        i = loan_interest
        n = n_years
        cca = total_installed_cost * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
        return cca

    def revenue(products):
        rev = 0
        for r in products["index"]:
            rev += products["Price"][r] * products["Flowrate"][r]
        return rev

    def feed(raw_materials):
        fd = 0
        for f in raw_materials["index"]:
            fd += raw_materials["Price"][f] * raw_materials["Flowrate"][f]
        return fd

    def utility_cost(utilities):
        utility_cost = 0
        for u in utilities["index"]:
            utility_cost += utilities["Price"][u] * utilities["Usage"][u]
        return utility_cost

    def credit(credit_discount):
        credit = 0
        for c in credit_discount["index"]:
            credit += credit_discount["Price"][c] * credit_discount["Usage"][c]
        return credit

    r = revenue(products)
    f = feed(raw_materials)
    cca = capital_cost_annuity(total_installed_cost, loan_interest, n_years)
    u = utility_cost(utilities)
    c = credit(credit_discount)
    w = waste
    p = r - f - cca - u - w + c
    table = pd.DataFrame(
        [
            ["Credits", "${:,.2f}".format(c)],
            ["Revenue", "${:,.2f}".format(r)],
            ["Raw materials", "-${:,.2f}".format(f)],
            ["Equipment loan", "-${:,.2f}".format(cca)],
            ["Utilities", "-${:,.2f}".format(u)],
            ["Waste Treatment", "-${:,.2f}".format(w)],
            ["Profit", "${:,.2f}".format(p)],
        ]
    )

    project_life_total = []
    n = 0
    while n < n_years:
        project_life_total.append(p)
        n += 1

    return table, project_life_total


def cash_flow(annual_cost, discount_rate):
    nd_cash_flow = []
    nd_sum = 0
    for y in annual_cost:
        nd_sum += y / 1e6
        nd_cash_flow.append(nd_sum)

    d_cash_flow = []
    d_sum = 0
    j = 0
    for y in annual_cost:
        discount = y / (1 + discount_rate) ** j
        d_sum += discount / 1e6
        d_cash_flow.append(d_sum)
        j += 1

    plt.figure(figsize=(20, 7))
    ax1 = plt.subplot(121)
    plt.plot(nd_cash_flow)
    plt.title("Non-discounted Cash Flow", fontsize=20, color="white")
    plt.xlabel("Year", fontsize=14, color="white")
    plt.ylabel("$ (Million)", fontsize=14, color="white")
    ax1.tick_params(axis="x", colors="white")
    ax1.tick_params(axis="y", colors="white")
    plt.grid(True)

    ax2 = plt.subplot(122)
    plt.plot(d_cash_flow)
    plt.title("Discounted Cash Flow", fontsize=20, color="white")
    plt.xlabel("Year", fontsize=14, color="white")
    plt.ylabel("$ (Million)", fontsize=14, color="white")
    ax2.tick_params(axis="x", colors="white")
    ax2.tick_params(axis="y", colors="white")
    plt.grid(True)
    plt.show()
