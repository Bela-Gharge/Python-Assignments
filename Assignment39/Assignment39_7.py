import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier(max_depth=3,random_state=42)
    model.fit(X_train,Y_train)

    student_info = pd.DataFrame([
        {
        "StudyHours" : 6,
        "Attendance" : 85,
        "PreviousScore" : 66,
        "AssignmentsCompleted" : 7,
        "SleepHours" : 7,
        }
    ])

    pred = model.predict(student_info)
    result = lambda pred : "Pass(1)" if pred[0] == 1 else "Fail(0)"

    print(f"Result is : {result(pred)} ")

if __name__ == "__main__":
    main()
