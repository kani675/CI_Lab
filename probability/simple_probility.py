# Rolling 2 Dice Probability
def dice_probability(target, condition):
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    total = len(outcomes)  # 36

    favorable = 0
    l=[]
    for d1, d2 in outcomes:
        s = d1 + d2

        if condition == "equal" and s == target:
            favorable += 1
            l.append((d1,d2))
        elif condition == "greater" and s > target:
            favorable += 1
            l.append((d1,d2))
        elif condition == "less" and s < target:
            favorable += 1
            l.append((d1,d2))

    probability = favorable / total

    print("\nTotal outcomes:", total)
    print("Favorable outcomes:", favorable)
    print("The chosen pairs : ",l)
    print("Probability:", round(probability, 5))


# ---- USER INPUT ----
target = int(input("Enter target sum (2–12): "))

print("Choose condition: equal / greater / less")
condition = input().lower()

dice_probability(target, condition)
