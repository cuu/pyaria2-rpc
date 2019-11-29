import sys

from pyaria2 import Jsonrpc
jsonrpc = Jsonrpc('localhost', 6800)

resp = jsonrpc.getGlobalStat()
print resp["result"]
if( int(resp["result"]["numActive"]) > 0 ):
    resp2 = jsonrpc.tellActive()
    print resp2

if( int(resp["result"]["numWaiting"]) > 0):
    offset = 0
    num = int(resp["result"]["numWaiting"]) 
    resp2 = jsonrpc.tellWaiting(offset,num)
    print resp2

if( int(resp["result"]["numStopped"]) > 0):
    offset = 0
    num = int(resp["result"]["numStopped"])
    print num 
    resp2 = jsonrpc.tellStopped(offset,num)
    print resp2


