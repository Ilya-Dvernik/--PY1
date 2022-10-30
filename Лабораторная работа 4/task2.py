def get_count_char(str_):
    stringlover = str_.lower()
    re = ''.join(stringlover)
    without__ = re.split(sep='!')
    without__1 = ''.join(without__)
    without__12 = without__1.split(sep='\n')
    without__2 = ''.join(without__12)
    without__23 = without__2.split(sep=' ')
    without__3 = ''.join(without__23)
    without__34 = without__3.split(sep=',')
    without__4 = ''.join(without__34)
    without__45 = without__4.split(sep='.')
    without__5 = ''.join(without__45)

    strocka = ''.join(without__5)

    sett = {}
    for i in strocka:
        if i in sett :
            sett[i] += 1
        else :
            sett[i] = 1
    return sett

     # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
