
import srt
import io

filename = 'Person of Interest 1x08 - Foe (English).srt'

f = io.open(filename) 

my_sub = srt.parse(f)

for sub in my_sub:
    print(sub.content)