import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)

    counts = df["FinalResult"].value_counts()
    percentage = df["FinalResult"].value_counts(normalize=True)*100

    pass_count = counts.get(1,0)
    print(f"Pass Student : {pass_count}")

    fail_count = counts.get(0,0)
    print(f"Fail Student : {fail_count}")

    pass_students = percentage.get(1,0)
    print(f"Percent of pass students : {pass_students}")

    fail_students = percentage.get(0,0)
    print(f"Percentage of fail students : {fail_students}")


    print("Therefore Dataset is balanced")
     

if __name__ == "__main__":
    main()