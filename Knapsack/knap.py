weight =[3,1,2,2,2]
price = [100,100,150,180,250]
capacity = 3

table = [[0 for col in range(capacity+1)] for row in range(len(weight)+1)]

for row in range(len(weight)+1):
    for col in range(capacity+1):
        if row == 0 or col==0:
            table[row][col]=0
        elif weight[row-1] <= col:
            table[row][col] = max(table[row-1][col],table[row-1][col-weight[row-1]]+price[row-1])
        else:
            table[row][col] = table[row-1][col]

for row in table:
    print(row)

maks_value = table[len(weight)][capacity]

things = []
for x in range(len(weight),0,-1):
    if maks_value >0:
        maks_value = maks_value - price[x-1]
        things.append(x)
print(f"{things}")





n = len(weight)
for i in range(n, 0, -1):
        if maks_value <= 0:
            break
        # either the maks_valueult comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if maks_value == table[i - 1][capacity]:
            continue
        else:
 
            # This item is included.
            print(weight[i - 1])
            # Since this weight is included
            # its value is deducted
            maks_value = maks_value - price[i - 1]
            capacity = capacity - weight[i - 1]
 