



purchases = [
    {'Cliente':'Maria', 'Ultima Compra': 'PS4', 'qtd_compras': 110 },
    {'Cliente':'Paulo', 'Ultima Compra': 'Redmi note 11', 'qtd_compras': 34 },
    {'Cliente':'Sandra', 'Ultima Compra': 'Chapinha', 'qtd_compras': 750 }
]

purchases.append({'Cliente':'Natália', 'Ultima Compra': 'Iphone 13', 'qtd_compras': 230 })

purchases.append({'Cliente':'Josefa', 'Ultima Compra': 'PS4', 'qtd_compras': 635})

#Menores compradores
print(sorted(purchases,key = lambda compra : compra ['qtd_compras']))

#Maior comprador 
max_buyer= sorted(purchases, key = lambda compra : compra ['qtd_compras'],reverse=True)


max_buyer[0]['Disconto']=1-0.75
print(max_buyer[0])

#Ordenando pelo nome....

print(sorted(purchases,key = lambda username : username['Cliente']))












