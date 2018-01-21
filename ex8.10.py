def magicians(magicians_names):
    while magicians_names:
        tempvar = magician_names.pop()
        great_magician.append(tempvar)
        print(great_magician,'is a great magician')
        print(magician_names)
magician_names =['xerak','sibtain','muqeet','usman']
great_magician =[]
magicians(magician_names)