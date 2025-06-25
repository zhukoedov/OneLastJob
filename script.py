import pygame
import defs
import entities
import vars
import preloads


def inbossik_start():
    defs.create_start_spells()
    with open('records.txt', 'r') as file:
        recs = file.read()
        list_rec = recs.split('\n')
        vars.glblt.best_easy = int(list_rec[0])
        vars.glblt.best_medium = int(list_rec[1])
        vars.glblt.best_hard = int(list_rec[2])
    while vars.glblt.inbossik:
        preloads.screen.fill((0, 0, 0))
        if vars.glblt.proccing:
            preloads.clock.tick(vars.glblt.fps)
            vars.glblt.time += 0.033
            if not vars.glblt.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            vars.glblt.spheres.append('quas')
                            vars.glblt.spheresVisual.append(
                                preloads.quas)
                            vars.glblt.pressed_keys_count += 1
                        if event.key == pygame.K_w:
                            vars.glblt.spheres.append('wex')
                            vars.glblt.spheresVisual.append(
                                preloads.wex)
                            vars.glblt.pressed_keys_count += 1
                        if event.key == pygame.K_e:
                            vars.glblt.spheres.append('exort')
                            vars.glblt.spheresVisual.append(
                                preloads.exort)
                            vars.glblt.pressed_keys_count += 1
                        if len(vars.glblt.spheresVisual) > 3:
                            vars.glblt.spheres.pop(0)
                            vars.glblt.spheresVisual.pop(0)
                        if event.key == pygame.K_r:
                            defs.invoke()

                preloads.screen.blit(preloads.bg, (0, 0))
                defs.print_text(str(vars.glblt.score), 135, 550)
                pygame.draw.line(preloads.screen, (255, 0, 0),
                                 (0, 398), (300, 398))

                defs.keep_giving_skills()

                # show spheres
                defs.show_spheres()

                # Game over checking
                defs.game_over_checking()

            # Game over
            else:
                defs.end_result()
                defs.save()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            vars.glblt.proccing = False
                            break
                        if event.key == pygame.K_SPACE:
                            defs.start_game(vars.glblt.speed)
        else:  # proccing = False
            defs.game_menu()
            defs.button_checking()
            m_pos = pygame.mouse.get_pos()
            click = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.button
                    if entities.button_easy.is_clicked(m_pos, click):
                        defs.start_game(2)
                    if entities.button_medium.is_clicked(m_pos, click):
                        defs.start_game(3)
                    if entities.button_hard.is_clicked(m_pos, click):
                        defs.start_game(4)
                    if entities.button_records.is_clicked(m_pos, click):
                        vars.glblt.show_records = True
            if vars.glblt.show_records:
                entities.button_back.check_hover(m_pos)
                if entities.button_back.is_clicked(m_pos, click):
                    vars.glblt.show_records = False
                defs.show_records()

        pygame.display.update()
