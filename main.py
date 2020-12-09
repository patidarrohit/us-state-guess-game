import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
guessed_state = []

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

while len(guessed_state) < 50:
    answer = turtle.textinput(title=f"{len(guessed_state)}/50 states Correct", prompt="What's the another state name?").title()
    if answer == 'Exit':
        missing_states = [state for state in states if state not in guessed_state]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer in states and answer not in guessed_state:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


#screen.exitonclick()
