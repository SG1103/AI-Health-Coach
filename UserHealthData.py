from deepface import DeepFace


name = 'Saad Golandaz'
weight = 65
height = 187
gender = "Male"


weekly_HR = (75, 74, 76, 74, 77, 76, 65)
weekly_sleepscore = (76, 82, 81, 92, 68, 76, 72)
weekly_HRV = (105, 113, 89, 108, 123, 78, 97)
weekly_STV = (-6, -3, -5, 0, 0, 3, 0)
weekly_SPO2 = (97, 98, 95, 100, 99, 97, 98)
weekly_active = (23, 156, 42, 96, 204, 62, 13)

fitness_scores = []  # Initialize an empty list to store the fitness scores

for i in range(len(weekly_HR)):
    RHR = weekly_HR[i]
    SleepScore = weekly_sleepscore[i]
    HRV = weekly_HRV[i]
    SkinTemperature = weekly_STV[i]
    SPO2 = weekly_SPO2[i]
    DailyActiveMinutes = weekly_active[i]

    Fitness_Score = (0.3 * RHR) + (0.4 * SleepScore) + (0.1 * HRV) + (0.05 * abs(SkinTemperature)) + (0.05 * SPO2) + (
                0.1 * DailyActiveMinutes)
    fitness_scores.append(Fitness_Score)  # Append the calculated fitness score to the list

print(fitness_scores)


objs = DeepFace.analyze(img_path = "img.jpg",
        actions = ['age', 'gender', 'race', 'emotion']
)

print(objs)
