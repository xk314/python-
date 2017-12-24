import pygame
from pygame.locals import *


pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption('进击的坦克！')
help(pygame)

input()
class Master(object):
    __level = '享受特殊津贴'
    __instance = None
    #重写new魔法方法，使用单例模式，使得该类实例化的对象在同一处内存
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        print('实例化时传入的参数：', end='')
        print(args)
        return cls.__instance

