import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    # 2. Train-test split & model training
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, Y_train)

    # 3. Visualize the decision tree
    plt.figure(figsize=(12, 8))
    plot_tree(
        model,
        feature_names=X.columns,
        class_names=["Fail", "Pass"],
        filled=True,
        rounded=True,
    )
    plt.title("Decision Tree Structure")
    plt.show()

if __name__ == "__main__":
    main()