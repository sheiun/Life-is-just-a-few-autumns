import tempfile
import winsound

from gtts import gTTS
from pygame import mixer

SONG = """人生短短幾個秋啊.
不醉不罷. 休.
東邊兒. 我的美人. 哪
西邊兒. 黃河流
來呀來個酒. 啊
不醉不罷休.
愁情煩事別放.
心. 頭."""


def sing(sentence, lang='zh-tw', slow=False):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang, slow=slow)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.set_volume(1)
        mixer.music.play()
        winsound.PlaySound("life_down.wav", winsound.SND_ASYNC |
                           winsound.SND_ALIAS)
        while mixer.music.get_busy():
            continue
        mixer.quit()


if __name__ == '__main__':
    sing(SONG, slow=True)
