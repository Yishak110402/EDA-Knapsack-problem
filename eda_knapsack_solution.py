import random

def knapsack_value(solution, items, weight_limit):
    
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += items[i]['weight']
            if total_weight > weight_limit:  # Invalid solution
                return 0, total_weight
            total_value += items[i]['value']
    return total_value, total_weight


def eda_knapsack(items, weight_limit, population_size=20, generations=100):
    
    n = len(items)
    probabilities = [0.5] * n  # Start with a uniform distribution for each item

    best_solution = None
    best_value = 0

    for generation in range(generations):
        # Generate population based on probabilities
        population = []
        for _ in range(population_size):
            solution = [1 if random.random() < probabilities[i] else 0 for i in range(n)]
            population.append(solution)
        
        # Evaluate population
        evaluated = [(solution, knapsack_value(solution, items, weight_limit)) for solution in population]
        evaluated = [(sol, val) for sol, (val, _) in evaluated if val > 0]  # Keep only valid solutions
        evaluated.sort(key=lambda x: x[1], reverse=True)  # Sort by value
        
        if not evaluated:
            continue
        
        # Update best solution
        if evaluated[0][1] > best_value:
            best_solution = evaluated[0][0]
            best_value = evaluated[0][1]
        
        # Select elite solutions
        top_k = 5
        elites = [sol for sol, _ in evaluated[:top_k]]
        
        # Update probabilities
        for i in range(n):
            probabilities[i] = sum(sol[i] for sol in elites) / top_k
        print(probabilities)
    
    return best_solution, best_value


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

solution, value = eda_knapsack(items, weight_limit)
print(f"Best solution: {solution}")
print(f"Maximum value: {value}")
