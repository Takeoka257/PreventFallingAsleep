import pyautogui
from time import sleep, time
import datetime
import math

def move_mouse():
    ''' マウスポインタを中央付近で移動させる
    '''
    (display_w, display_h) = pyautogui.size()
    center_x = display_w / 2
    center_y = display_h / 2
    distance_x = display_w / 4
    distance_y = display_h / 4

    pyautogui.moveTo(0, center_y)                    # マウスポインタを画面左下へ移動
    pyautogui.click()

    pyautogui.moveTo(center_x, center_y)                    # マウスポインタを画面中央へ移動
    pyautogui.move(distance_x, -distance_y, duration=1)     # マウスポインタを画面中央右上へ移動
    pyautogui.moveTo(center_x, center_y, duration=1)        # マウスポインタを画面中央へ移動
    pyautogui.move(-distance_x, distance_y, duration=1)     # マウスポインタを画面中央左下へ移動
    pyautogui.moveTo(center_x, center_y, duration=1)        # マウスポインタを画面中央へ移動

    pyautogui.moveTo(0, center_y)                    # マウスポインタを画面左下へ移動
    pyautogui.click()
    pyautogui.moveTo(center_x, center_y)                    # マウスポインタを画面中央へ移動

def is_mouse_moved(position_new, position_old):
    ''' マウス移動判定
    '''
    threshold_move_distance = 32        # 動いたと判定する距離
    moved = False
    dif_x = position_new.x - position_old.x
    dif_y = position_new.y - position_old.y 
    distance = math.sqrt((dif_x * dif_x) + (dif_y * dif_y))
    if distance >= threshold_move_distance:
        moved = True
    return moved

def main():
    wait_min = 1                                            # 待機時間[分]
    time_start = time()                                     # 開始時刻
    mouse_position_start = pyautogui.position()             # マウス位置取得

    # ここをずっとループ
    while(True):
        # マウス操作判定
        mouse_position_now = pyautogui.position()           # マウス位置取得
        if is_mouse_moved(mouse_position_now,mouse_position_start):
            mouse_position_start = pyautogui.position()     # マウス位置取得
            now_time = datetime.datetime.now().strftime('%H:%M:%S') 
            print(F'{now_time} 移動したと判定 ')
            time_start = time()
        else:
            # 時間経過判定
            time_now = time()
            time_elapsed = int(time_now - time_start)
            now_time = datetime.datetime.now().strftime('%H:%M:%S') 
            print(F'{now_time}  {time_elapsed}秒経過')      # 動作中であることを確認する時間経過表示
            if(time_elapsed >= (wait_min * 60)):            # 指定時間経過
                print(F'{wait_min}分経過したのでマウスを自動操作')
                move_mouse()                                # マウス移動操作
                time_start = time()

        # 負荷かけないよう10秒待機
        sleep(10)

main()
