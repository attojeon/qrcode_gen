'''
pip install qrcode 
pip install pillow 
'''
import qrcode, time
from PIL import Image 

msg = 'https://python.learnsteam.kr'
target_file = time.strftime("%Y%m%d%H%M%S", time.localtime())
target_file += ".png"

img = qrcode.make(msg)
img.save(target_file)
im = Image.open(target_file)
im.show()

