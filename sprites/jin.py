from pico2d import *






class Jin:
    def add_event(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): #소년이 스스로 이벤트를 처리할 수 있게
        # evnet는 키 이벤트 ..이것을 내부 RD로 변환
        if (event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q=[]
        self.cur_state =IDLE
        self.cur_state.enter(self,None)

    def update(self):
        self.cur_state.do(self)

        if self.q: #q에 뭔가 들어있다면
            event = self.q.pop()    #이벤트를 가져오고
            self.cur_state.exit(self)   #현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산하고
            self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)