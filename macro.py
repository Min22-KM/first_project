import pyautogui
import time
import numpy as np
from pynput import keyboard

# ------------------- 설정 -------------------
region = (23, 157, 648, 611)

# 🎯 색 여러 개 (초록 + 파랑 + 보라)
target_colors = [
    np.array([79, 166, 52]),   # 초록
    np.array([83, 176, 249]),  # 파랑
    np.array([120, 105, 230])  # 보라
]

tolerance = 40  # ⭐ 핵심 (크게 잡기)
confirm_button = (750, 655)

running = False

# ------------------- 색 찾기 -------------------
def find_color(img):
    for color in target_colors:
        diff = np.abs(img - color)
        mask = np.all(diff <= tolerance, axis=2)

        coords = np.argwhere(mask)
        if coords.size > 0:
            y, x = coords.mean(axis=0).astype(int)
            return x, y
    return None


# ------------------- 매크로 -------------------
def run_macro():
    screenshot = pyautogui.screenshot(region=region)
    img = np.array(screenshot.convert("RGB"))

    pos = find_color(img)

    if pos:
        x, y = pos
        real_x = region[0] + x
        real_y = region[1] + y

        pyautogui.click(real_x, real_y)
        time.sleep(0.05)
        pyautogui.click(*confirm_button)

        print("좌석 클릭 성공")
    else:
        print("못 찾음")


# ------------------- 키 제어 -------------------
def on_press(key):
    global running
    try:
        if key == keyboard.Key.f8:  # ⭐ ALT 말고 F8 사용
            running = not running
            print("실행 상태:", running)
    except:
        pass


# ------------------- 실행 -------------------
print("F8 누르면 시작/정지")

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if running:
        run_macro()
        time.sleep(0.1)
