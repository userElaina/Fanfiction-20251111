import re
import sys
import time
import easyocr
import keyboard
import pyperclip
import numpy as np
from PIL import ImageGrab

ZH_PATTERN = r'[\u4e00-\u9fa5]+'

# reader = easyocr.Reader(['ch_sim'])
reader = easyocr.Reader(['ch_sim', 'en'])


def ocr(img: np.ndarray) -> str:
    return reader.readtext(img)


def f1() -> None:
    print('[Meta Shift S]')
    time.sleep(5)

    print('get img...')
    img = ImageGrab.grabclipboard()
    while img is None:
        img = ImageGrab.grabclipboard()
    data = np.array(img)

    print('get str...')
    l = list()
    for idx, s, acc in ocr(data):
        # matches = re.findall(ZH_PATTERN, s)
        # l += matches
        l += s
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
