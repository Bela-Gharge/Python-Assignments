import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)
    og_accuracy = accuracy_score(Y_test,y_pred)*100
    print(f"Original Accuracy : {og_accuracy}")


    ## Creating new column 
    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
    X1 = df.drop(columns=["FinalResult"])
    Y1 = df["FinalResult"]
    
    X1_train,X1_test,Y1_train,Y1_test = train_test_split(X1,Y1,test_size=0.2,random_state=42)
    
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X1_train,Y1_train)
    
    y1_pred = model.predict(X1_test)
    new_accuracy = accuracy_score(Y1_test,y1_pred)*100
    print(f"New Accuracy : {new_accuracy}")



if __name__ == "__main__":
    main()