from pico2d import *
import pygame
Screen_width,Screen_Height = 1200,800

open_canvas(800,600)
BackGround1 = load_image('BackGrounds1.png')
Jin = load_image('Jin.png')
kazuya = load_image('Kazuya_reverse.png')
life_bar = load_image('life bar.png')
title_image = load_image('title_image.png')

running = True
x,y=200,200
x2,y2=600,200
frame_1 = 0
frame_2 = 0
kick_1 , punch_1 = 0, 0
kick_2,punch_2 = 0,0
dir_x_1,dir_x_2= 0,0
space ,k = False,False
num_5 ,num_2 = False, False
defence_1 ,defence_2 = False,False
title = True
game_result = None
total_time = 10
start_ticks = pygame.time.get_ticks()

#키보드 입력 함수
def handle_events():
  global running
  global x,y
  global dir_x_1,dir_x_2
  global space
  global k
  global defence_1,defence_2
  global num_5
  global num_2
  global title
  events = get_events()
  for event in events:
    if event.type == SDL_QUIT:
      running = False
    elif event.type == SDL_KEYDOWN:
      if event.key == SDLK_ESCAPE:
        running = False
      elif event.key == SDLK_d:
        dir_x_1 += 1
      elif event.key == SDLK_a:
        dir_x_1 -= 0.5
        defence_1 = True
      elif event.key == SDLK_SPACE:
        space = True
      elif event.key == SDLK_k:
        k = True
      elif event.key == SDLK_LEFT:   #두 번째 객체
        dir_x_2 -= 1
      elif event.key == SDLK_RIGHT:
        dir_x_2 +=0.6
        defence_2 = True
      elif event.key == SDLK_5:
        num_5 = True
      elif event.key == SDLK_2:
        num_2 = True
      #elif event.key == SDLK_KP_5:
        #num_5 = True
      elif event.key == SDLK_RETURN:
        title = False




    elif event.type == SDL_KEYUP:
      if event.key == SDLK_d:
        dir_x_1 -= 1
      elif event.key == SDLK_a:
        dir_x_1 += 0.5
        defence_1 = False
      elif event.key == SDLK_LEFT:
        dir_x_2 += 1
      elif event.key == SDLK_RIGHT:
        dir_x_2 -= 0.6
        defence_2 = False


#def display_time(time):
  #txt_timer = game_font.render(f"Time:{time}",True,Black)
  #screen.blit(txt_timer,(600,500))

while running:
  clear_canvas()

  handle_events()
  if title == True:
    title_image.draw(400,300)
  elif title == False:
    BackGround1.draw(Screen_width // 2 + 1,Screen_Height // 2 + 1)
    life_bar.draw(400,500)
    x += dir_x_1 * 10
    x2 += dir_x_2 * 10
    frame_1 = (frame_1 + 1) % 4
    frame_2 = (frame_2 + 1) % 6

    if space == False and k == False and defence_1 == False:
      Jin.clip_draw(frame_1 * 160, 2580, 100, 140, x, y)
    elif space == True:
      Jin.clip_draw((punch_1)*170, 1220, 115, 140, x, y)
      punch_1 = (punch_1 + 1) % 4
      if punch_1 == 3:
        space = False
    elif k == True:
      Jin.clip_draw((kick_1 * 170 )+ 630, 1220, 130, 160, x, y)
      kick_1 = (kick_1 + 1) % 5
      if kick_1 == 4:
        k = False
    elif space == False and k == False and defence_1 == True:
      Jin.clip_draw(640, 80, 130, 100, x, y)

    if num_5 == False and num_2 == False and defence_2 == False:
      kazuya.clip_draw((frame_2 * 142)+830, 2520, 120, 140, x2, y2)
    elif num_5 ==True:
      kazuya.clip_draw((punch_2) * 142+1120, 1000, 120, 140, x2, y2)
      punch_2 = (punch_2 + 1) % 3
      if punch_2 == 0:
        num_5 = False
    elif num_2 == True:
      kazuya.clip_draw((kick_2) * 142+0,1000,120,140,x2,y2)
      kick_2 = (kick_2 + 1) % 4
      if kick_2 == 0:
        num_2 = False
    elif defence_2 == True:
      kazuya.clip_draw(0, 250, 120, 140, x2, y2)

    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000
    #display_time(total_time - int(elapsed_time))

    if total_time - int(elapsed_time) <= 0:
      running = False


  #pygame.display.update()
  update_canvas()





  delay(0.1)

close_canvas()
