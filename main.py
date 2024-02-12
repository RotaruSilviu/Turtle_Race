from turtle import Turtle, Screen
import random

### Cream un intrerupator pentru while loop.
is_race_on = False
screen = Screen()
###Setam latime si inaltimea ferestrei care se deschide.
screen.setup(500, 400)
###Cream un pop up care sa scrie userul care testoasa o sa castige.
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()
###O lista cu culorile testoasei.
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
###Pozitiile testoaselor in ordinea in care o sa apara pe ecran.
y_positions = [-100, -60, -20, 20, 60, 100]
###O lista goala in care o sa se append testoasele care se creaza in for loopde mai jos.
all_turtles = []

####Cream un for loop cu diferite caracteristici pentru fiecare testoasa.
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    ### Se alege o culoare din lista de culori.
    new_turtle.color(colors[turtle_index])
    ### Sa nu scrie testoasele.
    new_turtle.penup()
    ### Pozitia de start a fiecarei testoase utilizand lista y_pozitions si cu ajutorul turtle index
    # alegem pozitia din lista respectiva
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    ###Se adauga la lista all_turtles fiecare testoasa creata.
    all_turtles.append(new_turtle)

### Daca userul face un pariu atunci incepe cursa.
if user_bet:
    is_race_on = True

###Cursa propriuzisa
while is_race_on:
    ###Se ia fiecare testoasa din lista all_turtles.
    for turtle in all_turtles:
        ###Daca testoasela ajung la final se opreste cursa.
        if turtle.xcor() > 230:
            is_race_on = False
            ###Se verifica care testoasa e castigatoare.
            winning_color = turtle.pencolor().lower()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        ###Fiecare testoasa o sa mearga la fiecare loop o distanta random.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
