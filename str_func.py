def upper_text(text):
    '''
    возвращает текста в
     верхнем регистре'''
    return str(text.upper)


def title_text(text):
    '''
    возвращает текст с первыми заглавными
     буквами в каждом слове
    '''
    for word in text:
        word = str(word.title)
    return ' '.join(word)
