import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        connections = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                connections.append(userID, friendID)
        
        # Shuffle
        random.shuffle(connections)

        # Add friends
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = connections[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
    
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue(userID)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.update({v: []})
                for friend in self.friendships[v]:
                    q.enqueue(friend)

            for friend in visited:
                if userID is not friend:
                    path = self.bfs(userID, friend)
                    visited.update({friend: path})
                else:
                    visited.update({userID: [userID]})
            

        return visited

    # bfs to find shortest friendship path
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty set to store visited nodes
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        # While the queue is not empty...
            # Dequeue the first PATH
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # IF VERTEX = TARGET, RETURN PATH
            # If that vertex has not been visited...
                # Mark it as visited
                # Then add A PATH TO all of its neighbors to the back of the queue
                    # Copy the path
                    # Append neighbor to the back of the copy
                    # Enqueue copy
        q = Queue()
        visited = set()
        print('visited', visited)

        q.enqueue([starting_vertex])
        print('q enqueue', q.size())

        while q.size() > 0:
            v = q.dequeue()
            node = v[-1]
            print('node', node)

            if node not in visited:
                for neighbor in self.vertices[node]:
                    path = list(v)
                    print('path pre-append', path)
                    path.append(neighbor)
                    print('path post-append', path)
                    q.enqueue(path)
                    print('q post enqueue path', q.size())
                    if neighbor == destination_vertex:
                        return path
                
                visited.add(node)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
