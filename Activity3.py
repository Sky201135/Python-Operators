print("Enter Marks Obtained in 8 subjects:")
math = int(input("Math: "))
chemistry = int(input("Chemistry: "))
physics = int(input("Physics: "))
bangla = int(input("Bangla: "))
english = int(input("English: "))
indivaidual_society = int(input("Individual and Society: "))
art = int(input("Art: "))
physical_health_education = int(input("Physical Health Education: "))


sum = (math + chemistry + physics + bangla + english + indivaidual_society + art + physical_health_education)

print ("The percentage of all the subject's marks are:")
perc = (sum / 800) * 100
print(perc)