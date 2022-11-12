from pico2d import *
import game_state

class Timefont:
    def __init__(self):
        self.image = load_image('time_font.png')

    def update(self):
        pass

        # 기본 613,325
    def draw(self):
        if game_state.total_time-int(game_state.elapsed_time) == 100:
            self.image.clip_draw(100, 00, 20, 20, 373, 510)  ######1
            self.image.clip_draw(53, 20, 22, 20, 390, 510)######0
            self.image.clip_draw(53, 20, 22, 20, 412, 510)######0
        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 9:
            self.image.clip_draw(98,20,22,20,390,510)######9 앞자리 위치
            if (game_state.total_time-int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 8:
            self.image.clip_draw(32, 20, 22, 20, 390, 510)  ######8 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 7:
            self.image.clip_draw(80, 0, 22, 20, 390, 510)  ######7 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 6:
            self.image.clip_draw(75, 20, 22, 20, 390, 510)  ######6 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 5:
            self.image.clip_draw(-2, 0, 22, 20, 390, 510)  ######5 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 4:
            self.image.clip_draw(41, 0, 22, 20, 390, 510)  ######4 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 3:
            self.image.clip_draw(62, 0, 22, 20, 390, 510)  ######3 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 2:
            self.image.clip_draw(20, 0, 22, 20, 390, 510)  ######2 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 1:
            self.image.clip_draw(100, 0, 22, 20, 390, 510)  ######1 앞자리 위치
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 412, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 412, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 412, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 412, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 412, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 412, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 412, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 412, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 412, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 412, 510)  ######0

        if (game_state.total_time-int(game_state.elapsed_time)) // 10 == 0:
            if (game_state.total_time - int(game_state.elapsed_time)) % 10 == 9:
                self.image.clip_draw(98, 20, 22, 20, 401, 510)  ######9 뒷자리 위치
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 8:
                self.image.clip_draw(32, 20, 22, 20, 401, 510)  ######8
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 7:
                self.image.clip_draw(80, 0, 22, 20, 401, 510)  ######7
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 6:
                self.image.clip_draw(75, 20, 22, 20, 401, 510)  ######6
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 5:
                self.image.clip_draw(-2, 0, 22, 20, 401, 510)  ######5
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 4:
                self.image.clip_draw(41, 0, 20, 20, 401, 510)  ######4
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 3:
                self.image.clip_draw(62, 0, 20, 20, 401, 510)  ######3
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 2:
                self.image.clip_draw(20, 0, 22, 20, 401, 510)  ######2
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 1:
                self.image.clip_draw(100, 0, 18, 20, 401, 510)  ######1
            elif (game_state.total_time - int(game_state.elapsed_time)) % 10 == 0:
                self.image.clip_draw(53, 20, 22, 20, 401, 510)  ######0