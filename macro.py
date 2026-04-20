import pyautogui
import time
import numpy as np
from pynput import keyboard

# ------------------- 설정 -------------------
REGION = (23, 157, 648, 611)
TARGET_COLOR = np.array([83, 176, 249])  # RGB
TOLERANCE = 8
CONFIRM_BUTTON = (750, 655)

RUNNING = False


# ------------------- 색상 탐색 -------------------
def find_color_position(img, target_color, tol):
    diff = np.abs(img - target_color)
    mask = np.all(diff <= tol, axis=2)

    coords = np.argwhere(mask)
    if coords.size == 0:
        return None

    # 평균 좌표 → 중앙 클릭
    y, x = coords.mean(axis=0).astype(int)
    return x, y


# ------------------- 매크로 실행 -------------------
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
    else:
        print("[INFO] 색상 못 찾음")


# ------------------- 키보드 제어 -------------------
def on_press(key):
    global RUNNING

    try:
        # 🔥 ALT 대신 안정적인 키 사용 (F8)
        if key == keyboard.Key.f8:
            RUNNING = not RUNNING
            print(f"[STATE] {'ON' if RUNNING else 'OFF'}")

    except Exception as e:
        print("[ERROR]", e)


# ------------------- 메인 루프 -------------------
def main():
    print("F8 키로 시작/정지 토글 | Ctrl+C 종료")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        if RUNNING:
            run_macro()
            time.sleep(0.1)
        else:
            time.sleep(0.1)


# ------------------- 실행 -------------------
if __name__ == "__main__":
    main()
