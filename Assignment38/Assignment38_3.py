import pandas as pd

def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    avg_study = df["StudyHours"].mean()
    print(f"Average Study Hours : {avg_study}")

    print(f"Average Attendance : {df.Attendance.mean()}")

    max_score = df["PreviousScore"].max()
    print(f"Maximum Previous Score : {max_score}")

    print(f"Minimum Sleep : {df.SleepHours.min()}")

if __name__ == "__main__":
    main()