# import drozer util
import sys
sys.path.append('../')

from drozerutil import *
import time

def printUsage():
    print "Usage:\npython %s [packagename] [extra] [extra] ...\n\n[extra]\te.g. string,test,test" % (sys.argv[0])

WAIT_TIME = 5

if len(sys.argv) > 1:
    packagename = sys.argv[1]
else:
    printUsage()
    sys.exit()

#extraslist = [("string", "bla", "bla")]
extraslist = []

if len(sys.argv) > 2:
    for arg in sys.argv[2:]:
        argsplit = arg.split(",")
        if len(argsplit)  != 3:
            printUsage()
            sys.exit()
            
        extraslist.append((argsplit[0], argsplit[1], argsplit[2]))

try:
    drozercon = DrozerConnection("Broadcastfuzzer")
except:
    print "Cannot connect to Drozer Client. Drozer Client up and port forwarded?"
    sys.exit()

receiverlist = drozercon.get_exported_receivers(packagename)

drozercon.logdebug("BROADCASTRECEIVER_FUZZER START")
for receiver in receiverlist:
    intents = receiver.intentfilters
    print "---- Testing %s with extras %s ----" % (receiver.name, str(extraslist))
    for intent in intents:    
        for action in intent.actions:
            try:
                drozercon.sendintent(action, packagename, receiver.name, extraslist)
                drozercon.logdebug("sent intent " + action + " to " + receiver.name)
                print "SENT action %s to receiver %s" % (action, receiver.name)
                #raw_input("WAIT FOR KEY...")
                time.sleep(WAIT_TIME)
            except:
                print "Intent %s:%s sent failure: probably no permission"  % (action, receiver.name)

drozercon.logdebug("BROADCAST FUZZER FINISH")            
