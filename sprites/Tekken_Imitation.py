from pico2d import *
Screen_width,Screen_Height = 1200,800

open_canvas(1200,800)
BackGround1 = load_image('BackGrounds1.png')
Jin = load_image('Jin.png')

running = True
x,y=200,200
frame = 0

while running:
  clear_canvas()
  BackGround1.draw(Screen_width // 2 + 1,Screen_Height // 2 + 1)
  Jin.clip_draw(frame*100,0,50,140,x,y)
  frame = (frame+1) % 8
  update_canvas()


  delay(0.1)

close_canvas()
