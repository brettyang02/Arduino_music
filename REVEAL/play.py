import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

args = sys.argv[1:]

notes = ['?', 'C', 'D', 'E', 'F', 'G', 'A', 'B', '?']
note = int(args[0])
mode = int(args[1])
distance = args[2]


print("PLAYING: ", notes[note], " ("+distance+"cm)", "\t", "mode = ", mode)

os.chdir("./REVEAL/audio/")
audio_files = ["bass_"+notes[note]+"_1s.wav", "drum_120bpm.wav"]  # Replace with your actual file paths

pygame.mixer.init()
num_channels = pygame.mixer.get_num_channels()

channels = []
for i, mp3_file in enumerate(audio_files):
    if i < num_channels:
        channel = pygame.mixer.Channel(i)
        sound = pygame.mixer.Sound(mp3_file)
        channel.set_volume(1.0)  # Set the volume (0.0 to 1.0)
        channel.play(sound)
        channels.append(channel)

# Wait for all sounds to finish playing
while any(channel.get_busy() for channel in channels):
    pass

pygame.mixer.quit()