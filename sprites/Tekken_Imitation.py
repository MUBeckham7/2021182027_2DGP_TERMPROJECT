from pico2d import *
Screen_width,Screen_Height = 1200,800

open_canvas(800,600)
BackGround1 = load_image('BackGrounds1.png')
Jin = load_image('Jin.png')

running = True
x,y=200,200
frame = 0
punch = 0
dir_x=0
space = False
#키보드 입력 함수
def handle_events():
  global running
  global x,y
  global dir_x
  global space
  events = get_events()
  for event in events:
    if event.type == SDL_QUIT:
      running = False
    elif event.type == SDL_KEYDOWN:
      if event.key == SDLK_ESCAPE:
        running = False
      elif event.key == SDLK_d:
        dir_x += 1
      elif event.key == SDLK_a:
        dir_x -= 1
      elif event.key == SDLK_SPACE:
        space = True
    elif event.type == SDL_KEYUP:
      if event.key == SDLK_d:
        dir_x -= 1
      elif event.key == SDLK_a:
        dir_x += 1


while running:
  clear_canvas()

  handle_events()
  BackGround1.draw(Screen_width // 2 + 1,Screen_Height // 2 + 1)
  x += dir_x * 10
  frame = (frame+1) % 4




  if space == False:
    Jin.clip_draw(frame*160,2580,100,140,x,y)
  elif space == True:
    Jin.clip_draw(punch*170, 1220, 115, 140, x, y)
    punch = (punch + 1) % 4
    if punch == 3:
      space = False






  update_canvas()





  delay(0.1)

close_canvas()
