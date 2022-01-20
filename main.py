import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game')

# in Turtle we can load an image as a new shape:
image = './blank_states_img.gif'
screen.addshape(image)

# this shape can now be used by Turtle
turtle.shape(image)

answer_state = screen.textinput(
    title='Guess the State', prompt='Enter Your Guess:').title()

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

correct_guesses, score = [], 0

for state in all_states:
    # exit out of a game
    if(answer_state == 'Exit'):
        break
    if(answer_state in all_states):
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        # get the row of the state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, 16)
        correct_guesses.append(answer_state)
        score = len(correct_guesses)
        answer_state = screen.textinput(
            title=f'Guess the State {score}/50', prompt='Enter Your Guess:')
    elif(answer_state in correct_guesses):
        answer_state = screen.textinput(
            title=f'Guess the State {score}/50', prompt='Enter Your Guess:')
    else:
        answer_state = screen.textinput(
            title=f'Guess the State {score}/50', prompt='Enter Your Guess:')

# states that player wasn't able to guess will be created into a CSV file
missed_states = []
for state in all_states:
    if state_data.items() not in all_states:
        missed_states.append(state)

missed_states_DF = pandas.DataFrame(missed_states)

missed_states_CSV = missed_states_DF.to_csv('missed_states.csv')

screen.exitonclick()
