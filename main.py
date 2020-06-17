from PIL import Image, ImageDraw
import glob, os
value = 110
image = Image.open('what.png')
draw = ImageDraw.Draw(image)

width = image.size[0]
height = image.size[1]
pix = image.load()
white = 0
black = 0
za = 0
for y in range(height):
    for x in range(width):
        r = pix[x, y][0]  # узнаём значение красного цвета пикселя
        g = pix[x, y][1]  # зелёного
        b = pix[x, y][2]  # синего
        sr = (r + g + b) // 3  # среднее значение
        # print(x, y)

        if sr > 200: # белый
            print('╬', end='')
        elif sr >= 175 and sr <= 200: # ближе к белому
            print('#', end='')
        elif sr >= 50 and sr <= 175: # среднее
            print('░', end='')
        elif sr >= 5 and sr <= 50: # ближе к черному
            print('▓', end='')
        elif sr < 5: # черный
            print('█', end='')
        if x >= width - 1:
            print('')

#
#
# print('\n', black, white)
# print(range(width), range(height))