import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']


    ## Q1
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.8,random_state=42)
    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)


    ## Q2
    y_pred = model.predict(X_test)
    print(f"Predicted Values : {y_pred}")
    print(f"Actual Values : {X_test}")

if __name__ == "__main__":
    main()