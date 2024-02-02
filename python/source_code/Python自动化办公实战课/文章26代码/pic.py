from PIL import Image
# pip3 instlal pillow

# 打开图片文件
image = Image.open("./文章26代码/sunrise.jpg")

# 模式“P”为8位彩色图像，每个像素用8个bit表示
image_p = image.convert(
    "P", palette=Image.ADAPTIVE
    )  
# image_p.show()

# 以列表形式返回图像调色板,目标需先转换为P模式，才具有调色板属性，否则得到的调色板为None
palette = image_p.getpalette()

# 返回此图像中使用的颜色列表,maxcolors默认256
color_counts = sorted(image_p.getcolors(maxcolors=9999), reverse=True)
colors = []


for i in range(5):
    palette_index = color_counts[i][1]
    dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]
    colors.append(tuple(dominant_color))

print(colors)
# [(204, 154, 86), (230, 237, 226), (213, 213, 212), (251, 238, 206), (82, 167, 204)]
for i, val in enumerate(colors):
    image.paste(val,(0+i*120, 0 ,100+i*120, 100))

image.save("./文章26代码/sunrise2.png")
image.show()

