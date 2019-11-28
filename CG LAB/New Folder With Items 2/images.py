import os
from PIL import Image
path = "images"
newpath = "newimages"

files = [f for f in os.listdir(newpath) if os.path.isfile(os.path.join(newpath,f))]

avg = Image.open(os.path.join(newpath,files[0]))

avg = avg.convert("RGBA")

print(files)
for i in range(1,len(files)):

    img = Image.open(os.path.join(newpath, files[i]))
    img = img.convert("RGBA")


    avg = Image.blend(avg, img, 1.0 /i+1)
    
avg.save("Avg.png","PNG")
