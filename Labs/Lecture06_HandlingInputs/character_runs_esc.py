from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    # fill here
    pass


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.01)

close_canvas()

