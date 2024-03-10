f = open('products.csv', encoding='utf-8-sig')
head = f.readline().strip()
head += ';Total'
strok = f.readlines()
zak = 0
f = open('products_new.csv', 'w', encoding='utf-8-sig')
print(head, file=f)
for i in range(len(strok)):
    a = strok[i].strip().split(';')
    pr = float(a[-1]) * float(a[-2])
    if 'Закуски' in a[0]:
        zak += pr
    strok[i] = strok[i].strip() + ';' + str(pr)  # убираем перенос строки
    print(strok[i], file=f)
print(zak)
