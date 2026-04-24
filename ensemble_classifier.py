import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, 
f1_score, confusion_matrix
def run_model():
    try:
        print("\n========= MACHINE LEARNING EXECUTION =========")
        # USER INPUTS
        file_path = input("\nEnter dataset file path: ")
        n_trees = int(input("Enter number of decision trees: "))
        impurity = input("Enter impurity measure (gini/entropy): ").lower()
        test_size = float(input("Enter test size (0.1 to 0.3 recommended): "))
        k_value = int(input("Enter K value for K-Fold: "))
        # STEP 1
        print("\n[STEP 1] Loading Dataset...")
        data = pd.read_csv(file_path)
        print("Dataset Loaded Successfully")
        print("Shape:", data.shape)
        # STEP 2
        print("\n[STEP 2] First 5 Rows:")
        print(data.head())
        # STEP 3
        data.isnull().sum()
        # STEP 4
        print("\n[STEP 4] Splitting Features and Target...")
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        print("X shape:", X.shape)
        print("y shape:", y.shape)
        # STEP 5
        print("\n[STEP 5] Encoding categorical data...")
        X = pd.get_dummies(X)
        print(" Encoded shape:", X.shape)
        # STEP 6
        print("\n[STEP 6] Train-Test Split...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        print("Train size:", X_train.shape)
        print("Test size :", X_test.shape)
        # STEP 7
        print("\n[STEP 7] Creating Model...")
        model = RandomForestClassifier(
            n_estimators=n_trees,
            criterion=impurity,
            random_state=42
        )
        print("Model ready")
        # STEP 8
        print("\n[STEP 8] K-Fold Cross Validation...")
        kf = KFold(n_splits=k_value, shuffle=True, random_state=42)
        cv_scores = cross_val_score(model, X_train, y_train, cv=kf)
        for i, score in enumerate(cv_scores):
            print(f"Fold {i+1}: {score}")
        print("Mean CV Score:", np.mean(cv_scores))
        # STEP 9
        print("\n[STEP 9] Training Model...")
        model.fit(X_train, y_train)
        # STEP 10
        print("\n[STEP 10] Predicting...")
        y_pred = model.predict(X_test)
        # STEP 11
        print("\n[STEP 11] Evaluation Metrics...")
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', 
zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', 
zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        print("\n========= RESULTS =========")
        print("Accuracy :", accuracy)
        print("Precision:", precision)
        print("Recall   :", recall)
        print("F1 Score :", f1)
        # STEP 12: CONFUSION MATRIX
        print("\n[STEP 12] Confusion Matrix...")
        cm = confusion_matrix(y_test, y_pred)
        print("\nConfusion Matrix:")
        print(cm)
    except Exception as e:
        print("\nERROR:", e)
if __name__ == "__main__":
    run_model()
