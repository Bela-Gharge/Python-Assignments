import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model = DecisionTreeClassifier(max_depth=3 , random_state=42)
    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    #----------------------------------------------------
    # Actual Accuracy
    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy is : ",accuracy*100)


    #------------------------------------------------------
    # Manunal Accuracy
    correct_acc = np.sum(y_pred==Y_test)
    total_accu = len(y_pred)

    Manual_accuracy = (correct_acc/total_accu)*100
    print("Manual Accuracy calculated is : ",Manual_accuracy)



if __name__ == "__main__":
    main()