import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 15270
ip = '127.0.0.1'
def open_connection():
    soc.connect((ip, port))
    print('-----Connection Opened-----')

def close_connection():
    soc.close()
    print('-----Connection Closed-----')

def send_packet(payload):
    print('-----Sending ' + payload + ' -----')
    soc.send(payload.encode())
    msg = soc.recv(128)
    print('-----Response: ' + msg + ' -----')


open_connection()

print('======Testing SECURITY rule======')
send_packet('SECURITY')            # must match
send_packet('security')            # must not match
send_packet('Test')               # must not match

print('\n======Testing Hello World rule======')
send_packet('HelloWorld')          # must not match
send_packet('Hello World')         # must match
send_packet('Hello  World')        # must match
send_packet('Hello     World')     # must match
send_packet('Test')                # must not match

print('\n======Testing Capital Quoted Word rule======')
send_packet('"Word"')              # must match
send_packet('"HELLO"')            # must match
send_packet('"Abc"')               # must not match
send_packet('"MoreThan7Letters"')  # must not match
send_packet('"test"')              # must not match
send_packet('"Test"')              # must not match

print('\n======Testing NI number rule======')
send_packet('AB123456A')           # must match
send_packet('AB 12 34 56')         # must match
send_packet('EZ 123456 F')         # must match
send_packet('PO 12 34 56 F')       # must not match
send_packet('DG 12 34 56')         # must not match
send_packet('AB 12 34 56 X')       # must not match

close_connection()