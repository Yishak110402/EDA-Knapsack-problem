# items = [
#     {
#         "weight": 12,
#         "value": 20
#     },
#     {
#         "weight": 10,
#         "value": 20
#     },
#     {
#         "weight": 10,
#         "value": 20
#     },
#     {
#         "weight": 10,
#         "value": 20
#     },
#     {
#         "weight": 10,
#         "value": 20
#     },
#     {
#         "weight": 10,
#         "value": 20
#     },
#     {
#         "weight": 10,
#         "value": 20
#     },
# ]
# weight_limit = 2

# def fitness(items):
#     return sum(items)

# def create_dp_table(items, weight_limit):
#     dp = [[0 for _ in range(weight_limit + 1)] for _ in range(len(items) + 1)]
#     print(dp)
    
#     for i in range(1,len(items) + 1):
#         for w in range(weight_limit + 1):
#             weight = items[i]['weight'] 
#             value = items[i]['value'] 
#             if weight <= w:
#                 dp[i][w] = max(dp[i][w], value + dp[i][w - weight])
#             else:
#                 dp[i][w] = dp[i-1][w]
    
# create_dp_table(items, weight_limit)


def knapsack(items, weight_limit):
    """
    Solves the 0/1 Knapsack Problem using dynamic programming.

    :param items: List of dictionaries, each with 'weight' and 'value'.
    :param weight_limit: Maximum weight capacity of the knapsack.
    :return: Maximum value and the list of items included in the knapsack.
    """
    n = len(items)

    # Create DP table with dimensions (len(items)+1) x (weight_limit+1), initialized to 0
    dp = [[0 for _ in range(weight_limit + 1)] for _ in range(len(items) + 1)]

    # Fill the DP table
    for i in range(1, len(items) + 1):  # Start from 1 because row 0 represents "no items"
        for w in range(weight_limit + 1):  # Include 0 to weight_limit
            weight = items[i - 1]["weight"]  # i-1 because items are 0-indexed
            value = items[i - 1]["value"]

            if weight <= w:
                # Option to include the item or not
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])
            else:
                # Can't include the item, so take the previous value
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    w = weight_limit
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # If value changed, the item was included
            selected_items.append(items[i - 1])
            w -= items[i - 1]["weight"]

    selected_items.reverse()  # Reverse to maintain original order
    return dp[n][weight_limit], selected_items


# Example usage
items = [
    {"weight": 4, "value": 10},
    {"weight": 2, "value": 4},
    {"weight": 3, "value": 7},
    {"weight": 1, "value": 2},
    {"weight": 2, "value": 6},
    {"weight": 5, "value": 3},
    {"weight": 3, "value": 9},
    {"weight": 1, "value": 1},
]
weight_limit = 7


max_value, selected_items = knapsack(items, weight_limit)
print(f"Maximum value: {max_value}")
print("Selected items:")
for item in selected_items:
    print(item)
