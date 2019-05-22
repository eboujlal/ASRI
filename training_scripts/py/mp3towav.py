## Please install apt-get install ffmpeg<
from os import path,listdir,stat
from pydub import AudioSegment
from pydub.playback import play
import sox
from easyThreading.BaseThreading import BaseThreading


CLIPS = "/home/iiraven/ASRI/raw_files/clips/"
OUTPUT = "/home/iiraven/ASRI/dataset/wavs/"


def convert_wav(mp3_filename, wav_filename):
    if not path.exists(wav_filename):
        transformer = sox.Transformer()
        transformer.convert(samplerate=16000)
        try:
            transformer.build(mp3_filename, wav_filename)
        except sox.core.SoxError:
            print("error")
            pass


class ConverterThreading(BaseThreading):
    def process(self, row):
        convert_wav(CLIPS+row,OUTPUT+row.replace('.mp3','.wav'))

audios = listdir(CLIPS)
audios = [audio for audio in audios if audio.endswith('.mp3')]
nt = ConverterThreading(raw_list=audios, number_of_threads=6)
nt.start()