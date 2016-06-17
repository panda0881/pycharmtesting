from pil import Image

import argparse

ascii_char = list("!@#$%^&*()12345670QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
WIDTH = 80
HEIGHT = 80

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im=Image.open("ascii_dora.png")
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""
