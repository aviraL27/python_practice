items = ['apple', 'banana', 'banana', 'orange', 'mango']

unique_item = set()

for item in items:
    if item in unique_item:
        print(item)
        break
    else:
        unique_item.add(item)

