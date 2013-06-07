#!usr/bin/python

""" SimonSimon """
import sys
sys.path.append('./gen-py')

from simonsays import SimonSays
from simonsays.ttypes import *
from simonsays.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

EMAIL = "zimkies@hotmail.com"

def main():
    try:
        # Make socket
        transport = TSocket.TSocket('thriftpuzzle.facebook.com', 9030)
        
        # Buffering is critical. Raw sockets are very slow
        transport = TTransport.TBufferedTransport(transport)
        
        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
       
        # Create a client to use the protocol encoder
        client = SimonSays.Client(protocol)
       
        # Connect!
        transport.open()
       
        client.registerClient(EMAIL)
        
        while 1: 
            colours = client.startTurn()
            for c in colours:
                client.chooseColor(c)
            
            if (client.endTurn() is True):
                client.winGame()
                break
    
        transport.close()
    
    except Thrift.TException, tx:
        print "errormessage: %s" % (tx.message)
        
if __name__ == "__main__":
    main()