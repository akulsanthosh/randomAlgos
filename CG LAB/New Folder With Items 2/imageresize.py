import os
from PIL import Image
from tkinter import filedialog



path = filedialog.askdirectory()
newpath = "newimages"
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]

if not os.path.exists(newpath):
    os.mkdir(newpath)
size = [600,600]
j = "a.png"
for  i in files:
    img = Image.open(os.path.join(path,i))
    img = img.resize((size[0],size[1]),Image.ANTIALIAS)
    img.convert("RGBA")
    img.save(newpath+"\\"+str(j),"PNG")
    j = "a"+j



files = [f for f in os.listdir(newpath) if os.path.isfile(os.path.join(newpath,f))]

avg = Image.open(os.path.join(newpath,files[0]))

avg = avg.convert("RGBA")


for i in range(1,len(files)):

    img = Image.open(os.path.join(newpath, files[i]))
    img = img.convert('RGBA')
    avg = Image.blend(avg, img, 1.0 /(i+1))
    print(i)

avg.save("Avg.png","PNG")
