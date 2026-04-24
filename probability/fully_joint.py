import itertools

# Step 1: Get features
def get_features():
    features = input("Enter feature names (space-separated, positive only): ").split()
    return features


# Step 2: Generate all combinations (positive + negative)
def generate_combinations(features):
    combos = []
    for values in itertools.product([True, False], repeat=len(features)):
        combo = []
        for i in range(len(features)):
            if values[i]:
                combo.append(features[i])
            else:
                combo.append("not_" + features[i])
        combos.append(tuple(combo))
    return combos


# Step 3: Input probabilities
def input_probabilities(combos):
    joint = {}
    print("\nEnter joint probabilities:")
    
    for combo in combos:
        val = float(input(f"P{combo} = "))
        joint[combo] = val
    
    return joint

def display_table(joint, features):
    print("\n--- Joint Probability Table ---")

    # Assuming order: [Burglary, Earthquake, Alarm]
    A = features[0]   # Row variable
    B = features[1]   # Inner column
    C = features[2]   # Outer column

    A_vals = [A, "not_" + A]
    B_vals = [B, "not_" + B]
    C_vals = [C, "not_" + C]

    # Header
    print(f"\n{'':15}| {C_vals[0]:^30} | {C_vals[1]:^30}")
    print("-" * 80)
    print(f"{'':15}| {B_vals[0]:^15} {B_vals[1]:^15} | {B_vals[0]:^15} {B_vals[1]:^15}")
    print("-" * 80)

    # Rows
    for a in A_vals:
        print(f"{a:15}|", end=" ")

        for c in C_vals:
            for b in B_vals:
                key = (a, b, c)
                val = joint.get(key, 0)
                print(f"{val:<15}", end=" ")

            print("|", end=" ")

        print()


# Step 5: Query function
def query_probability(joint, query, given=None):
    numerator = 0
    denominator = 0

    for key, prob in joint.items():
        key_set = set(key)

        # numerator
        if all(q in key_set for q in query):
            if given is None or all(g in key_set for g in given):
                numerator += prob

        # denominator
        if given:
            if all(g in key_set for g in given):
                denominator += prob

    if given is None:
        return numerator

    if denominator == 0:
        return 0

    return numerator / denominator


# MAIN
features = get_features()
combinations = generate_combinations(features)
joint = input_probabilities(combinations)

display_table(joint, features)

while True:
    print("\n===== MENU =====")
    print("1. P(A)")
    print("2. P(A | B)")
    print("3. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        q = input("Enter query (e.g., Burglary or not_Burglary): ").split()
        print("Result:", query_probability(joint, q))

    elif ch == 2:
        q = input("Enter A (query): ").split()
        g = input("Enter B (given): ").split()
        print("Result:", query_probability(joint, q, g))

    elif ch == 3:
        break