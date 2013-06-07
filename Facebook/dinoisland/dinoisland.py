#!/usr/bin/python

################################################################
# NOTE
# * Lots of warning signs when dinoisland.thrift was generated. Might need to check that out
################################################################

""" dinoisland"""
import sys
sys.path.append('gen-py/')

from com.facebook.puzzles.dinoislands.thrift import Dinosaur
from com.facebook.puzzles.dinoislands.thrift.ttypes import *
from com.facebook.puzzles.dinoislands.thrift.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

EMAIL = "zimkies@hotmail.com"
HIGH_SCORE_NAME = "bengeraldwaronakies"

def main(entity_type):
    try:
        ##############################
        # Connect
        
        # Make socket
        transport = TSocket.TSocket('thriftpuzzle.facebook.com', 9033)
        
        # Buffering is critical. Raw sockets are very slow
        transport = TTransport.TBufferedTransport(transport)
        
        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
       
        # Create a client to use the protocol encoder
        client = Dinosaur.Client(protocol)
       
        # Connect!
        transport.open()
        print "Opened Transport"
        client.registerClient(EMAIL, HIGH_SCORE_NAME, entity_type)
        print client.registerClient(EMAIL, HIGH_SCORE_NAME, entity_type)
        print "Registered Client"
        ##############################
        # Play
    
        
        
        transport.close()
    
    except Thrift.TException, tx:
        print "%s" % (tx.message)
        
if __name__ == "__main__":
    main(0)