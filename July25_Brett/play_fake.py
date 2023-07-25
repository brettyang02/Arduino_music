import sys
import time

args = sys.argv[1:]

notes = ['?', 'C', 'D', 'E', 'F', 'G', 'A', 'B', '?']
note = int(args[0])
mode = int(args[1])
distance = args[2]


print("PLAYING: ", notes[note], " ("+distance+"cm)", "\t", "mode = ", mode)