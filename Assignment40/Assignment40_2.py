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


    ## Step 4 : Test the model
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy of model : ",accuracy*100)



#------------------------------------------------------------------------
# Train the model without sleep hours 
#------------------------------------------------------------------------
    X1 = df.drop(columns = ["FinalResult","SleepHours"])
    Y1 = df["FinalResult"]    

    X1_train,X1_test,Y1_train,Y1_test = train_test_split(X1,Y1,test_size=0.2,random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X1_train,Y1_train)

    y1_pred = model.predict(X1_test)

    accuracy_new = accuracy_score(Y1_test,y1_pred)
    print("New Accuracy : ",accuracy_new*100) 

    if (accuracy_new != accuracy):
        print("Removing sleep jours does affect performance")
    else : 
        print("No change")

    

if __name__ == "__main__":
    main()