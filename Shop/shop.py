input1 = open("shop/input.txt", "r")
output1 = open("shop/output", 'w')
shop = {

}
for item in input1:
    item = item.split()
    name = item[0]
    product = item[1]
    count = int(item[2])
    if name not in shop:
        shop[name] = {product: count}
    else:
        if product in shop[name]:
            shop[name][product] += count
        else:
            shop[name][product] = count

shop = str(shop)
output1.write(shop)
input1.close()
output1.close()