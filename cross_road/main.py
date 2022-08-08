import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("pink")
screen.setup(width=600, height=600)
screen.tracer(0)

new_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_player.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
     
    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(new_player) < 20:
            game_is_on = False
    #Detect level up
    if new_player.level_up():
        new_player.go_to_start()
        car_manager.level_up_speed()
        scoreboard.increase_level()
        
scoreboard.game_over()
screen.exitonclick()