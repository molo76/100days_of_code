import turtle
import pandas as pd

FONT = ("Arial", 10, "normal")
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
states_guessed = []
states_missed = []
data = pd.read_csv('50_states.csv')
states = data.state.to_list()

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f'{len(states_guessed)}/50 - Guess the state', prompt='Enter a state').title()
    if answer_state == 'Exit':
        states_missed = [state for state in states if state not in states_guessed]
        if len(states_missed) > 0:
            output_dict = {
                'state': [],
                'x': [],
                'y': []
            }
            for state in states_missed:
                state_data = data[data.state == state]
                output_dict['state'] += [state]
                output_dict['x'] += [state_data.x.item()]
                output_dict['y'] += [state_data.y.item()]

            output_data = pd.DataFrame(output_dict)
            output_data.to_csv('missed_states.csv')
            break

    if answer_state in states:
        states_guessed.append(answer_state)
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        # My solution below, 3 lines......
        # x_cor = data[data.state == answer_state].x.item()
        # y_cor = data[data.state == answer_state].y.item()
        # state.goto(x_cor, y_cor)
        # Angela's solution, 2 lines.....nifty - I added .item() to get just the data, not the
        # pandas d_type etc:
        state_data = data[data.state == answer_state]
        state.goto(state_data.x.item(), state_data.y.item())
        state.write(answer_state, align='left', font=FONT)

if states_guessed >= 50:
    completed = turtle.Turtle()
    completed.penup()
    completed.hideturtle()
    completed.write('You completed the game. Well done!', align='center', font=("Arial", 24, "bold"))
else:
    completed = turtle.Turtle()
    completed.penup()
    completed.hideturtle()
    completed.write("You didn't complete the game, try again!", align='center', font=("Arial", 24, "bold"))

screen.exitonclick()