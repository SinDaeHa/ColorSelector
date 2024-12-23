import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
import colorsys

def rgb_to_cmyk(r, g, b):
    # RGB 값을 0~1 사이 값으로 변환
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    k = 1 - max(r, g, b)
    if k < 1:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    else:
        c = m = y = 0
    return int(c * 100), int(m * 100), int(y * 100), int(k * 100)

def choose_color():
    # 색상 선택 대화상자 열기
    color_code = colorchooser.askcolor(title="Select a color")
    if color_code:
        rgb_color, hex_color = color_code
        if rgb_color and hex_color:
            r, g, b = rgb_color
            # HSV 변환
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            h = int(h * 360)
            s = int(s * 100)
            v = int(v * 100)

            # CMYK 변환
            c, m, y, k = rgb_to_cmyk(r, g, b)

            # UI 업데이트
            rgb_label.config(text=f"선택한 색상 (RGB): {int(r)}, {int(g)}, {int(b)}")
            hex_label.config(text=f"선택한 색상 (Hex): {hex_color}")
            hsv_label.config(text=f"선택한 색상 (HSV): {h}°, {s}%, {v}%")
            cmyk_label.config(text=f"선택한 색상 (CMYK): {c}%, {m}%, {y}%, {k}%")
            color_display.config(bg=hex_color)

def reset_color():
    # 모든 레이블 초기화 및 미리보기 색상 초기화
    rgb_label.config(text="선택한 색상 (RGB): ")
    hex_label.config(text="선택한 색상 (Hex): ")
    hsv_label.config(text="선택한 색상 (HSV): ")
    cmyk_label.config(text="선택한 색상 (CMYK): ")
    color_display.config(bg="white")

# GUI 초기화
root = tk.Tk()
root.title("Color Selector")

choose_button = tk.Button(root, text="색상 선택", command=choose_color)
choose_button.grid(row=0, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="초기화", command=reset_color)
reset_button.grid(row=0, column=1, padx=10, pady=10)

rgb_label = tk.Label(root, text="선택한 색상 (RGB): ")
rgb_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

hex_label = tk.Label(root, text="선택한 색상 (Hex): ")
hex_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

hsv_label = tk.Label(root, text="선택한 색상 (HSV): ")
hsv_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

cmyk_label = tk.Label(root, text="선택한 색상 (CMYK): ")
cmyk_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

color_display = tk.Label(root, text="색상 미리보기", bg="white", width=20, height=10)
color_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()


""" 
키워드 색상 추천 기능
import webcolors

color_keywords = {
    "하늘": "skyblue",
    "바다": "blue",
    "숲": "forestgreen",
    "불": "red",
    "해": "yellow",
    "흙": "brown",
    "밤": "navy",
    "구름": "lightgray"
}

def get_color_by_keyword(keyword):
    if keyword in color_keywords:
        color_name = color_keywords[keyword]
        color_rgb = webcolors.name_to_rgb(color_name)
        return color_name, color_rgb
    else:
        return None, None
keyword = input("색상을 추천받고 싶은 키워드를 입력하세요: ")

color_name, color_rgb = get_color_by_keyword(keyword)
if color_name:
    print(f"추천 색상: {color_name}")
    print(f"RGB 값: {color_rgb}")
else:
    print("추천할 색상을 찾을 수 없습니다. 다른 키워드를 입력해보세요.") 
    색감과  RGB, HSV 값의 연관성 제작 후 다시 개발
    ex) 따듯한 색감 >> R값 높게 책정"""

""" 
가까운 색의 이름 찾기 기능
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]
CSS3_HEX_TO_NAMES 부분이 오류를 계속 일으키는 현상 발생. 더 고심한 후 개발 예정
     
"""