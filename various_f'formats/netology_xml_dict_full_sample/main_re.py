# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:09:49 2024

@author: Nina
"""

text2 = '";http://customs.ru/index.php?option=com_content&view=article&id=8018&Itemid=1878;"197720, Санкт-Петербург,г. Зеленогорск, Приморское шоссе, д. 511                                      ";7,80E+18;52168252;1,03E+12;7827000634;beloe-solnce@bests.ru;(812) 433-31-16;" (812) 433-30-52; (812) 640-35-34                                           ";"Секретарь  начальника: 8 (812) 433-30-45; Бухгалтерия: 8 (812) 433-49-88; Заместитель начальника пансионата по административно-хозяйственной деятельности: 8 (812)  432-97-31;                                   Заместитель начальника пансионата профилактическо-оздоровительного отделения: 8 (812)  432-97-32; заместитель начальника пансионата-начальник филиала: 8(40153)2-10-81; Администратор по размещению:  (812) 432-97-33   ";http://www.beloe-solnce.bests.ru "Государственное казенное учреждение ""Санаторий ""Победа"" ФТС России""";"""Санаторий ""Победа"" ФТС России""";"Еременко Николай Николаевич; Начальник санатория";"Войтко Владимир Васильевич; Заместитель начальника санатория по инженерно-технической части; Жигунова Вера Александровна; заместитель начальника санатория по финансово-экономическим вопросам - главный бухгалтер; Мазин Александр Александрович; Заместитель начальника санатория; Нехай Тимур Нальбиевич;Заместитель начальника санатория-начальник филиала ""Лесная сказка""; Рудницкая Любовь Николаевна; Заместитель начальника санатория по медицинской части - врач-специалист; Шлыков Анатолий Константинович;Заместитель начальника санатория-начальник филиала ""Кабардинка""";http://customs.ru/index.php?option=com_content&view=article&id=8018&Itemid=1878;354037, Краснодарский край, г. Сочи, Новороссийское шоссе, д. 2;2,30E+18;52243166;1,02E+12;2319027603;pobeda@sochi.com;8 (862)265-88-29;8 (862)265-88-25;"Заместитель начальника санатория: 8 (862) 265-88-22; Главный бухгалтер: 8 (862) 265-88-93; Заместитель начальника санатория по медицинской части - врач-специалист: 8 (862) 265-88-24; Приемная филиала ""Лесная сказка"": +7 (8777) 2-94-51; Приемная филиала ""Кабардинка"": 8 (86141) 6-57-45 '

import re

# =================================
# именованные группы https://docs.python.org/3/howto/regex.html#grouping
# для создания именованной группы после открывающей скобки нужно ввести ?P - это означает, что синтаксис регулярки написан для Python, и в угловых скобках задать имя группы
# =================================
# ПРИМЕР 1: для всех телефонов получаем только код страны и код города (например, чтобы узнать, откуда нам звонили). здесь две именованных группы: ccountry и ccity
# справочник телефонных кодов городов мира: https://www.statkod.ru/telefon.html
text_test = text2
pattern = re.compile(r"(?P<ccountry>8|\+7)?\s*\((?P<ccity>\d+)\)\s*(\d+)[-\s]*(\d{2})[-\s]*(\d{2})")
# группы мы можем получить только через match или search (т.к. нужен объект re.Match)
# поэтому придется передвигаться по нашему тексту вручную в цикле. каждый проход цикла возвращает следующий подходящий телефон и в нем будут наши две именованные группы, либо только одна - ccity.
# помним, что (?P<ccountry>8|\+7)? знак ? после группы означает, что она встречается либо ровно один раз, либо ее вообще нет. а вот группа ccity - обязательная
while True:
	result = pattern.search(text_test)
	# result == None будет означать, что в тексте больше нет совпадений и поиск пора остановить
	if result != None:
		# функция groupdict() возвращает словарь с ключом=именем группы и найденным значением
		print(result.groupdict())
		# после этого мы вручную сдвигаемся по тексту за пределы найденного телефона при помощи функции end()
		text_test = text_test[result.end():]
	else:
		break

# =================================
# поиск с предварительным условием https://docs.python.org/3/howto/regex.html#lookahead-assertions
# (?=...) - "позитивное условие"
# если выполняется регулярка, записанная после ?=, то отрабатывает все регулярное выражение. если она не выполняется, то регулярка тоже не срабатывает
# =================================
# ПРИМЕР 2: найдем телефоны всех небольших городов. у небольших городов обычно длинный, 4 и более символов, код города. вот их и будем проверять
# (?=\(\d{4,}\)) - проверочная часть представляет собой группу с проверкой условия ?=. условие: в круглых скобках должна быть последовательность цифр не короче 4 штук. например, (40153). только тогда мы будем находить и брать такой телефон.
# после проверочной группы мы записываем нашу регулярку поиска телефона (включая снова проверку кода города): \(\d+\)\s*\d+[-\s]*\d+[-\s]*\d+
pattern = re.compile(r"(?=\(\d{4,}\))\(\d+\)\s*\d+[-\s]*\d+[-\s]*\d+")
result = pattern.findall(text2)
# в тексте у нас всего три подходящих телефона, поэтому в результатах будет: ['(40153)2-10-81', '(8777) 2-94-51', '(86141) 6-57-45']
# print(result)

# =================================
# поиск с предварительным условием https://docs.python.org/3/howto/regex.html#lookahead-assertions
# обратное условие: поиск выполняется только если НЕ выполняется проверочное условие
#  (?!...) - "негативное условие"
# получим результат из все тех же телефонов с длинным кодом. в проверочном условии мы теперь запишем, что нужно игнорировать телефоны, у которых код города состоит из 3х цифр
# было: (?=\(\d{4,}\)) стало: (?!\(\d{3}\)), т.е. = поменялось на ! и {4,} поменялось на {3}
pattern = re.compile(r"(?!\(\d{3}\))\(\d+\)\s*\d+[-\s]*\d+[-\s]*\d+")
result = pattern.findall(text2)
# print(result)

# =================================
# усложняем задачу: условие if .. else в исполнении регулярок. в Python else не работает, есть только if. для работы с if нам понадобится создать группу и проверять, находим ли мы ее
#  (?(1)...)
# полностью пишется как (группа1)(?(1)регулярка)
# читается так: если в тексте встретилась группа с нужным номером, то выполняем регулярку, которая записана дальше
# =================================
text2 = u'Перелётные птицы   Перелётные птицы – это такие пернатые, какие с приходом сезонных холодов улетают в теплые страны. Для всякого типа перелётных птиц потребность перелёта определяется по-разному. Большинство людей пологают, что пернатые улетают из-за того, что им не подходят перемены в погоде. У многих перелетных птах имеется сбалансированное теплое оперение, какое удерживает тепло. Впрочем, основным фактором перелётов является неимение пищи в зимнее время. Птицы, улетающие в период холодов в теплые края, кормятся в основном червями, насекомыми, жуками и комарами. В период зимних морозов подобная живность либо погибает, либо впадают в спячку, по этой причине в данный этап сезона птицам просто-напросто недостаточно питания.   Куда улетают перелетные птицы   Перелетные птицы выполняют периодические сезонные передвижения с места гнездования в район зимовки. Они выполняют полеты, как на длинноватые, так и на краткие дистанции. Серединная скорость птиц различных объемов во время перелета может достичь 70 км/час. Перелеты делаются в пару стадий, с приостановками на питание и отдых.   Установлено, что не все самцы и самки из одной пары перекочевывают вместе. Распределенные пары весной воссоединяются. Окончательной точкой странствия птиц оказываются зоны с подобными погодными условиями. Лесная птица подбирает зоны с схожими климатическими условиями, а полевые пернатые отыскивают местности с похожим питанием.  Список перелетных птиц  Полевой жаворонок   Перелётные птицы    Пигментирован в коричневые, бурые, сероватые, желтые цвета. Данные расцветки дают возможность жаворонку скрыться посреди полей, какие этот заселяет. Тут же в начале весны жаворонки делают из травы и нетолстых ветвей гнезда.   В марте данная птица прилетает почти что самая первая. Жаворонки летят и днем, и ночью маленькими стайками.  Камышевая овсянка   Перелётные птицы   Птаха маленького габарита – её длина может достичь 16 см. Расцветка головы, подбородка и горла до половины зоба чёрного тона. От углов клюва обратно следует светлая полоска. Спина и плечи тёмного цвета, переходящего от серого до чёрно-коричневого с ржаво-коричневыми боковыми полосами. По бокам хвоста находятся светлые полосы.   Прилетают, в то время, когда кругом еще лежит снег. В основном летят парами либо в одиночку. Имеют возможность лететь совместно с зябликами и трясогузками.  Зяблик   Перелётные птицы   Зяблик хоть и имеет в длину 16 см, весит всего лишь приблизительно 25 граммов. Следовательно, перья зяблика маленькие, но их следует поискать. Вдобавок на туловище птахи имеется бежево-оранжевый тон. Ей наполнены перья грудки зяблика. На голове, крыльях и хвосте имеются темные вкрапления. На крыльях птички находятся белоснежные полоски. Это характерная характерная черта зябликов. Обычная скорость миграции зябликов равняется 70 км в сутки. Самки прилетают на пару дней позже самцов.  Белая трясогузка   Перелётные птицы   Длина тела данной птицы равняется 16-19 см и для неё свойственен продолговатый хвост. Расцветка верхней части тела в основном сероватая, а нижней – белая. Головка точно так же белая, с чёрным горлом и шапочкой.  Приобрела своё наименование из-за отличительных движений хвостом.   Осенняя миграция считается природным продолжением летних кочевок юных и окончивших свое размножение зрелых индивидов. Перемещение проходит в основном вблизи водоемов.  Болотная камышевка   Перелётные птицы   Болотная камышовка размером приблизительно 13 см, широта крыльев равняется от 17 до 21 см. Масса птицы равняется приблизительно от 11 до 14 граммов. Болотная камышовка практически не различается от тростниковой камышовки. Верхняя сторона коричнево-сероватая, а нижняя желтовато-белая. У птахи белёсое горло и острый клюв.   Самец и самка имеют схожую расцветку. Болотная камышовка проворно перемещается в плотной растительности и имеет способность подражать  пение иных птиц. Её пение весьма звучное, похоже на трель тростниковой камышовки. Припархивают на родную местность только в конце мая. Перелетают на зимовку в Центральную и Южную Африку.  Обыкновенная кукушка   Перелётные птицы   Птаха перелетает на юг Африки. Кукуют, к слову, лишь самцы. Самки типа испускают низкочастотные тона, неуловимые человечьим слухом.   Кукушка как правило летит в ночное время суток. Подразумевают, что кукушки имеют возможность пролетать до 3600 км за 1 полет без остановки.  Перепел   Перелётные птицы   Покров охристого тона, верх головы, спина, надхвостье и внешние покрывающие перья хвоста в тёмных и светлых коричневых поперечных полосках и пятнышках, сзади глаз рыжая полоска. У самца щёки тёмно-рыжие, зоб рыжий, подбородочек и горло чёрные. Самка выделяется от него бледно-охристым подбородком и горлом, и наличием чёрно-коричневых пятнышек на нижней доли тела и боках.   Больше всего перепелы в период миграции передвигаются через Балканы и Ближний Восток. Первые пролетные стаи практически целиком состоят из самцов.  Черный стриж   Перелётные птицы   Чёрный стриж может достичь в длину 18 см, размах крыльев – 40 см. Хвост вилкообразный, оперенье тёмно-коричневого тона с зеленым железным оттенком, по виду стриж схож на ласточку. Оперенье самцов и самок не различается, но птенцы чуть-чуть светлее зрелых стрижей, а их перья отличаются грязно-белыми каёмками на концах. Летом перья сильно выцветают и общий цвет делается более светлым.   Вылет на зимовку у стрижей наступает уже в начале августа. Полет птиц проходит через Украину, Румынию и Турцию. Последней их остановкой будет Африканский континент. Продолжительность миграции стрижа длится 3-4 недель.  Серая цапля   Перелётные птицы   Птица большая, может достичь в длину 95-ти сантиметров. Масса птицы равна 1,5-2 кг. Птица находить под наблюдением, так как число популяции уменьшается. В России цапли погибают не столь от рук охотников, как от холодов.   Миграция у таких птиц совершается с конца августа, летят они предпочтительно вечером и ночью. во время миграции цапли имеют все шансы дойти возвышенности полета до 2000 метров.  Лесная завирушка   Перелётные птицы   Внешний вид птицы незаметный. Оперенье буро-сероватое. Она весьма маленькая. Масса тела завирушки не больше 25-ти граммов. Некоторые перепутывают птичку с воробьем. Завирушка иметь отношение к подразделению воробьинообразных.  Какие перелётные птицы улетают раньше, а какие позже?       В начале улетают пернатые, кормящиеся насекомыми. Так как их еды в определенный момент становится мало: насекомые скрываются, и птицы улетают южнее, для того, чтобы прокормить себя.      После, совместно с обмерзанием земли, улетают и пернатые, кормящиеся зёрнами, семенами насаждений и растений.      Почти до конца задерживаются большие водоплавающие адепты птиц, до того времени, как их водоёмы не станут покрываться ледяной коркой.'

# ПРИМЕР 3 - найдем в тексте про перелетных птиц (https://rarebirds.ru/interesno/perelyotnye-ptitsy) все предложения, в которых говорится про зиму, зимовку и т.д. и выведем их на экран
# для этого в регулярке нужно объявить группу такого вида: (зим\w+)
# если эта группа находится, мы собираем предложение вокруг нее (т.е. часть предложения до группы + сама группа + конец предложения)
pattern = re.compile(r"[А-ЯЁ][^\.!?]+(зим\w+)(?(1)[^\.!?]+[\.!?])")
# такой вызов выведет только первый результат поиска
result = pattern.search(text2)
print(result.group())

# если мы хотим увидеть все результаты, делаем как в ПРИМЕРЕ 1, с циклом:
text_test = text2
while True:
	result = pattern.search(text_test)
	# result == None будет означать, что в тексте больше нет совпадений и поиск пора остановить
	if result != None:
		print(result.group())
		# после этого мы вручную сдвигаемся по тексту за пределы найденного телефона при помощи функции end()
		text_test = text_test[result.end():]
	else:
		break
