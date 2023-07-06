import play

speed = 2

play.set_backdrop('light blue')
ball = play.new_circle(
        color=(255, 204, 36), 
        x=-130, 
        y=-175, 
        radius=200, 
        border_color="black", 
        border_width=5, 
        transparency=100
    )
character = play.new_image(
        image='character.png', 
        x=-130, 
        y=60, 
        angle=0, 
        size=100, 
        transparency=100
    )

@play.repeat_forever
def do():
    if play.key_is_pressed('right', 'd'):
        character.turn(-2)
    if play.key_is_pressed('left', 'a'):
        character.turn(2)
play.start_program()