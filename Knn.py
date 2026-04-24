import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
# ---------------- DISTANCE FUNCTIONS ---------------- #
def euclidean(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
def manhattan(x1, x2):
    return np.sum(np.abs(x1 - x2))
def chebyshev(x1, x2):
    return np.max(np.abs(x1 - x2))
def distance(metric, x1, x2):
    if metric == 1:
        return euclidean(x1, x2)
    elif metric == 2:
        return manhattan(x1, x2)
    else:
        return chebyshev(x1, x2)
# ---------------- PRINT MANUAL TABLE ---------------- #
def print_manual_table(X_train, y_train):
    print("\n===== TRAINING DATA TABLE =====")
    header = ["Sample"] + [f"F{i+1}" for i in range(len(X_train[0]))] + 
["Class"]
    print("{:<8}".format(header[0]), end="")
    for h in header[1:]:
        print("{:<10}".format(h), end="")
    print()
    for i, (x, y) in enumerate(zip(X_train, y_train)):
        print("{:<8}".format(i+1), end="")
        for val in x:
            print("{:<10}".format(val), end="")
        print("{:<10}".format(y))
# ---------------- KNN FUNCTION ---------------- #
def knn(X_train, y_train, X_test, k, metric, weighted=False, mode="manual"):
    predictions = []
    for t, test in enumerate(X_test):
        if mode == "manual":
            print("\n===================================")
            print(f"Test Sample {t+1}: {test}")
            print("===================================")
        dist_list = []
        if mode == "manual":
            print("\nStep 1: Distance Computation")
        for i in range(len(X_train)):
            d = distance(metric, test, X_train[i])
            dist_list.append((d, y_train[i]))
            if mode == "manual":
                print(f"Train {i+1}: Class={y_train[i]}, Distance={d:.4f}")
        dist_list.sort(key=lambda x: x[0])
        if mode == "manual":
            print("\nStep 2: Sorted Distances")
            for d, c in dist_list:
                print(f"Distance={d:.4f}, Class={c}")
        neighbors = dist_list[:k]
        if mode == "manual":
            print(f"\nStep 3: Top {k} Nearest Neighbors")
            for d, c in neighbors:
                print(f"Distance={d:.4f}, Class={c}")
        # -------- UNWEIGHTED -------- #
        if not weighted:
            if mode == "manual":
                print("\nStep 4: Unweighted Voting")
            votes = Counter([c for _, c in neighbors])
            if mode == "manual":
                for cls, cnt in votes.items():
                    print(f"Class {cls}  Votes = {cnt}")
            prediction = votes.most_common(1)[0][0]
        # -------- WEIGHTED -------- #
        else:
            weight_sum = {}
            for d, c in neighbors:
                w = 1 / (d ** 2 + 1e-9)
                weight_sum[c] = weight_sum.get(c, 0) + w
            if mode == "manual":
                print("\nWeighted Voting Results:")
                for cls, wsum in weight_sum.items():
                    print(f"Class {cls}  Weight Sum = {wsum:.4f}")
            prediction = max(weight_sum, key=weight_sum.get)
        if mode == "manual":
            print("Final Prediction:", prediction)
        predictions.append(prediction)
    return np.array(predictions)
# ---------------- MANUAL MODE ---------------- #
def manual_mode():
    n = int(input("Enter number of training samples: "))
    f = int(input("Enter number of features: "))
    X_train, y_train = [], []
    print("\nEnter Training Data")
    for i in range(n):
        X_train.append(list(map(float, input(f"Features {i+1}: ").split())))
        y_train.append(input("Class label: "))
    print_manual_table(X_train, y_train)
    k = int(input("\nEnter k value: "))
    X_test = np.array([list(map(float, input("Enter test data: ").split()))])
    print("\nDistance Metric\n1. Euclidean\n2. Manhattan\n3. Chebyshev")
    metric = int(input("Choice: "))
    print("\n===== UNWEIGHTED KNN =====")
    knn(np.array(X_train), np.array(y_train), X_test, k, metric,
        weighted=False, mode="manual")
    print("\n===== WEIGHTED KNN =====")
    knn(np.array(X_train), np.array(y_train), X_test, k, metric,
        weighted=True, mode="manual")
# ---------------- CSV MODE ---------------- #
def csv_mode():
    #path = input("Enter CSV file path: ")
    path =  r"\\172.16.16.220\CSE-Student\UG\23BCS\A\19805\SEM6\ci\EX3\
diabetes.csv"
    path =  r"\\172.16.16.220\CSE-Student\UG\23BCS\A\19805\SEM6\ci\EX3\
diabetes.csv"
    df = pd.read_csv(path)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    train_percent = float(input("Enter training percentage (e.g. 70): "))
    train_size = train_percent / 100
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42
    )
    k = max(1, int(0.1 * len(X_train)))
    print("\nTraining Samples:", len(X_train))
    print("Testing Samples :", len(X_test))
    print("k (10% of training data):", k)
    print("\nDistance Metric\n1. Euclidean\n2. Manhattan\n3. Chebyshev")
    metric = int(input("Choice: "))
    # -------- UNWEIGHTED -------- #
    print("\n===== UNWEIGHTED KNN =====")
    y_pred = knn(X_train, y_train, X_test, k, metric,
                 weighted=False, mode="csv")
    print("\nPerformance Metrics (Unweighted)")
    print("Accuracy :", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred, average='macro'))
    print("Recall   :", recall_score(y_test, y_pred, average='macro'))
    print("F1 Score :", f1_score(y_test, y_pred, average='macro'))
    print("\nConfusion Matrix (Unweighted)")
    print(confusion_matrix(y_test, y_pred))
    # -------- WEIGHTED -------- #
    print("\n===== WEIGHTED KNN (1 / D) =====")
    y_pred_w = knn(X_train, y_train, X_test, k, metric,
                   weighted=True, mode="csv")
    print("\nPerformance Metrics (Weighted)")
    print("Accuracy :", accuracy_score(y_test, y_pred_w))
    print("Precision:", precision_score(y_test, y_pred_w, average='weighted'))
    print("Recall   :", recall_score(y_test, y_pred_w, average='weighted'))
    print("F1 Score :", f1_score(y_test, y_pred_w, average='weighted'))
    print("\nConfusion Matrix (Weighted)")
    print(confusion_matrix(y_test, y_pred_w))
# ---------------- MAIN MENU ---------------- #
def main():
    while True:
        print("\n====== KNN MENU ======")
        print("1. Manual Input")
        print("2. CSV File Input")
        print("3. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            manual_mode()
        elif ch == 2:
            csv_mode()
        elif ch == 3:
            print("Program Exited")
            break
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
    main()
