import pandas as pd 
df = pd.read_csv(r"C:\Users\SOC-S-608\Desktop\dataat.csv")
df['attendance_date'] = pd.to_datetime(df['dataat'])
def find_consecutive_absences(df):
    results = []
    for student_id, group in df.groupby('student_id'):
        group = group.sort_values('dataat')
    
absent_days = group[group['status'] == 'Absent']
streak_start = None
streak_end = None
for i in range(1, len(absent_days)):
    if absent_days['attendance_date'].iloc[i] - absent_days['attendance_date'].iloc[i-1] == pd.Timedelta(days=1):
        if streak_start is None:
                    streak_start = absent_days['attendance_date'].iloc[i-1]
                    streak_end = absent_days['attendance_date'].iloc[i]
    else:
        if streak_start is not None and (streak_end - streak_start).days > 2:
                    results.append({
                        'student_id': student_id,
                        'absence_start_date': streak_start,
                        'absence_end_date': streak_end
                    })
streak_start = None
streak_end = None