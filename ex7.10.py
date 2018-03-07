poll_results={}
while True:
    name = input('what is your name?')
    place = input('where do you wanna go?')
    stopper=input('would you like some one else to responf?')
    poll_results[name]=place
    if stopper !='yes':
        break
for name,place in poll_results.items():
    print(name.title()+' would like to visit '+place.title())