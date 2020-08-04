f = open("c:/KenPyfiles/kenScanresult",'a')

import socket

server = input("Enter a Host to Scan:")
remoteServerIP=socket.gethostbyname(server)
print("server ip is:", remoteServerIP)

# Start date & time
from datetime import datetime
startTimestamp=datetime.now()
print("Monday date is:",datetime.month,datetime.now())

f = open("C:/KenPyfiles/KenScanresult.txt",'w')
f.write("I love Python ")
print("_"*60,file=f)
print("Scanning host.",server,file=f)
print("_"*60,file=f)
print(startTimestamp,file=f)
# Start time
import time
start=time.time()
# Start socket stream


try:
    for port in range(1,1026):
        sock:socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        print("port=",port, "port result=",result)
        if result == 0:
            print("Port {}: is OPEN".format(port),file=f)
        sock.close()

        if port == 1025:
            break

# Exceptions
except KeyboardInterrupt:
    print("ERROR! Scan was interrupted by user",file=f)
    sys.exit()

except socket.gaierror:
    print("ERROR! Host name could not be resolved. Exiting Scan.",file=f)
    sys.exit()

except socket.error:
    print("ERROR! Could not locate server.",file=f)
    sys.exit()
from datetime import datetime
endTimestamp = datetime.now()
print(endTimestamp,file=f)
# Print total time the scan took
print("Scan finished in",time.time() - start,"seconds.",file=f)

f.close()
