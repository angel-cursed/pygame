from os import walk
import pygame

def import_folder(path):
    surf_list = []
    for _,__,img_files in walk(path):
        for img in img_files:
            full_path = path + "/" + img
            surface = pygame.image.load(full_path).convert_alpha()
            surf_list.append(surface)
    return surf_list
