from pico2d import *
import random



KPU_WIDTH, KPU_HEIGHT = 1280, 1024

# 이 함수는 분석할 필요 없음. 기존 코드.
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

# 이 함수는 10개의 랜덤 위치의 화살표를 화면에 그려줌. 분석 필요 없음.
def draw_all_arrows():
    for i, p in enumerate(target_points):
        arrow.draw(p[0], p[1])
        pico2d.debug_font.draw(p[0], p[1], str(i), (255,0,0))



# 이 이후의 코드에 대한 분석하면 됨.


def update_character():
    global cx, cy
    global running_right
    global p1, p2, p3, p4
    global t
    global prev_cx

    cx = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
    cy = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

    # 다음 코드가 하는 일은?
    t += 0.001
    if t >= 1.0:
        p1, p2, p3, p4 = get_next_four_points()
        t = 0


    # 다음 코드의 목적은?
    running_right = cx > prev_cx
    prev_cx = cx


# 아래 코드는 어떤 식으로 4개의 포인트를 가져오는가?
def get_next_four_points():
    global cur_index
    start = cur_index % num_points
    end = start + 4
    points = extended_target_points[start:end]
    cur_index += 1
    return points


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# prepare images
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
running_right = True
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
prev_cx = cx
frame = 0
hide_cursor()

num_points = 10
target_points = []
for i in range(num_points):
    target_points.append((random.randint(100, KPU_WIDTH-100), random.randint(100, KPU_HEIGHT-100)))

# 아래의 코드에서, target_points[:3]을 더해서, extended_target_points를 만든 이유는?
extended_target_points = target_points + target_points[:3]
cur_index = -1

t = 0
p1, p2, p3, p4 = get_next_four_points()

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_all_arrows()
    if running_right:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, cx, cy)
    update_canvas()

    frame = (frame + 1) % 8
    update_character()

    handle_events()

close_canvas()




