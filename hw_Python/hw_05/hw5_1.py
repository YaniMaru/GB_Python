# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text_str = 'Унылая абвг пора, абв, очей очарованье! абвгд?'
print(' '.join((filter(lambda x: 'абв' not in x, text_str.split()))))
