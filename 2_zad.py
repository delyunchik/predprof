f = open('products.csv', encoding='utf-8-sig')
head = f.readline().strip()
strok = f.readlines()
mxx = 0
mxprod = 0
for i in range(len(strok)):
    a = strok[i].strip().split(';')
    if 'Выпечка' in a[0]:
        if float(a[-2]) > float(mxx):
            mxx = a[-2]
            mxprod = a[1]
print(f'В категории: Выпечка самый дорогой товар: {mxprod} его цена за единицу товара составляет {mxx}')
