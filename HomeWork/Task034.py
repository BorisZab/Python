
lists = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
lists = list(map(str, lists.split()))
last = lists[len(lists)-1]
res = list(filter(lambda x: x == "а", last))
if len(res)  % 2 == 0:
    lists.append('Парам пам-пам')
else:
    lists.append('Пам парам')
print(lists)





