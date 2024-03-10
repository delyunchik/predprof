f = open('products.csv', encoding='utf-8-sig')
head = f.readline().strip()
strok = f.readlines()
mnn = 'inf'
mn_prod = 0
categ = input()
while categ != 'молоко':
    for i in range(len(strok)):
        a = strok[i].strip().split(';')
        if categ in a[0]:
            if float(a[-2]) < float(mnn):
                mnn = a[-2]
                mn_prod = a[1]
    if mnn == 'inf':
        print('Такой категории не существует в нашей БД')
    else:
        print(f'В категории: {categ} товар: {mn_prod} был куплен {mnn} раз')
    categ = input()
    mnn = 'inf'
