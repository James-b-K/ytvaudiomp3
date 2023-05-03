import glob
import os.path
from pydub import AudioSegment

files = glob.glob("*.mp4")
for x in files:
    if not os.path.isdir(x):
        filename = os.path.splitext(x)
        try:
            os.rename(x,filename[0] + '.m4a')
        except:
            pass
        m4a_audio = AudioSegment.from_file(filename[0]+'.m4a', format="m4a")
        m4a_audio.export(filename[0]+'.mp3', format="mp3")
        os.remove(filename[0] + '.m4a')
