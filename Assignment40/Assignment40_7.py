import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    random_states = [0,10,42]

    for rs in random_states:
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=rs)
        model = DecisionTreeClassifier(random_state=rs)
        model.fit(X_train,Y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,y_pred)
        print(f"Accuracy of model{rs} : {accuracy*100}")
    

if __name__ == "__main__":
    main()