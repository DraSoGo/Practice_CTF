import numpy as np
from PIL import Image

img1 = Image.open('/home/drasogo/DraSoGo/Practice_CTF/Cryptography/Cryptohack/general/xor/lemur_xor/flag.png')
img1 = img1.convert("RGB")
img1 = np.asarray(img1)
img2 = Image.open('/home/drasogo/DraSoGo/Practice_CTF/Cryptography/Cryptohack/general/xor/lemur_xor/lemur.png')
img2 = img2.convert("RGB")
img2 = np.asarray(img2)
result = Image.fromarray(img1 ^ img2)
result.save('result.png')