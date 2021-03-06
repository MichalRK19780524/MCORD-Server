#import network
import _thread
import socket as usocket
import json as ujson

CMD_LIMIT=600
#Functions which process requests
def remote_mult(obj):
  return ('OK', obj[1]*obj[2])
  
def sum_vals(obj):
  res = 0
  for v in obj[1:]:
      res += v
  return ('OK', res)

def remote_div(obj):
  if obj[2] == 0:
      return ('ERR','I can not divide by 0')
  return ('OK', obj[1]/obj[2])

def return_text(obj):
    text = obj[1] + obj[2] + ' : this is text send to server'
    return ('OK',text)


#Table of functions
func={
   'mult':remote_mult,
   'sum':sum_vals,
   'div': remote_div,
   'rettext': return_text,
  }
  
class ctlsrv():
    def __init__(self):
        # Start Ethernet
        #self.lan = network.LAN()
        #self.lan.active(True)
        # Start server
        self.srvthread = None
        self.runflag = False

    def srv_handle(self,port):
        addr = usocket.getaddrinfo('0.0.0.0', port)[0][-1]
        print(addr)
        s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
        s.bind(addr)
        print(s)
        s.listen(1)
        print('listening on', addr)
        while self.runflag:
            cl, addr = s.accept()
            sockFile = cl.makefile()
            print('client connected from', addr)
            cl.sendall(b"AFE hub 1.0\n")
            while True:
                line = sockFile.readline(CMD_LIMIT)
                print(line)
                if not line or line == b'\n' or line == b'\r\n':
                    break
                if line[-1] != '\n'[0]:
                    print([hex(ord(i)) for i in line])
                    self.send_msg(cl,('ERR', 'Line too long'))
                    break
                #Parse the line and execute the command
                try:
                    cmd = ujson.loads(line)
                    res = func[cmd[0]](cmd)
                except Exception as e:
                    res = ('ERR',str(e))    
                self.send_msg(cl,res)
            cl.close()
    def send_msg(self,cl,msg):
        cl.sendall((ujson.dumps(msg)+"\n").encode("utf8"))
		        
    def run(self,port):
        if self.srvthread:
            raise(Exception("Server already running"))
        self.runflag = True
        self.srvthread = _thread.start_new_thread(self.srv_handle,(port,))
        return
        
    def stop(self):
        self.runflag = False
        return

