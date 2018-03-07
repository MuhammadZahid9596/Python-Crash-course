class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post','can block user']
    def show_privileges(self):
        for admins in self.privileges:
            print(self.name,admins)
obj = Privileges('Zahid')
obj.show_privileges()

