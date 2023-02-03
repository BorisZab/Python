# настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки
# распределяются так:
one = [
    "A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н",
    "О", "Р", "С", "Т"
]
two = ["D", "G", "Д", "К", "Л", "М", "П", "У"]
three = ["B", "C", "M", "P", "Б", "Г", "Ё", 'Ь', "Я"]
four = ["F", "H", "V", "W", "Y", "Й", "Ы"]
five = ["K", "Ж", "З", "Х", "Ц", "Ч"]
eight = ["J", "X", "Ш", "Э", "Ю"]
ten = ["Q", "Z", "Ф", "Щ", "Ъ"]
word = input()
word = tuple(word)
sum = 0
n = 0
c = len(word) - 1
for i in word:
    n = word[c]
    if n in one:
        sum += 1
    if n in two:
        sum += 2
    if n in three:
        sum += 3
    if n in four:
        sum += 4
    if n in five:
        sum += 5
    if n in eight:
        sum += 8
    if n in ten:
        sum += 10
    c -= 1
print(sum)