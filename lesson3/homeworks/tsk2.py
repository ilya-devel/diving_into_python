"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

TEXT = """
Эсседарий (лат. essedarius) — тип гладиатора, часто упоминающийся в античной литературе и эпиграфических источниках с 
середины I века н. э. Название в переводе с латыни означает «колесничий». Предположительно основу для этого типа 
гладиаторов заложили увиденные Цезарем во время завоевания Британии воины на колесницах.

Среди известных эсседариев — два бойца, упоминаемые в надписях в амфитеатре Нима. Один из них, арабский раб Фавст, по 
прозвищу Счастливчик, одержал 37 побед на арене, прежде чем получить свободу во время игр, устроенных Гаем Помпеем 
Марциалом. Другой, греческий раб Берилл, одержал 20 побед до того, как тоже получил свободу, однако умер в 
возрасте 25 лет, возможно, от полученных многочисленных ран. Несмотря на обилие упоминаний в текстах, изображений 
гладиаторов, сражающихся с колесниц, не сохранилось, за единственным исключением. Однако на этом изображении 
гладиатор, вооружённый круглым мечом и копьём, дерётся со львом, то есть речь идёт об изображении не эсседария, а 
венатора. Исходя из многочисленности упоминаний и основываясь на предположении, что эсседарии могли вести бой и 
пешими, М. Юнкельман предлагает по умолчанию считать представителями этого типа любых изображённых гладиаторов, 
чьё вооружение не совпадает ни с одним другим описанным типом. В частности, на роль эсседариев претендуют два 
гладиатора с рельефа из Помпей, ведущие бой между собой при участии ретиариев. На этом изображении их вооружение 
составляют овальный щит и меч, а также закрытый шлем с перьями. Изображение, возможно, относится к периоду, когда 
ещё не сформировалось устойчивого противостояния ретиариев и секуторов, так как снаряжение изображённых гладиаторов 
(относительно небольшой щит, отсутствие поножей) оставляет их уязвимыми для трезубца ретиария. По схожим изображениям 
восстанавливается остаток снаряжения — низкие гетры без поножей и маника на левой руке. По предположению Юнкельмана, 
основанному на изображении плохой сохранности из Помпей (на котором могут быть изображены также самниты), эсседарии 
могли использовать также копья или начинать бой с метания дротиков, но подтверждающих это изображений или текстов не 
найдено.

Остаётся невыясненным, как именно эсседарии вели бой на колесницах и происходило ли это вообще. К. С. Носов 
предлагает два возможных объяснения: этот тип гладиаторов изначально предназначался для боя с колесниц, но 
из-за дороговизны оборудования вскоре стал пешим, либо колесницы изначально использовались только для торжественного 
выезда на арену, подобно героям Гомера, после чего гладиатор продолжал бой пешим.
"""

# clear_text = TEXT.lower()
# for ch in ',.()«»':
#     if ch in clear_text:
#         clear_text = clear_text.replace(ch, "")
clear_text = ''.join([ch for ch in TEXT.lower() if ch.isalnum() or ch == ' '])

words = set([word.strip() for word in clear_text.lower().split()])

counts = {word: clear_text.split().count(word) for word in words}

print(sorted(counts.items(), key=lambda c: c[1], reverse=True)[:10])
