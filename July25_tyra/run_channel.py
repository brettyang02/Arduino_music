import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def play_file(file_path, channel):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(file_path))

def get_file():

    current_folder_path = os.path.join('.')
    # List of sound file names
    wav_files = [filename for filename in os.listdir(current_folder_path) if
                 filename.endswith(".mp3")] # Change this depending on which type of sound files
    return wav_files

def main():
    pygame.mixer.init()

    # Get files to a list
    files_1 = get_file()

    channels = [0, 1, 2]  # Three different channels (0, 1, 2)

    # Play files
    for i in range(len(files_1)):
        play_file(files_1[i], channels[i])

    # Wait for the sounds to finish playing
    while any(pygame.mixer.Channel(channel).get_busy() for channel in channels):
        pass

    pygame.mixer.quit()

if __name__ == "__main__":
    main()
