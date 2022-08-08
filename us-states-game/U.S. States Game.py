from multiprocessing.connection import answer_challenge
import pandas as pd
import turtle

screen = turtle.Screen()
screen.setup(width= 730, height= 500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup()
turtle.goto(0,0)
screen.tracer(0)
state_df = pd.read_csv("50_states.csv")
correct_ans_list = []
while len(correct_ans_list) < 50:
    answer = screen.textinput(f"Guess the state, {len(correct_ans_list)}/50 correct answer(s)","What's another state's name?").title()
    if answer == "Exit":
        missing_states = []
        for state in state_df.state.to_list():
            if state not in correct_ans_list:
                missing_states.append(state)
        pd.DataFrame({"Missing states":missing_states}).to_csv("Missing_States.csv")
        break
    data = state_df[state_df["state"] == answer].to_dict()
    # print(data)
    correct_ans_list.append(answer)
    if data["state"] != {}:
        cor = [count for count, state in data["state"].items()]
        turtle.goto(data['x'][cor[0]], data['y'][cor[0]])
        turtle.write(answer,align="center")
        turtle.goto(0,0)
        screen.update()