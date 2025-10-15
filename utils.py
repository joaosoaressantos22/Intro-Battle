import pygame

def play_sound(path, vol=0.1):
    sound_bg = pygame.mixer.Sound(path)
    sound_bg.set_volume(vol)
    sound_bg.play()

def stop_sound(sound):
    sound.stop()

def sound_restart(sound, vol=0.1):
    stop_sound(sound)
    sound.play()