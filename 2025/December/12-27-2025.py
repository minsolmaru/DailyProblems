"""
At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
"""



def min_drinks(preferences):
    # Build drink -> customers mapping
    drink_to_customers = {}
    for customer, drinks in preferences.items():
        for drink in drinks:
            drink_to_customers.setdefault(drink, set()).add(customer)

    uncovered = set(preferences.keys())
    chosen = set()

    while uncovered:
        # Choose drink covering most uncovered customers
        best_drink = max(
            drink_to_customers,
            key=lambda d: len(drink_to_customers[d] & uncovered)
        )

        chosen.add(best_drink)
        uncovered -= drink_to_customers[best_drink]

    return len(chosen), chosen

