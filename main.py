#KD-TREE PROJECT
#Authors: Micki Eustache, 

class KDTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class KDTree:
    def __init__(self, k):
        self.root = None
        self.k = k
        self.count = 0

    def insert(self, value):
        if self.root == None:
            self.root = KDTNode(value)
            self.count += 1
            return
        
        current = self.root
        depth = 0

        while True:
            cd = depth % self.k

            if value[cd] < current.value[cd]:
                if current.left is None:
                    current.left = KDTNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = KDTNode(value)
                    break
                current = current.right

            depth += 1
        self.count += 1

    def __len__(self):
        return self.count
    
    def __contains__(self, value):
        current = self.root
        depth = 0

        while current is not None:
            if value == current.value:
                return True

            cd = depth % self.k

            if value[cd] < current.value[cd]:
                current = current.left
            else:
                current = current.right

            depth += 1

        return False
    
    def delete(self):
        pass

    def nearest(self):
        pass