# coding = utf-8
from PIL import Image, ImageDraw, ImageFont
import numpy as np

import cfgs


class PictureMaker():
    def __init__(self, font_list=[cfgs.root_path + _ for _ in cfgs.pic['font_list']], height = cfgs.pic['height'], width = cfgs.pic['width']) -> None:
        self.H = height
        self.W = width
        self.fonts = []
        self.P = []
        remain = 1
        for i, f in enumerate(font_list):
            fontStyle=ImageFont.truetype(f, cfgs.text['text_size'], encoding="utf-8")
            self.fonts.append(fontStyle)
            if i == len(font_list)-1:
                self.P.append(remain)
            else:
                self.P.append(0.5*remain)
                remain -= self.P[i]

    def make_background(self, colors):
        res = np.ones((self.H, self.W, 3), dtype=int)
        for i in range(len(colors)):
            res[:,:,i] *= colors[i]
        return res

    def make(self, text, textColor=cfgs.pic['text_color'], bg_colors=cfgs.pic['bg_colors']):
        if textColor is None:
            textColor = tuple(np.random.randint(0, 256, 3))
        if bg_colors is None:
            bg_colors = np.random.randint(0, 256, 3)
        background = self.make_background(bg_colors)
        img=Image.fromarray(np.uint8(background))
        draw =ImageDraw.Draw(img)
        draw.text(cfgs.pic['position'], text, textColor, font=np.random.choice(self.fonts, size=None, replace=True, p=self.P))
        # draw.text((left,top),text,textColor,font=fontStyle)
        return np.asarray(img)
    
    def __call__(self, text):
        return self.make(text)