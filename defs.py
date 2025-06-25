import pygame
import random
import vars
import preloads
import classes
import entities


def print_text(message, x, y, font_color=(255, 255, 255), font_type='./assets/Roboto-Regular.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    preloads.screen.blit(text, (x, y))


def cls(icons):
    if icons.get('sunstrike') != None:
        icons.__delitem__('sunstrike')
    if icons.get('tornado') != None:
        icons.__delitem__('tornado')
    if icons.get('coldsnap') != None:
        icons.__delitem__('coldsnap')
    if icons.get('forgespirit') != None:
        icons.__delitem__('forgespirit')
    if icons.get('chaosmeteor') != None:
        icons.__delitem__('chaosmeteor')
    if icons.get('emp') != None:
        icons.__delitem__('emp')
    if icons.get('deafenningblast') != None:
        icons.__delitem__('deafenningblast')
    if icons.get('alacrity') != None:
        icons.__delitem__('alacrity')
    if icons.get('ghostwalk') != None:
        icons.__delitem__('ghostwalk')
    if icons.get('icewall') != None:
        icons.__delitem__('icewall')


def create_start_spells():
    vars.glblt.used_abilities = list()
    vars.glblt.waiting_abilities = list(preloads.abilities.keys())
    for i in range(0, 3):
        new_ability = random.choice(vars.glblt.waiting_abilities)
        vars.glblt.used_abilities.append(new_ability)
        vars.glblt.waiting_abilities.remove(new_ability)


def end_result():
    cls(vars.glblt.icons)
    print_text('Game Over', 75, 40)
    print_text('Total time: ' +
               str(((100*vars.glblt.timeOver)//1)/100), 50, 100)
    print_text('Wrong invokes: ' +
               str(vars.glblt.r_false), 45, 150)
    print_text('Keys pressed: ' +
               str(vars.glblt.pressed_keys_count), 45, 200)
    print_text('Press SPACE', 55, 260)
    print_text('to restart', 75, 285)


def keep_giving_skills():
    if vars.glblt.proccing:
        if len(vars.glblt.icons) < 3:
            in_moment = list(vars.glblt.icons.keys())
            if len(vars.glblt.icons) > 0:
                if vars.glblt.used_abilities[0] not in in_moment:
                    vars.glblt.icons[vars.glblt.used_abilities[0]] = classes.Icon(
                        preloads.abilities[vars.glblt.used_abilities[0]], 0, 0
                    )
                if vars.glblt.used_abilities[1] not in in_moment:
                    vars.glblt.icons[vars.glblt.used_abilities[1]] = classes.Icon(
                        preloads.abilities[vars.glblt.used_abilities[1]], 100, 0
                    )
                if vars.glblt.used_abilities[2] not in in_moment:
                    vars.glblt.icons[vars.glblt.used_abilities[2]] = classes.Icon(
                        preloads.abilities[vars.glblt.used_abilities[2]], 200, 0
                    )
            else:
                vars.glblt.icons[vars.glblt.used_abilities[0]] = classes.Icon(
                    preloads.abilities[vars.glblt.used_abilities[0]], 0, 0
                )
                vars.glblt.icons[vars.glblt.used_abilities[1]] = classes.Icon(
                    preloads.abilities[vars.glblt.used_abilities[1]], 100, 0
                )
                vars.glblt.icons[vars.glblt.used_abilities[2]] = classes.Icon(
                    preloads.abilities[vars.glblt.used_abilities[2]], 200, 0
                )


def game_over_checking():
    for i in vars.glblt.icons:
        vars.glblt.icons[i].blit()
        vars.glblt.icons[i].move()
        if vars.glblt.icons[i].rect.y > 300:
            pygame.display.update()
            preloads.bg.fill((0, 0, 0))
            pygame.mixer.music.pause()
            vars.glblt.game_over = True
            vars.glblt.timeOver = vars.glblt.time


def show_spheres():
    coords = 0
    for i in vars.glblt.spheresVisual:
        preloads.screen.blit(i, (coords, 400))
        coords += 100


def game_menu():
    entities.button_easy.draw(preloads.screen)
    entities.button_medium.draw(preloads.screen)
    entities.button_hard.draw(preloads.screen)
    pass


def start_game(speed):
    vars.restart(speed)
    pygame.mixer.music.load('./assets/music.mp3')
    pygame.mixer.music.play()
    create_start_spells()


def invoke():
    vars.glblt.pressed_keys_count += 1
    res = None
    spheres = vars.glblt.spheres.copy()
    spheres.sort()
    if ['exort', 'wex', 'wex'] == spheres:
        res = 'alacrity'
    if ['exort', 'exort', 'wex'] == spheres:
        res = 'chaosmeteor'
    if ['quas', 'quas', 'quas'] == spheres:
        res = 'coldsnap'
    if ['exort', 'quas', 'wex'] == spheres:
        res = 'deafenningblast'
    if ['wex', 'wex', 'wex'] == spheres:
        res = 'emp'
    if ['exort', 'exort', 'quas'] == spheres:
        res = 'forgespirit'
    if ['quas', 'quas', 'wex'] == spheres:
        res = 'ghostwalk'
    if ['exort', 'quas', 'quas'] == spheres:
        res = 'icewall'
    if ['exort', 'exort', 'exort'] == spheres:
        res = 'sunstrike'
    if ['quas', 'wex', 'wex'] == spheres:
        res = 'tornado'
    if vars.glblt.icons.get(res) != None:
        vars.glblt.icons.__delitem__(res)
        vars.glblt.score += 1
        new_ability = random.choice(vars.glblt.waiting_abilities)
        for i in range(0, 3):
            if vars.glblt.used_abilities[i] == res:
                vars.glblt.used_abilities[i] = new_ability
        vars.glblt.waiting_abilities.remove(new_ability)
        vars.glblt.waiting_abilities.append(res)
        preloads.invoke.play()
    else:
        vars.glblt.r_false += 1


def button_checking():
    if not vars.glblt.show_records:
        mouse_pos = pygame.mouse.get_pos()
        entities.button_easy.check_hover(mouse_pos)
        entities.button_medium.check_hover(mouse_pos)
        entities.button_hard.check_hover(mouse_pos)
        entities.button_records.check_hover(mouse_pos)
        entities.button_easy.draw(preloads.screen)
        entities.button_medium.draw(preloads.screen)
        entities.button_hard.draw(preloads.screen)
        entities.button_records.draw(preloads.screen)
    pass


def save():
    if vars.glblt.speed == 2:
        vars.glblt.best_easy = max(
            int(vars.glblt.best_easy), vars.glblt.score)
    if vars.glblt.speed == 3:
        vars.glblt.best_medium = max(
            int(vars.glblt.best_medium), vars.glblt.score)
    if vars.glblt.speed == 4:
        vars.glblt.best_hard = max(
            int(vars.glblt.best_hard), vars.glblt.score)
    with open('records.txt', 'w') as file:
        file.writelines([str(vars.glblt.best_easy)+'\n',
                         str(vars.glblt.best_medium)+'\n',
                         str(vars.glblt.best_hard)+'\n'])


def show_records():
    easy = vars.glblt.best_easy
    medium = vars.glblt.best_medium
    hard = vars.glblt.best_hard
    preloads.screen.fill((0, 0, 0))

    # Заголовок
    title = preloads.font.render("Top scores:", True, (255, 255, 255))
    preloads.screen.blit(
        title, (preloads.width // 2 - title.get_width() // 2, 100))

    # Отображение рекордов
    for i, mode, score in [(1, 'Easy', easy), (2, 'Medium', medium), (3, 'Hard', hard)]:
        score_text = preloads.font.render(
            f"{mode}: {score} scores", True, (255, 255, 255))
        preloads.screen.blit(
            score_text, (preloads.width // 2 - score_text.get_width() // 2, 180 + i * 40))
    entities.button_back.draw(preloads.screen)
    pass
