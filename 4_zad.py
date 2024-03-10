f = open('products.csv', encoding='utf-8-sig')
head = f.readline().strip()
head += ';Promocode'
strok = f.readlines()
zak = 0
f = open('products_promo.csv', 'w', encoding='utf-8-sig')
print(head, file=f)
for i in range(len(strok)):
    a = strok[i].strip().split(';')
    s = a[1][:2] + a[2][:2] + a[1][:-3:-1] + a[2][4:2:-1]
    s = s.upper()
    print(f'{strok[i].strip()};{s}', file=f)
