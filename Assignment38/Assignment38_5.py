import pandas as pd

def main():
    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)

    pass_students = df[df["FinalResult"] == 1]
    fail_students = df[df["FinalResult"] == 0]

    print("Pass Students Average Study Hours : ",pass_students["StudyHours"].mean())
    print("Fail Students Average Study Hours : ",fail_students["StudyHours"].mean())

    print("Pass Students Average Attendace : ",pass_students["Attendance"].mean())
    print("Fail Students Average Attendace : ",fail_students["Attendance"].mean())

    ## Group by function
    ## df.groupby("FinalResult")[["StudyHours","Attendance"]].mean()
                        
    # Students with higher study hours have better FinalResult
    # Students with better attendance have better peerformance
    # Therefore both features improve the FinalResult

if __name__ == "__main__":
    main()