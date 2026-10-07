import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def main():
    ## Step 1 : Load the dataset
    df = pd.read_csv("student_performance_ml.csv")


    ## Step 2 : Separate X and y columns
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]


    ## Step 3 : Split and train the data
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train,Y_train)

    new_students = pd.DataFrame({
        "StudyHours" : [2,3,4,9,11],
        "Attendance" : [67,35,90,75,50],
        "PreviousScore": [55, 40, 78, 85, 92],
        "AssignmentsCompleted" : [5,6,8,9,9] , 
        "SleepHours" : [5,6,4,7,8],
    })


    new_students["PredictedResult"] = model.predict(new_students)

    # 4. Map binary predictions (0/1) to human-readable labels (Fail/Pass)
    new_students["Status"] = new_students["PredictedResult"].map(
        {1: "Pass", 0: "Fail"}
    )

    print("--- Q4 Predictions ---")
    print(new_students)


if __name__ == "__main__":
    main()