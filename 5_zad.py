f = open('products.csv', encoding='utf-8-sig')
head = f.readline().strip()
strok = f.readlines()
f = open('products_hash.csv', 'w', encoding='utf-8-sig')
print('Hash;Count', file=f)
alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
p = 67
m = 10 ** 9 + 9
for j in range(len(strok)):
    a = strok[j].strip().split(';')
    cat = a[0]
    hash = 0
    for i in range(len(cat)):
        si = alf.find(cat[i]) + 1
        hash += (si * p ** i) % m
    hash %= m
    print(str(hash) + ';' + a[-1], file=f)

