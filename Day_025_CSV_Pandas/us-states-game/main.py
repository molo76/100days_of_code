import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_guessed = 0

data = pd.read_csv('50_states.csv')
states = data.state.to_list()
print(states)

while states_guessed < 50:
    answer_state = screen.textinput(title=f'{states_guessed}/50 - Guess the state', prompt='Enter a state').title()
    print(answer_state)
    if answer_state in states:
        states_guessed += 1
        x_cor = data[data.state == answer_state].x.item()
        y_cor = data[data.state == answer_state].y.item()
        print(x_cor)
        print(y_cor)


turtle.mainloop()

# screen.exitonclick()