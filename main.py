import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from sys import exit
from playsound import playsound

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car = CarManager()
player = Player()
scoreboard = Scoreboard()
scoreboard.update_score() 

screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_Car()
    
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()
        car.level_up()
        
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            playsound("Gameover.mp3", block=False)
            time.sleep(7)
            exit()