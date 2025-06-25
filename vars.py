import preloads


class glblt:
    fps = 30
    time = 0
    score = 0
    r_false = 0
    pressed_keys_count = 0
    inbossik = True
    proccing = False
    game_over = False
    spheres = list()
    spheresVisual = list()
    icons = dict()
    used_abilities = list()
    waiting_abilities = list(preloads.abilities.keys())
    timeOver = 0
    speed = 1
    show_records = False
    best_easy = 0
    best_medium = 0
    best_hard = 0


def restart(speed):
    glblt.fps = 30
    glblt.time = 0
    glblt.score = 0
    glblt.r_false = 0
    glblt.game_over = False
    glblt.proccing = True
    glblt.pressed_keys_count = 0
    glblt.spheres = list()
    glblt.spheresVisual = list()
    glblt.icons = dict()
    glblt.speed = speed
