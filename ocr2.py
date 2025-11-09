import re
import sys
import time
import keyboard
import pyperclip
import numpy as np
from PIL import ImageGrab
from cnocr import CnOcr

ocrs = CnOcr(det_model_name='naive_det')


def ocr(img: np.ndarray) -> str:
    return ocrs.ocr(img)


def f1() -> None:
    print('[Meta Shift S]')
    time.sleep(5)

    print('get img...')
    img = ImageGrab.grabclipboard()
    while img is None:
        img = ImageGrab.grabclipboard()
    pth = 'temp.png'
    img.save(pth)

    print('get str...')
    l = list()
    for i in ocr(pth):
        l += i['text']
    s = ''.join(l)
    print('ocr: %s' % s)

    pyperclip.copy(s)
    print("copied.")
    print()


if __name__ == '__main__':
    print('start')
    while True:
        if keyboard.is_pressed('ctrl+c'):
            sys.exit(0)
        if keyboard.is_pressed('windows+shift+s'):
            f1()
