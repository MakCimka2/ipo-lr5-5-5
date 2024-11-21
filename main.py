a ="Каша Ложка Python Python"
count = 0
b = a.split()
for i in b:
    if i == "Python": #Считаем сколько раз в списке встречается слово питон
        count += 1  #Прибавляем к счетчику 1
print(count)
