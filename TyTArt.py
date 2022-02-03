# Tranform every typing letter into a ASCII Art

print('Try typping anything and press enter')
message = input()
message = message.lower()
answer = ''


print(message)

for item in message:
    if not item == ' ':
        page = f'Letters/{item}.txt'
        with open(page, 'r') as pp:
            for i in pp.readlines():
                answer = answer + i
    else: answer = answer + '\n\n\n\n'



print(answer)
