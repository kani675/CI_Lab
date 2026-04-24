# DECISION TREE CLASSIFIER
import math
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
def entropy(data):
    total = len(data)
    counts = Counter(data)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent
def gini(data):
    total = len(data)
    counts = Counter(data)
    g = 1
    for count in counts.values():
        p = count / total
        g -= p ** 2
    return g
def gain(dataset, attribute, target, criterion):
    target_values = [row[target] for row in dataset]
    if criterion == "entropy":
        parent = entropy(target_values)
        print(f"\nParent Entropy = {parent:.4f}")
    else:
        parent = gini(target_values)
        print(f"\nParent Gini = {parent:.4f}")
    values = set(row[attribute] for row in dataset)
    weighted = 0
    for val in values:
        subset = [row[target] for row in dataset if row[attribute] == val]
        weight = len(subset) / len(dataset)
        if criterion == "entropy":
            m = entropy(subset)
            print(f"Entropy({attribute}={val}) = {m:.4f}")
        else:
            m = gini(subset)
            print(f"Gini({attribute}={val}) = {m:.4f}")
        weighted += weight * m
    gain_value = parent - weighted
    print(f"{criterion.capitalize()} Gain({attribute}) = {gain_value:.4f}")
    return gain_value
def build_tree(dataset, attributes, target, criterion):
    target_values = [row[target] for row in dataset]
    # If all target values same  leaf node
    if len(set(target_values)) == 1:
        return target_values[0]
    # If no attributes left  majority class
    if not attributes:
        return Counter(target_values).most_common(1)[0][0]
    gains = {}
    print("\nEvaluating attributes:")
    for attr in attributes:
        gains[attr] = gain(dataset, attr, target,criterion)
    best_attr = max(gains, key=gains.get)
    print(f"\nSelected Best Attribute: {best_attr}")
    tree = {best_attr: {}}
    values = set(row[best_attr] for row in dataset)
    for val in values:
        subset = [row for row in dataset if row[best_attr] == val]
        remaining_attrs = [a for a in attributes if a != best_attr]
        tree[best_attr][val] = build_tree(subset, remaining_attrs, target, 
criterion)
    return tree
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "->", tree)
        return
    for attr, branches in tree.items():
        for val, subtree in branches.items():
            print(f"{indent}{attr} = {val}")
            print_tree(subtree, indent + "   ")
def find_root_node(dataset, attributes, target, criterion):
    print("\n===== ROOT NODE SELECTION =====")
    gains = {}
    for attr in attributes:
        gains[attr] = gain(dataset, attr, target, criterion)
    root = max(gains, key=gains.get)
    print("\nGAIN SUMMARY:")
    for attr, g in gains.items():
        print(f"{attr} : {g:.4f}")
    print(f"\nROOT NODE SELECTED {root}")
    return root
def print_manual_table(dataset, attributes, target):
    print("\n===== DATASET TABLE =====")
    headers = attributes + [target]
    for h in headers:
        print(f"{h:<15}", end="")
    print()
    for row in dataset:
        for h in headers:
            print(f"{row[h]:<15}", end="")
        print()
def manual_mode(criterion):
    attributes = input("Enter attribute names (comma separated): ").split(",")
    attributes = [a.strip() for a in attributes]
    target = input("Enter target class column name: ")
    n = int(input("Enter number of records: "))
    dataset = []
    print("\nEnter data as comma-separated values")
    print(",".join(attributes) + "," + target)
    for i in range(n):
        values = input(f"Row {i + 1}: ").split(",")
        row = {}
        for j, attr in enumerate(attributes):
            row[attr] = values[j].strip()
        row[target] = values[-1].strip()
        dataset.append(row)
    # PRINT TABLE
    print_manual_table(dataset, attributes, target)
    # ROOT NODE ONLY
    find_root_node(dataset, attributes, target, criterion)
def csv_mode(criterion):
    #path = input("Enter CSV file path: ")
    target = input("Enter target column name: ")
    path= r"\\172.16.16.220\CSE-Student\UG\23BCS\A\19805\SEM6\ci\EX4\
playtennis.csv"
    df = pd.read_csv(path)
    X = df.drop(columns=[target])
    y = df[target]
    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = LabelEncoder().fit_transform(X[col])
    if y.dtype == 'object':
        y = LabelEncoder().fit_transform(y)
    train_percent = float(input("Enter training percentage (e.g. 70): "))
    train_size = train_percent / 100
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42
    )
    model = DecisionTreeClassifier(criterion=criterion)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\nMODEL PERFORMANCE:")
    print("Accuracy :", accuracy_score(y_test, y_pred))
    print(f"Precision: {precision_score(y_test, y_pred, average='macro', 
zero_division=0):.4f}")
    print(f"Recall   : {recall_score(y_test, y_pred, average='macro', 
zero_division=0):.4f}")
    print(f"F1 Score : {f1_score(y_test, y_pred, average='macro', 
zero_division=0):.4f}")
    print("\nCONFUSION MATRIX:")
    print(confusion_matrix(y_test, y_pred))
def main():
    while True:
        print("\n===== DECISION TREE MENU =====")
        print("1. Manual Input (Table + Root Node)")
        print("2. CSV Input (Training % + Confusion Matrix)")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '3':
            print("Exiting...")
            break
        print("\nChoose Splitting Criterion:")
        print("1. Entropy")
        print("2. Gini")
        c = input("Enter choice: ")
        criterion = "entropy" if c == '1' else "gini"
        if choice == '1':
            manual_mode(criterion)
        elif choice == '2':
            csv_mode(criterion)
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
