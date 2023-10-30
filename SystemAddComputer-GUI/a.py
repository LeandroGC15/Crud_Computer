import re
data = input('Enter data: ')
text = ''
with open('db/persons.txt', 'r') as file:
    text = file.read()
    file.close()
print(text)
patron = r'\[.+'+data+'.+\]'
search = re.findall(patron, text)

if search and len(data) > 4:
    for i in range(len(search)):
        person = search[i][1:-1].replace(' ', '').split(',') 
    data = person

print(data)