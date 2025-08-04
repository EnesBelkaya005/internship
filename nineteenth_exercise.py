# nineteenth exercise !!!
# create stores
freelancers = {'name':'mağaza','ahmet': 70, 'mehmet':20, 'ayşe':100, 'fatma':500, 'veli':-15}
antiques = {'name':'Antikacı','masa':400, 'vazo':3, 'ayna':150, 'sandalye':75, 'tablo':5}
pet_shop = {'name':'Petshop','kedi':10, 'köpek':5, 'balık': 2}

#create an empty shopping cart
cart = {}
#loop through stores/dicts
for shop in (freelancers,antiques) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'{shop["name"]}\'na hoş geldiniz! Ne satın almak istersiniz: {shop}').lower()
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
print(f'{", ".join(list(cart.keys()))} ürünlerini satın aldınız. Ödeme yapmanıza gerek yok!!')