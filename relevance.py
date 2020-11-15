from keywords import key_words
from parser_p.parser import html, return_dic

#  {релевантность: заголовок}
relevance_check = {}
string = '''Извините, не можем ответить на ваш вопрос.
Пожалуйста, обратитесь в службу поддержки по номеру: 8-800-1000-800'''


#  Сравнивает введенные слова с добытыми с сайта
#  question - введённые слова
def entry_relevance(question):
    try:
        #  проверка на соответствие слов
        parse_dict = return_dic()

        for i in parse_dict:
            relevance_check[len(key_words(question) & key_words(i))] = i
        max_relevance = max(relevance_check)
        relevance_check_value = relevance_check[max_relevance]
        relevance_check.clear()
        if max_relevance < 1:
            return string
        else:
            return parse_dict[relevance_check_value]
    except Exception:
        return string
        pass


if __name__ == '__main__':
    print(return_dic())
    while True:
        message = input()
        if message == '0':
            break
        print(entry_relevance(message))
