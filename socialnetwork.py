# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
# Some details:  Each sentence will be separated from one another with only
# a period (there will not be whitespace or new lines between sentences)
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

example_input_alternate="""John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure

def make_list(connection_type, line): #makes a list of all connections of the type friend or game depending on what it is in the line
    connections = []
    line = line[line.find(connection_type) + len(connection_type):] #so starts looking after the connection type is identified as these are the connections
    splitted = (line.split(',')) #.split(',') splits whenever there is a comma
    for items in splitted:
        connections.append(items[1:]) #removes the space and adds it to the connection
    return connections

def create_data_structure(data):
    network = {}
    lines = data.split('.')
    for line in lines:
        name = line[:line.find(' ')] # name of the person at the beginning of each line
        if name == '': 
            None
        else:
            if name not in network:
                network[name] = {'Friends': [], 'Games': []}
            if 'is connected to' in line:
                network[name]['Friends'] = make_list('is connected to', line)#network[line[:line.find(' ')]] gives the guys name in the dictionary
            if 'likes to play' in line:
                network[name]['Games'] = make_list('likes to play', line)
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.  
def get_connections(network, user):
    if user not in network:
        return None
    return network[user]["Friends"]

# -------------------------------------------------------------
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user not in network:
        return None
    return network[user]["Games"]
# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B not in network[user_A]['Friends']: # no use adding it if it's already there
        network[user_A]['Friends'].append(user_B)
    return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.
def add_new_user(network, user, games):
    if user not in network:
        network[user] = {'Friends':[], 'Games': games}
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    secondary_friends = []
    if user not in network:
        return None
    for friends in network[user]["Friends"]:
        for friend_of_friend in network[friends]["Friends"]: #list of friends friends
            if friend_of_friend not in secondary_friends: #prevents the same person appearing in the list twice
                secondary_friends.append(friend_of_friend)
    return secondary_friends

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.

def connections_in_common(network, user_A, user_B):
    shared_friends = 0
    if (user_A not in network) or (user_B not in network): 
        return False
    for friends in network[user_A]["Friends"]:
        if friends in network[user_B]["Friends"]:
            shared_friends += 1
    return shared_friends

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def create_node(state, parent_node): # creates a node for use in paths
    node = {'State': state, 'Path': parent_node['Path'] + [state]} #path will thus keep track of the path to this state
    return node

def goal_test(friend, path_map): #tests to see if the friend is in explored yet, done using explored instead of frontier to guarantee this is the shortest path
    for nodes in path_map['Explored']:
        if friend == nodes['State']:
            return nodes['Path']
        
def explored(node, path_map): #performed when a node has been explored to take it out of the frontier and place it into the explored list
    path_map['Frontier'].remove(node)
    path_map['Explored'].append(node)

def not_previously_explored(friend, explored_list): #tests to see if this path has been done before
    for nodes in explored_list:
        if friend == nodes['State']:
            return False
    return True

def explore_frontier(node, network, path_map): #adds all friends of this node not previously explored into the frontier and puts this node as explored
    for friend in network[node['State']]['Friends']:
        if not_previously_explored(friend, path_map['Explored']):
            path_map['Frontier'].append(create_node(friend, node))#adds this new friend as a new node in the frontier
    explored(node, path_map)
            
def path_to_friend(network, user_A, user_B):
    if type(user_A) is not dict: #converts the entered start friend into a dictionary as they are easier to work with
        if user_A not in network or user_B not in network:
            return None
        user_A = {'Frontier': [{'State': user_A, 'Path': [user_A]}], 'Explored':[]} #user_A now acts as a sort of path map to keep track of what users have been explored
    if goal_test(user_B, user_A):
        return goal_test(user_B, user_A)
    if user_A['Frontier'] == []: #No more frontier, all paths have been explored
        return None
    current_node = user_A['Frontier'][0] #next node to look at is the first one in the frontier,ensures always lowest level being looked at
    explore_frontier(current_node, network, user_A)
    return path_to_friend(network, user_A, user_B)#if it wasn't found go through the next node and repeat the process

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun! 

"""
Recommends a new game for a user based upon their own game interests
and what their friends are playing
"""

def add_to_recommended(user, recommendation_score, network):#adds scores for the games to recommendation_score
#could be changed to add in a weighting feature if say research shows that friends opinions matter more than similar gamers or vice versa
    for game in network[user]['Games']:
        if game in recommendation_score:
            recommendation_score[game] +=1
        else:
            recommendation_score[game] = 1

def similar_games(user, recommendation_score, network): #produces a dictionary of games and scores for how similar other games are to this game
#uses what other users who play this game play to see the similarity
    for game in network[user]['Games']:
        for users in network:
            if game in network[users]['Games']:
                add_to_recommended(users, recommendation_score, network)

def friends_games(user, recommendation_score, network): #gives a point to each game a friend plays, or more if lots of friends play it
    for friend in network[user]['Friends']:
        add_to_recommended(friend, recommendation_score, network)

def games_already_liked(user, recommendation_score, network):
    real_recommendation_score = {} #recommendation score without the ones already used by the user
    for game in recommendation_score:
        if game not in network[user]['Games']: #so the ones that are in the users game list won't be added
            real_recommendation_score[game] = recommendation_score[game]
    return real_recommendation_score

def choose_highest_score(recommendation_score): #chooses the highest score in the recommendation_score dictionary
    highest, score = None, 0
    for game in recommendation_score:
        if recommendation_score[game] > score:
            highest, score = game, recommendation_score[game]
    return highest


def recommend_new_game(user, network): #main procedure, use it and it recommends a game for a particular user
    recommendation_score = {} #this dictionary keeps a count of scores that various games have for the user
    similar_games(user, recommendation_score, network) #based on what other users who play the games they play
    friends_games(user, recommendation_score, network) #and based off what their friends are playing
    recommendation_score = games_already_liked(user, recommendation_score, network) #this step removes the games the user already plays to make sure they don't show up
    return choose_highest_score(recommendation_score)
 
net = create_data_structure(example_input)

#print (net)
#print path_to_friend(net, 'John', 'Levi')
#print net
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print add_connection(net, "John", "Freda")
print (get_secondary_connections(net, "John"))
#print connections_in_common(net, "Mercedes", "John")
#print connections_in_common(net,"Freda","Freda")

#print (recommend_games("Freda", net))
