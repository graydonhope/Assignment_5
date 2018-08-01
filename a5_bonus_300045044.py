## Assignment 5 Bonus
## Sadiq Abbas
## Graydon Hope 300045044

class Person:
    def __init__(self, user_id, name, friends):
        '''(Person, Int, String, List) -> None
        '''
        self.id= user_id
        self.name = name
        self.friends = friends

    def __repr__(self):
        '''(Person) -> String'''
        return "Person(" + str(self.id) + "," + str(self.name) + "," + str(self.friends) + ")"

    def get_friends(self):
        '''(Person) -> List '''
        return self.friends



class Network:
    def __init__(self, names, user_ids):
        '''(Network, List, List) -> None '''
        self.network = []
        friends_list = create_network(user_ids, names)[0]
        list_of_ids = create_network(user_ids, names)[1]
        name_listx = create_network(user_ids, names)[2]
        
        for index in range(len(name_listx)):
            self.network.append(Person(list_of_ids[index], name_listx[index], friends_list[index]))
        

    def __repr__(self):
        '''(Network) -> String'''
        return "Network(" + str(self.network) + ")"

    def __len__(self):
        '''(Network) -> Integer '''
        return len(self.network)

    def get_uid(self):
        '''(Network) -> None '''
        get_int()

    def getCommonFriends(self, user1, user2):
        '''(Network, Integer, Integer) -> List  
        Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
        and friends of user 1 and user 2 sorted 
        Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
        '''
    
        common=[]
        user1_friendlist = []
        user2_friendlist = []

        for item in range(len(self.network)):
            if int(self.network[item].id) == user1:
                user1_friendlist = self.network[item].friends
            if int(self.network[item].id) == user2:
                user2_friendlist = self.network[item].friends

        if len(user1_friendlist) > len(user2_friendlist):
            more_friends = user1_friendlist
            less_friends = user2_friendlist
        else:
            more_friends = user2_friendlist
            less_friends = user1_friendlist
        for i in more_friends:
            if i in less_friends:
                common.append(i)

        for i in range(len(common)):
            common[i] = int(common[i])
            
        return common


    
    def recommend(self, user_id):
        '''(int, 2Dlist)->int or None
        Given a 2D-list for friendship network, returns None if there is no other person
        who has at least one neighbour in common with the given user and who the user does
        not know already.
        
        Otherwise it returns the ID of the recommended friend. A recommended friend is a person
        you are not already friends with and with whom you have the most friends in common in the whole network.
        If there is more than one person with whom you have the maximum number of friends in common
        return the one with the smallest ID. '''
        
        location=get_index(self, user_id)
        maximum=-1
        who=None

        if location==-1: return who
        
        for item in self.network:
            if int(item.id)!= user_id:
                if user_id not in item.friends:
                    common=Network.getCommonFriends(self, user_id, int(item.id))
                    if len(common)>maximum and len(common)>0:
                        maximum=len(common)
                        who=int(item.id)
        
        return who


def get_index(self, user):
    '''(2Dlist, int)->int
    Given a 2D-list for friendship network, and a user ID,
    returns the index of that user in the 2D-list friendship network. Returns -1 if the user not in the network
    Precondition: user is a non-negative int'''
    
    location=-1
    for i in range(len(self.network)):
        if int(self.network[i].id) == user:
            location=i
    return location

    

def create_network(file_name, file_name2):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE
    total_list = []
    friends.pop(0)
    for i in friends:
        i = i.split(" ")
        total_list.append(i)

    listx = []
    for item in total_list:
        if item[0] not in listx:
            listx.append(item[0])
        if item[1] not in listx:
            listx.append(item[1])

    
    listx.sort()

    list_of_id =[]

    for item in friends:
        item = item.split(" ")

        if item[0] not in list_of_id:
            list_of_id.append(item[0])
        if item[1] not in list_of_id:
            list_of_id.append(item[1])
    list_of_id.sort()
    
##Gathering the similar friends between all users. If user 0 has 3 friends, this will create a list with all of user 0's friends, then for user 1,
##this will make a list of all user 1's friends. Output will be a 2d list of all users friends.
    
    friends_list= []
    temp_new_list = []
    
    for ids in listx:
        for item_x in total_list:
            if ids == item_x[0]:
                temp_new_list.append(item_x[1])
            if ids == item_x[1]:
                temp_new_list.append(item_x[0])
        friends_list.append(temp_new_list)
        temp_new_list = []


    name_list = open(file_name2).read().splitlines()
    name_listx = []
    for name in name_list:
        name = name.split("\t")
        name_listx.append(name[1])
        
    return (friends_list, list_of_id, name_listx)
    
    pass
 
def get_int():
    '''None->int or None'''
    num = None
    try:
        num=int(input("Enter an integer for a user ID:").strip())
    except ValueError:
        print("That was not an integer. Please try again.")
    return num           

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name
    
    

##############################
# main
##############################
print("Let's get first file that contains IDs and names:")
file_name1=get_file_name()
print("Let's get the 2nd file that contains pairs of friends as in Assignment 4")
file_name2=get_file_name()


net=Network(file_name1,file_name2)
print("Here are all the people in the network, if the network has at most 20 users:")
if len(net)<=20:
    print(net)


print("\nLet's recommend a friend for a user you specify.")
uid=net.get_uid()
rec=net.recommend(uid)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(net.getCommonFriends(uid,rec)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=net.get_uid()
print("About 2st user ...")
uid2=net.get_uid()
print("Here is the list of common friends of", uid1, "and", uid2)
common=net.getCommonFriends(uid1,uid2)
for item in common:
    print(item, end=" ")



    
