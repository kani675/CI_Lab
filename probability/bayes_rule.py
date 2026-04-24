# 🎯 Simple Bayes Rule using 2 Dice

# Helper function to check condition
def check(value, condition, target):
    if condition == "=":
        return value == target
    elif condition == ">":
        return value > target
    elif condition == "<":
        return value < target
    return False


# Function to define an event
def get_event(name):
    print(f"\n--- Define Event {name} ---")
    print("Choose type:")
    print("1. Sum of dice")
    print("2. First die")
    print("3. Second die")

    choice = int(input("Enter choice (1/2/3): "))

    if choice == 1:
        event_type = "sum"
    elif choice == 2:
        event_type = "first"
    else:
        event_type = "second"

    print("Condition (=, >, <): ")
    condition = input().strip()

    target = int(input("Enter value: "))

    return event_type, condition, target


# Main function
def bayes_dice():

    print("🎲 BAYES THEOREM (2 Dice)\n")

    # Get events
    type_a, cond_a, target_a = get_event("A")
    type_b, cond_b, target_b = get_event("B")

    total = 36
    count_A = 0
    count_B = 0
    count_A_and_B = 0
    l_A=[]
    l_B=[]
    l_AB=[]
    # Generate all outcomes
    for d1 in range(1, 7):
        for d2 in range(1, 7):

            s = d1 + d2

            # Evaluate A
            if type_a == "sum":
                A = check(s, cond_a, target_a)
            elif type_a == "first":
                A = check(d1, cond_a, target_a)
            else:
                A = check(d2, cond_a, target_a)

            # Evaluate B
            if type_b == "sum":
                B = check(s, cond_b, target_b)
            elif type_b == "first":
                B = check(d1, cond_b, target_b)
            else:
                B = check(d2, cond_b, target_b)

            # Count
            if A:
                count_A += 1
                l_A.append((d1,d2))
            if B:
                count_B += 1
                l_B.append((d1,d2))

            if A and B:
                count_A_and_B += 1
                l_AB.append((d1,d2))
                

    # Results
    print("\n📊 --- RESULTS ---")

    P_A = count_A / total
    P_B = count_B / total
    P_A_and_B = count_A_and_B / total

    print("The selected pairs for A: ",l_A)
    print(f"P(A) = {count_A}/36 = {round(P_A, 4)}")
    print("The selected pairs for B: ",l_B)
    print(f"P(B) = {count_B}/36 = {round(P_B, 4)}")
    print("The selected pairs for A and B: ",l_AB)
    print(f"P(A ∩ B) = {count_A_and_B}/36 = {round(P_A_and_B, 4)}")

    if count_A == 0:
        print("\n❌ Cannot compute P(B|A) since P(A)=0")
        return

    # Step 1: Compute P(B|A)
    P_B_given_A = count_A_and_B / count_A
    print(f"\nP(B | A) = {count_A_and_B}/{count_A} = {round    (P_B_given_A, 5)}")

    # Step 2: Apply Bayes Rule
    if P_B == 0:
        print("❌ Cannot divide by zero (P(B)=0)")
        return

    P_A_given_B = (P_B_given_A * P_A) / P_B

    print("\n📌 Using Bayes Rule:")
    print("P(A | B) = [P(B | A) * P(A)] / P(B)")

    print(f"= ({round(P_B_given_A,5)} × {round(P_A,5)}) / {round(P_B,5)}")

    print(f"= {round(P_A_given_B, 5)}")
# RUN
bayes_dice()