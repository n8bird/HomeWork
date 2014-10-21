import socket
import os.path

destdir="wynik"

class ConsoleText():
    def __init__(self):
        pass

    def ScreenPrint(self, stringtmp):
        print (stringtmp)


class ErrorHandling(ConsoleText):

    ErrorMessages = { 1: 'Unable to bind to port',
                      2: 'Unable to delete destination file',
                      3: 'Unable to open file for writing',
                      4: 'Unable to write received data',
                      5: 'Network communication error' }

    def __init__(self):
        pass

    def ShowErrorInfo(self, problemid):
        self.ScreenPrint ("Hello. Problem was found during runtime.")
        self.ScreenPrint (ErrorMessages[problemid])
        raise SystemExit


class Server(ErrorHandling,ConsoleText):

    def __init__(self):
        self.outputfilename = ""
        self.filesize = 0
        self.ipaddr = '127.0.0.1'
        self.ipport = 6666
        self.bufsize = 1024
        self.port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.port.bind((self.ipaddr, self.ipport))
        except:
            self.ShowErrorInfo(1)
        self.port.listen(1)
        self.initpacketsreceived = 0
        self.ScreenPrint( 'server up and running on address %s port %s' % (self.ipaddr, self.ipport))
        self.connection, self.addr = self.port.accept()

    def CloseConnection(self):
        self.connection.close()

    def GluePathAndName(self, filenametmp):
        return os.path.join(destdir,filenametmp)

    def RemoveExistingFile(self, filenametmp):
        if os.path.exists(self.GluePathAndName(filenametmp)):
            try:
                os.remove(self.GluePathAndName(filenametmp))
            except:
                self.ShowErrorInfo(2)

    def SplitHeaderLine(self, line):
        return line.split()

    def OpenFileForWriting(self, filenametmp):
        try:
            self.temp1 = open(self.GluePathAndName(filenametmp),"w")
        except:
            self.ShowErrorInfo(3)
        return self.temp1

    def WriteReceivedToFile(self, bufsize):
        try:
            self.file_write.write(self.connection.recv(bufsize))
        except:
            self.ShowErrorInfo(4)

    def FullPacketsCount(self, fullfilesize):
        return int(int(fullfilesize)/1024)

    def FileTail(self, fullfilesize):
        return int(int(fullfilesize) - self.FullPacketsCount(int(fullfilesize))*1024)

    def SendTransmitDetails(self):
        try:
            self.connection.send("%s %s %s" % (self.packetstoreceive, self.filetailpackets, '\n'))
        except:
            self.ShowErrorInfo(5)

    def ConsoleLog(self):
        self.ScreenPrint('%s \t %s bytes' % (self.outputfilename, self.filesize))

    def ReceiveFile(self):
        self.ScreenPrint('incoming connection from %s port %s' % (self.addr[0], self.addr[1]))
        while 1:
            self.data = self.connection.recv(256)
            if not self.data:
                break

            self.outputfilename, self.filesize = self.SplitHeaderLine(self.data)
            self.RemoveExistingFile(self.outputfilename)
            self.file_write=self.OpenFileForWriting(self.outputfilename)
            self.packetstoreceive=self.FullPacketsCount(self.filesize)
            self.filetailpackets=self.FileTail(self.filesize)
            self.SendTransmitDetails()
            self.ConsoleLog()
            self.ReceiveFullPackets()

    def ReceiveFullPackets(self):
        if self.initpacketsreceived < self.packetstoreceive + 1:
                self.initpacketsreceived += 1
                self.WriteReceivedToFile(self.bufsize)
                self.ReceiveFullPackets()
        else:
                self.WriteReceivedToFile(self.filetailpackets)


nasluch=Server()
nasluch.ReceiveFile()
nasluch.CloseConnection()





