import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)
data = pd.read_csv("50_states.csv")
states = data["state"].tolist()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State",
                                    prompt="What's another state's name?")

    if answer_state.title() == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_state:
                missing_states.append(state)
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missingStates.txt")
        break
    if answer_state.title() in states:
        guessed_state.append(answer_state.title())
        state_d = answer_state.title()
        coordinates = data[data["state"] == answer_state.title()]
        print(coordinates)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(coordinates.x), int(coordinates.y))
        t.write(answer_state.title(), align="center", font=("Courier", 10, "normal"))

