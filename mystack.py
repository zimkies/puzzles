
# Create a stack list
class Stacklist():
    def __init__(self):
        self.stacklist = []
        self.length = 0
       
    def pop(self):
        if (self.isempty()):
            return None
        else:
            s =self.stacklist[-1]
            p = s.pop()
            if s.isempty():
                self.stacklist.pop()
                self.length -= 1
            return p
                  
    def push(self,el):
        if (self.isempty() or self.stacklist[-1].isfull()):
            self.stacklist.append(LimitedStack())
            self.length += 1
        s = self.stacklist[-1]
        s.push(el)
            
    def peek(self):
        if (self.isempty()):
            raise Exception("Stack is empty")
        else:
            return self.stacklist[-1].peek()
   
    def isempty(self):
        return (self.length == 0)

# stack
class Stack(object):
    def __init__(self):
        self.stack  = []
       
    def pop(self):
        try:
            x = self.stack.pop()
        except:
            return None
        else:
            return x
    
    def push(self, i):
        self.stack.append(i)
        
    def peek(self):
            return self.stack[-1]
    
    def isempty(self):
        return (len(self.stack) <= 1)
                   

       
# limited stack derived from stack
class LimitedStack(Stack):
    
    def __init__(self):
        self.length = 0
        self.maxlength = 2
        super(LimitedStack, self).__init__()
       
    def pop(self):
        popped = super(LimitedStack, self).pop()
        if (popped):
            self.length -= 1
            return popped
        else:
            self.length = 0
            return popped

    def push(self, el):
        if (self.length == self.maxlength):
            raise Exception("Stack Length exceeded")
        else:
            self.length +=1
            return super(LimitedStack,self).push(el)  
            
    def isfull(self):
        return ( self.length == self.maxlength)

