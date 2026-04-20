import pyautogui
import time
import numpy as np
from pynput import keyboard

# ------------------- 설정 -------------------
REGION = (23, 157, 648, 611)
TARGET_COLOR = np.array([79, 166, 52])  # RGB
TOLERANCE = 5
CONFIRM_BUTTON = (750, 655)

RUNNING = False

# ------------------- 핵심 로직 -------------------

def find_color_position(img, target_color, tol):
    """
    numpy 기반 색상 탐색 (빠름)
    """
    diff = np.abs(img - target_color)
    mask = np.all(diff <= tol, axis=2)

    coords = np.argwhere(mask)
    if coords.size == 0:
        return None

    # 중앙 좌표 반환 (더 정확한 클릭)
    y, x = coords.mean(axis=0).astype(int)
    return x, y


def run_macro():
    screenshot = pyautogui.screenshot(region=REGION)
    img = np.array(screenshot.convert("RGB"))

    pos = find_color_position(img, TARGET_COLOR, TOLERANCE)

    if pos:
        x, y = pos
        real_x = REGION[0] + x
        real_y = REGION[1] + y

        pyautogui.moveTo(real_x, real_y, duration=0.02)
        pyautogui.click()
        time.sleep(0.05)

        pyautogui.click(*CONFIRM_BUTTON)

        print(f"[SUCCESS] 클릭: ({real_x}, {real_y})")
        return True
    else:
        print("[INFO] 색상 못 찾음")
        return False


# ------------------- 키보드 제어 -------------------

def on_press(key):
    global RUNNING

    try:
        if key == keyboard.Key.alt_l:
            RUNNING = not RUNNING
            print(f"매크로 상태: {'ON' if RUNNING else 'OFF'}")

    except Exception as e:
        print("오류:", e)


def start_loop():
    print("⌨️ ALT(왼쪽)로 시작/정지 토글, Ctrl+C로 종료")

    while True:
        if RUNNING:
            run_macro()
            time.sleep(0.1)  # 너무 빠르면 오히려 불안정
        else:
            time.sleep(0.1)


# ------------------- 실행 -------------------

listener = keyboard.Listener(on_press=on_press)
listener.start()

start_loop()
