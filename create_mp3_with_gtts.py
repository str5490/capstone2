import argparse
from gtts import gTTS
from playsound import playsound

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", default = 'voice',
                help = "path to save mp3 file")
ap.add_argument("-n", "--name", default = 'notice01',
                help = 'The name of mp3 file')
ap.add_argument("-l", "--lang", default = 'ko',
                help = 'language')
ap.add_argument("-t", "--text", default = '테스트중입니다.',
                help = 'Sentence to be converted')
args = vars(ap.parse_args())

tts = gTTS(text = args["text"], lang = args["lang"])
m_mpfile = args["path"] + '\\' + args["name"] + ".mp3"
tts.save(m_mpfile)
playsound(m_mpfile)
