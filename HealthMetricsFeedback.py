from Hub import hubmain
import openai
import UserHealthData


HR = UserHealthData.weekly_HR[-1]
sleepscore = UserHealthData.weekly_sleepscore[-1]
HRV = UserHealthData.weekly_HRV[-1]
STV = UserHealthData.weekly_STV[-1]
SPO2 = UserHealthData.weekly_SPO2[-1]
active = UserHealthData.weekly_active[-1]

def average(list):

    average = sum(list) / len(list)

    return average

def is_value_close_to_average(list, value, threshold=5):
    average = sum(list) / len(list)
    difference = abs(value - average)
    return difference <= threshold

if is_value_close_to_average(UserHealthData.weekly_HR, HR):
    print(f"Your resting heart rate of {HR} bpm is within the normal range.")

elif average(UserHealthData.weekly_HR) > HR:
    print(f"Your resting heart rate of {HR} bpm is lower than the normal range, if this persists please try contacting a medical professional")

elif average(UserHealthData.weekly_HR) < HR:
    print(f"Your resting heart rate of {HR} bpm is higher than the normal range, this could be due to fatigue or lack of sleep, if this persists please try contacting a medical professional")

if is_value_close_to_average(UserHealthData.weekly_HRV, HRV):
    print(f"Your HRV of {HRV} is within this normal range, but individual factors should still be taken into account.")

else:
    print(f"Your HRV of {HRV} is out of your normal range, if this persists please try contacting a medical professional.")

if sleepscore > 70:
    print(f"Your sleep score of {sleepscore} suggests that you had a good nights rest.")

else:
    print(f"Your sleep score of {sleepscore} suggests that you didn't have an optimal sleep.")

if abs(STV) > 5:
    print(f"Your {STV} suggests that your skin tempreture is different than your body's average, please consult a medical professional.")

if SPO2 < 95:
    print("Your Oxygen Levels are quite low, please consult a medical professional if these problems persist")

if active < 15:
    print("Your activity levels are quite low, WHO recommends about 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous-intensity aerobic activity per week.")


#prompt = f"A persons resting heart rate is {HR}, sleep score is {sleepscore}, HRV is {HRV}, skin temperature variance is {STV}, SPO2 level is {SPO2}, and has {active} active minutes, provide normal ranges for each"

