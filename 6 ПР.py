text = input('Введите текст: ')
text1 = ''
a = len(text) // 2
for i in range(a):
    if text[i] == 'п' or text[i] == 'П':
        text1 += '*'
    else: text1 += text[i]
b = text[a:]
text1 += b
print(text1)