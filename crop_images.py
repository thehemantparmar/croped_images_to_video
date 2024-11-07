from PIL import Image

for x in range(1, 3):
    img_name="img/flower"+str(x)+".png"
    print(img_name)
    im = Image.open(img_name)

    left = 150
    top = 40
    right = 350
    bottom = 240
 
    im1 = im.crop((left, top, right, bottom))
    save_img_name="crop/flower"+str(x)+".png"
    im1.save(save_img_name)
