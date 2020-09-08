from googletrans import Translator

# 多线程翻译
import threading


# translator = Translator()
# translate = translator.translate('你好世界', src='zh-cn', dest='km')
# print(translate.text)

# <Translated src=ko dest=en text=Goo


# # 翻译成英文
# translator = Translator()
# translate = translator.translate(data, src='zh-cn', dest='en')
# en = translate.text
# print(en)
#
# # 翻译成高棉
# translator = Translator()
# translate = translator.translate(data, src='zh-cn', dest='km')
# km = translate.text
# print(km)


def runTr(data, id):
    print('runTr', data, id)
    translator = Translator()
    translate = translator.translate(data, src='zh-cn', dest='en')
    en = translate.text
    print(en)


if __name__ == '__main__':
    for i in range(1, 30):
        thread = threading.Thread(target=runTr, args=('你好世界' + str(i), 11,))
        thread.start()
