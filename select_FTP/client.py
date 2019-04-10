import socket
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class selectFtpClient:
    def __init__(self):
        self.args = sys.argv
        if len(self.args) > 1:
            self.port = (self.args[1],int(self.args[2]))
        else:
            self.port = ("127.0.0.1",8885)
        self.create_socket()
        self.command_fanout()

    def create_socket(self):
        try:
            self.sk = socket.socket()
            self.sk.connect(self.port)
            print("成功连接FTP服务器")
        except Exception as e:
            print("error:",e)

    def command_fanout(self):
        while True:
            cmd = input(">>>").strip()  #strip()拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list
            if cmd == 'exit()':
                break
            cmd,file = cmd.split()
            if hasattr(self,cmd):   #hasattr判断类中是否有相应属性
                func = getattr(self,cmd)   #getattr(object, name[,default])  获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
                func(cmd,file)
            else:
                print("调用错误")

    def put(self,cmd,file):

        if os.path.isfile(file):
            fileName = os.path.basename(file)
            fileSize = os.path.getsize(file)
            fileInfo = '%S|%s|%s' %(cmd,fileName,fileSize)
            self.sk.send(bytes(fileInfo,encoding='utf8'))
            recvStatus = self.sk.recv(1024)
            print('recvStatus',recvStatus)
            hasSend = 0

            if str(recvStatus,encoding='utf8') == "OK":
                with open(file,'rb') as f:
                    while fileSize > hasSend:
                        contant = f.read(1024)
                        recv_size = len(contant)
                        self.sk.send(contant)
                        hasSend += recv_size
                        s = str(int(hasSend/fileSize*100))+"%"
                        print("正在上传文件："+fileName+"    已经上传："+s)
                print("%s文件上传完毕" %(fileName,))

            else:
                print("文件不存在")

    def get(self,cmd,file):
        pass

if __name__ == '__main__':
    selectFtpClient()