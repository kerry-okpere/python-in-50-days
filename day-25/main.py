import turtle
import pandas

screen = turtle.Screen()
screen.title('USA')

image = 'day-25/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("day-25/50_states.csv")

game_is_on = True
while game_is_on:
    answer = screen.textinput(title="Guess the state", prompt="name a state in random order")
    current_state = states_data[states_data['state'] == answer]

    if (not current_state.y.empty): 
        y = current_state.y.to_list()[0]
        x = current_state.x.to_list()[0]
        state = current_state.state.to_list()[0]
        print(x, y)

        new_turtle = turtle.Turtle()
        new_turtle.color('black')
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.write(f"{state}", font=("Courier", 12, "normal"))

screen.exitonclick()