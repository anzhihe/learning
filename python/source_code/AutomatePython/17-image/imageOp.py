catIm = Image.open('zophie.png')
width, height = catIm.size
catIm.save('zophie.jpg')
im = Image.new('RGBA', (100,200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')
croppedIm = catIm.crop((335,345, 565,560))
croppedIm.save('cropped.png')
catCopyIm = catIm.copy()
facedIm = catIm.crop((335,345, 565,560))
faceIm = catIm.crop((335,345, 565,560))
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')
w, h = catIm.size
fw, fh = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, w, fw):
    for top in range(0, h, fh):
            print(left, top)
            catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('tiled.png')
qIm = catIm.resize((int(w/2), int(h/2)))

qIm.save('quartersized.png')
sveltedIm = catIm.resize((w, h+300))

sveltedIm.save('svelte.png')
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')
im = Image.new('RGBA', (100, 100))
im.getpixel((0,0))
(0, 0, 0, 0)
for x in range(100):
    for y in range(50):
            im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))


from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

im.save('putPixel.png')