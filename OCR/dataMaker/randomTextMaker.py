# coding = utf-8

import math
import random
import numpy as np

import cfgs

class TextMaker():

    def __init__(self, dict_path=cfgs.text['dict_path']) -> None:
        dictionary = []
        try:
            with open(dict_path, 'r', encoding='utf-8') as dp:
                for line in dp.readlines():
                    dictionary.append(line.strip())
        except:
            print('Error When Makeing Dict')
            exit()
        self.dict = dictionary
        self.size = len(dictionary)

    def make(self, text_len):
        res = []
        for i in np.random.randint(self.size, size=text_len):
            res.append(self.dict[i])
        return ''.join(res)

    def make_gaussian(self, text_len, sigma=0.2):
        return self.make(math.floor(np.random.normal(text_len, sigma)))

    def __len__(self):
        return self.size

    def __call__(self, text_len):
        return self.make(text_len)
        

