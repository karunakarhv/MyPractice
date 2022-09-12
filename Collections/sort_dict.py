from operator import itemgetter, attrgetter

my_list = [{'name':'Karun', 'id':2},
           {'name': 'Adithi', 'id':1},
           {'name':'Anshu', 'id':0}]

# Sort by names
print(sorted(my_list, key=itemgetter('name')))
# Sort by ID
print(sorted(my_list, key=itemgetter('id')))
# min
print(min(my_list, key=itemgetter('id')))
# max
print(max(my_list, key=itemgetter('id')))

class User:
    def __init__(self, userId):
        self.userId = userId
    def __repr__(self):
        return 'User({})'.format(self.userId)

users = [User(1), User(4), User(0)]
# Sort by ID
print(sorted(users, key=attrgetter('userId')))
# min
print(min(users, key=attrgetter('userId')))
# max
print(max(users, key=attrgetter('userId')))
