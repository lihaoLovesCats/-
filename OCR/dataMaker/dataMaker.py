# coding = utf-8
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pathlib

from randomTextMaker import TextMaker
from picMaker import PictureMaker
import cfgs

def main():
    text_maker = TextMaker()
    pic_maker = PictureMaker()
    for i in range(10):
        cv2.imshow(None, pic_maker.make(text_maker.make_gaussian(26)))
        cv2.waitKey(0)

if __name__ == '__main__':
    main()
