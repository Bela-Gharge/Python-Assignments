import pandas as pd

def main():
    Datapath = "student_performance_ml.csv"

    ## 1 
    df = pd.read_csv(Datapath)
    print(f"Total number of students are {len(df)}")


    ## 2
    pass_count = (df["FinalResult"] == 1).sum()
    print(f"Total number of students who passed are : {pass_count}")

    ## 3
    fail_count = (df["FinalResult"] == 0).sum()
    print(f"Total number of students who failed are : {fail_count}")
    

if __name__ == "__main__":
    main()