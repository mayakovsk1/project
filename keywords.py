from string import punctuation
import pymorphy2


#  разделения текста на слова
def word_split(text):
    text = ''.join(ch for ch in text if ch not in punctuation)
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].lower()
    return text


#  приведение слов в нормальную форму
def morphy_split(text):
    rawkey = []
    morph = pymorphy2.MorphAnalyzer()
    for i in range(len(text)):
        p = morph.parse(text[i])[0]
        p = p.normal_form
        rawkey.append(p)
    return rawkey


#  Исключение паразитных слов. Стопвордс - словарь слов паразитов
def sift(text, stopwords):
    keywords = []
    for i in text:
        if not (i in stopwords):
            keywords.append(i)
    return keywords


#  Функция, объеденяющая все.
#  На ввод идет строка запрса и словарь паразитных слов, на выход идет множество ключевых слов
def key_words(text):
    stopwords = ['как', 'куда', 'сегодня', 'я', 'он', 'она', 'они', 'лагать', 'работать', 'вчера', 'скоро', 'мало',
                 'много', 'что', 'делать', 'какое', 'или', 'и', 'от', 'в', 'на', 'нас', 'вас', 'их', "какими"]
    text = word_split(text)
    text = morphy_split(text)
    text = sift(text, stopwords)
    text = set(text)
    return text


if __name__ == '__main__':
    while True:
        message = input()
        if message == 0:
            break
        stopwords = ['как', 'куда', 'сегодня', 'я', 'он', 'она', 'они', 'лагать', 'работать', 'вчера', 'скоро', 'мало',
                     'много', 'что', 'делать', 'какое', 'или', 'и', 'от', 'в', 'на', 'нас', 'вас', 'их', "какими",
                     'подключить']
        print(key_words(message))