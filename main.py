import os
import random
import time 
import keyboard

def Draw(row_cols, snake, x_food, y_food):

    for y in range(row_cols):
        for x in range(row_cols * 2):
            
            corodinates_match = False

            #draw snake
            for i in snake:
                if x ==  i.get('x') and y == i.get("y"):
                    print("s", end='')
                    corodinates_match = True
                

            if corodinates_match: 
                continue


            if x == 0 or y == 0 or y == row_cols - 1 or x == (row_cols * 2) - 1 :
                print("#", end="")
            
            #print food of the snake
            elif x == x_food and y == y_food:
                print("f", end='')

            else:
                print(" ", end="")

        print("")





def snake_food():
    return [ random.randint(2, 20), random.randint(2, 20) ]

row_cols = 30



def GameLoop():

    snake =  [ { "x": 10 , "y":5  } ]
    [x_food, y_food ] = snake_food()

    x_direction = 1
    y_direction = 0
    is_game_running = True


    while is_game_running:

        #clear the terminal
        os.system("cls")

        [snake, y_direction, x_direction] = Controls(snake, x_direction, y_direction)


        #check if the x and y cord of the snake is the same as the food
        if snake[0].get('x') == x_food and snake[0].get('y') == y_food:
            [x_food, y_food ] = snake_food()
        else:
            snake.pop()


        # If snake touch the walls it dies
        # these are the cord of the wall
        if snake[0].get("x") == 0 or snake[0].get("y") == 0 or snake[0].get("y") == row_cols - 1 or snake[0].get("x") == (row_cols * 2) - 1 :
            is_game_running = False
            print("Game Over")
            return

        
        Draw(row_cols, snake, x_food, y_food)


        time.sleep(0.1)





def Controls(snake, x_direction, y_direction): 

    update = { 
        "x": snake[0]["x"] + x_direction , 
        "y": snake[0]['y'] + y_direction 
        }
        
    snake = [update] + snake

    if keyboard.is_pressed('w'):
        if y_direction == 0:
            y_direction = - 1 
            x_direction = 0


    elif keyboard.is_pressed('s'):
        if y_direction == 0:
            y_direction = 1
            x_direction = 0


    elif keyboard.is_pressed('d'):
        if x_direction == 0:
            x_direction = 1
            y_direction = 0



    elif keyboard.is_pressed('a'):
        if x_direction == 0:
            x_direction = - 1
            y_direction = 0



    return [snake, y_direction, x_direction]

            






if __name__ == "__main__":
    GameLoop()