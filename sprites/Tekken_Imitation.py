from pico2d import *
Screen_width,Screen_Height = 1200,800

open_canvas(800,600)
BackGround1 = load_image('BackGrounds1.png')
Jin = load_image('Jin.png')
kazuya = load_image('Kazuya.png')

running = True
x,y=200,200
x2,y2=600,200
frame_1 = 0
frame_2 = 0
kick_1 , punch_1 = 0, 0
punch_2 = 0
dir_x_1,dir_x_2= 0,0
space ,k = False,False
num_5 = False
defence_1 ,defence_2 = False,False
#키보드 입력 함수
def handle_events():
  global running
  global x,y
  global dir_x_1,dir_x_2
  global space
  global k
  global defence_1,defence_2
  global num_5
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
      elif event.key == SDLK_KP_5:
        num_5 = True




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


while running:
  clear_canvas()

  handle_events()
  BackGround1.draw(Screen_width // 2 + 1,Screen_Height // 2 + 1)
  x += dir_x_1 * 10
  x2 += dir_x_2 * 10
  frame_1 = (frame_1 + 1) % 4
  frame_2 = (frame_2 + 1) % 6

  if space == False and k == False and defence_1 == False:
    Jin.clip_draw(frame_1 * 160, 2580, 100, 140, x, y)
  elif space == True:
    Jin.clip_draw((punch_1-1)*170, 1220, 115, 140, x, y)
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

  if num_5 == False and defence_2 == False:
    kazuya.clip_draw(frame_2 * 142, 2520, 120, 140, x2, y2)
  elif num_5 ==True:
    kazuya.clip_draw((punch_2-1) * 142, 1000, 120, 140, x2, y2)
    punch_2 = (punch_2 + 1) % 3
    if punch_2 == 2:
      num_5 = False
  elif defence_2 == True:
    kazuya.clip_draw(1570, 250, 120, 140, x2, y2)


  update_canvas()





  delay(0.1)

close_canvas()
