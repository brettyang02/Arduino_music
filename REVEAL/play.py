import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

args = sys.argv[1:]

notes = ['?', 'C', 'D', 'E', 'F', 'G', 'A', 'B', '?']
note = int(args[0])
mode = args[1]
distance = args[2]

volumes = [0.5, 1.0] # Set the volume (0.0 to 1.0)

print("PLAYING: ", notes[note], " ("+distance+"cm)", "\t", "mode = ", mode)

os.chdir("./REVEAL/audio/")
bass_filename = notes[note]+"_"+mode+".mp3"
drum_filename = "drum_"+mode+".mp3"
audio_files = [bass_filename, drum_filename]  # Replace with your actual file paths

pygame.mixer.init()
num_channels = pygame.mixer.get_num_channels()

channels = []
for i, mp3_file in enumerate(audio_files):
    if i < num_channels:
        channel = pygame.mixer.Channel(i)
        sound = pygame.mixer.Sound(mp3_file)
        channel.set_volume(volumes[i])
        channel.play(sound)
        channels.append(channel)

# Wait for all sounds to finish playing
while any(channel.get_busy() for channel in channels):
    pass

pygame.mixer.quit()