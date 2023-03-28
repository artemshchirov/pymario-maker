import os
import pygame


def get_path(path):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, path)

    return full_path


def import_folder(path):
    unique_path = get_path(path)
    surface_list = []

    for folder_name, sub_folders, img_files in os.walk(unique_path):
        for image in img_files:
            full_path = unique_path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def import_folder_dict(path):
    unique_path = get_path(path)
    surface_dict = {}

    for folder_name, sub_folders, img_files in os.walk(unique_path):
        for image in img_files:
            full_path = unique_path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_dict[image.split('.')[0]] = image_surf

    return surface_dict
