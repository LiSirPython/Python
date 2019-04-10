import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('conn is: ',self.request)   #conn
        print('addr is: ',self.client_address)  #addr

        while True:
            try:
                #收消息
                data = self.request.recv(1024)
                if not data:break
                print('收到客户端的消息是: ',data,self.client_address)

                #发消息
                self.request.sendall(data.upper())

            except Exception as e:
                print(e)
                break



if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)  # 多线程
    s.serve_forever()