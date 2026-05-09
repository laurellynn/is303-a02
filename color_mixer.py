'''
Laurel Lynn
IS 303 - A02

Color Mixer
This program tells the user what color they will get if they mix two primary colors together. 
User will enter two primary colors and system will tell what it will result in. 
Error will occur if user enters a color that is not primary.

Inputs: 
- user inputs color number one
- user inputs color number two

Processes: 
- validate first color
- validate second color
- determine resulted color

Outputs: 
- Output the two colors that will be mixed together
- produce the newly created color
- reply with an error if invalid colors are entered
'''
color_a = "red"
color_b = "purple"
color_c = "orange"
color_d = "blue"
color_f = "green"
color_g = "yellow"

color_a = color_a.capitalize()
color_b = color_b.capitalize()
color_c = color_c.capitalize()
color_d = color_d.capitalize()
color_f = color_f.capitalize()
color_g = color_g.capitalize()          

first_color = input("Please enter a primary color: red/yellow/blue ")

if first_color != "red" and first_color != "yellow" and first_color != "blue":
    print("Color not accepted. Please start over and enter a primary color: red/yellow/blue ")
else:
    second_color = input("Please enter your second primary color: red/yellow/blue ") 
    verify_colors = print(f"The colors you entered were {first_color} and {second_color}. ")
    print(f"Mixing {first_color} and {second_color} will result in: ")

#reds
    if first_color == "red" and second_color == "red":
        print(color_a)
    elif first_color == "red" and second_color == "blue":
        print(color_b)
    elif first_color == "red" and second_color == "yellow":
        print(color_c)
    elif first_color == "blue" and second_color == "blue":
        print(color_d)
    elif first_color == "blue" and second_color == "red":
        print(color_b)
    elif first_color == "blue" and second_color == "yellow":
        print(color_f)
    elif first_color == "yellow" and second_color == "yellow":
        color_g = "yellow"
        print(color_g)
    elif first_color == "yellow" and second_color == "red":
        print(color_c)
    elif first_color == "yellow" and second_color == "blue":
        print(color_f)
    else:
        print("Color not accepted. Please start over and enter a primary color: red/yellow/blue ")
    

