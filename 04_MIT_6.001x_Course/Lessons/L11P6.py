class Queue(object):
    def __init__(self):
        self.vals = []
    
    def insert(self, a):
        self.vals.append(a)
        
    def remove(self):
        try:  
            return self.vals.pop(0)
        except:
            raise ValueError()