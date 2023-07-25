import threading
import pygame
import os
import time

# Define a function to play a sound file
def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print(f"Thread {threading.current_thread().name}: playing")
        continue
def get_wav_file():

    current_folder_path = os.path.join('.')
    # List of sound file names
    wav_files = [filename for filename in os.listdir(current_folder_path) if
                 filename.endswith(".wav")]
    return wav_files
def main():
    # Create a list to store thread objects
    threads = []

    files_1 = get_wav_file()
    for files in files_1:
        print(files)
    time.sleep(1)

    # Create and start a thread for each sound file
    for filename in files_1:
        thread = threading.Thread(target=play_sound, args=(filename,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All sound files played.")

# Check if this script is being run as the main program
if __name__ == "__main__":
    main()

