sandwich_orders=['chilli','chicken','beef','club','vegetable']
finished_sandwiches=[]
print('beef has been finished')
while'beef' in sandwich_orders:
    sandwich_orders.remove('beef')
print(sandwich_orders)
while sandwich_orders:
   current_sandwich=sandwich_orders.pop()
   print('i am working on '+current_sandwich+' for you')
   finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

