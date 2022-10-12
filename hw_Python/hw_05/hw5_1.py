# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Унылая абвг пора, абв, очей очарованье! абвгд?'
sort_text = list(filter(lambda x: 'абв' not in x, text.split()))
print(' '.join(sort_text))
