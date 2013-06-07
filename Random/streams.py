
def head(str):
    return str and str[0]
    
def tail(str):
    return str and str[1] and str[1]()
    
def stream(head):
    return (head, lambda: Empty)
    
def add(head, str):
    return (head, lambda: str)
    
def getstreamn(n, str):
    i = 0
    while(i < n):
        str = tail(str)
    
    return head(str)
    
def printstream(n, str):
    i = 0
    while(i < n):
        print head(str)
        str = tail(str)
        if not str:
            break
        i += 1
    
def addStreams(si, sj):
    if not si: return sj
    if not sj: return si
    joined = lambda ti=si, tj=sj: addStreams(tail(ti), tail(tj))
    return (head(si) + head(sj), joined)
    
ones = (1, lambda: ones)
integers = (0, lambda: addStreams(ones, integers))

