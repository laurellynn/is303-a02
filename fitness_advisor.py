'''
Laurel Lynn
IS 303 - A02

Fitness Advisor
This program recomends a fitness plan based 
fitness level and goals.

Inputs: 
- Customer name (string)
- Fitness level (beginner, intermediate, advanced) (string)
- Desired goal (weight loss, strength, endurance) (string)

Processes: 
- Validate fitness level (must be one of the options)'
- Validate desired goal (one of above options)
- Determines which fitness plan will be best based on level

Outputs: 
- Print customer name, fitness level, goal, and suggested plan
- Print error message if any input is invalid
'''

decision_a = "Beginning Weight Loss Plan: 30 minutes of cardio 3 days a week, 30 minutes of strength trianing 2 days a week. "

decision_b = "Beginning Strength Training Plan: 30 minutes of weights 3 days a week, 15 minutes of cardio 2 days a week. "

decision_c = "Beginning Endurance Training Plan: 5 minutes running, 5 minutes walking repeated 3 times 5 days a week. "

decision_d = "Intermediate Weight Loss Plan: 45 minutes of cardio 3 days a week, 30 minutes of strength trianing 2 days a week. "

decision_e = "Intermediate Strength Training Plan: 45 minutes of weights 3 days a week, 15 minutes of cardio 2 days a week. "

decision_f = "Intermediate Endurance Training Plan: 10 minutes running, 5 minutes walking repeated 4 times 5 days a week. "

decision_g = "Advanced Weight Loss Plan: 60 minutes of cardio 3 days a week, 30 minutes of strength trianing 2 days a week. "

decision_h = "Advanced Strength Training Plan: 60 minutes of weights 3 days a week, 15 minutes of cardio 2 days a week. "

decision_i = "Advanced Endurance Training Plan: 15 minutes running, 5 minutes walking repeated 5 times 5 days a week. "

beginner_plans = "What is your fitness goal? A. Weight loss B. Strength C. Endurance "
intermediate_plans = "What is your fitness goal? D. Weight loss E. Strength F. Endurance "
advanced_plans = "What is your fitness goal? G. Weight loss H. Strength I. Endurance "


customer_name = input("Please enter your name: ")
fitness_level = input("What is your desired fitness level: Beginner, Intermediate, or Advanced? Choose one. ")
fitness_level = fitness_level.capitalize()
if fitness_level == "Beginner":
    goal = input(beginner_plans)
elif fitness_level == "Intermediate":
    goal = input(intermediate_plans)
elif fitness_level == "Advanced":
    goal = input(advanced_plans)
else:
    print("Please enter one of the above choices.")

if goal == "A" or goal == "B" or goal == "C":
    print("Weight Loss")
elif goal == "D" or goal == "E" or goal == "F":
    print("Strength Training")
elif goal == "G" or goal == "H" or goal == "I":
    print("Endurance Training") 
else:
    print("Please type the selected capital letter for your goal, not the word.")



print(f"{customer_name} | Fitness Level: {fitness_level} | Goal: {goal}")
if fitness_level == "Beginner" and goal == "A":
    print(decision_a)
elif fitness_level == "Beginner" and goal == "B":
    print(decision_b)
elif fitness_level == "Beginner" and goal == "C":
    print(decision_c)
elif fitness_level == "Intermediate" and goal == "D":
    print(decision_d)
elif fitness_level == "Intermediate" and goal == "E":
    print(decision_e)
elif fitness_level == "Intermediate" and goal == "F":
    print(decision_f)
elif fitness_level == "Advanced" and goal == "G":
    print(decision_g)
elif fitness_level == "Advanced" and goal == "H":
    print(decision_h)
elif fitness_level == "Advanced" and goal == "I":
    print(decision_i)



