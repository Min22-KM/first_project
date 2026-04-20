### CordinationPicker.py
from pynput import mouse

saved_points = []

def on_click(x, y, button, pressed):
    if pressed:
        saved_points.append((x, y))
        print(f"클릭한 위치 저장: ({x}, {y})")

        # 예: 2개 클릭하면 region 자동 출력
        if len(saved_points) == 2:
            x1, y1 = saved_points[0]
            x2, y2 = saved_points[1]
            region = (x1, y1, x2 - x1, y2 - y1)
            print(f"\n 저장된 region: {region}")

# 마우스 클릭 리스너 실행
with mouse.Listener(on_click=on_click) as listener:
    print("클릭하면 좌표가 저장됩니다. Ctrl+C로 종료")
    listener.join()
