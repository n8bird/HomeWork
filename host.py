import glob
import os.path

NULL = 0

ListOfFiles = ['./raz.txt', './dwa.txt', './trzy.txt']


class sendfile():
    def __init__(self):
        self.sock=socket.socket()
        self.sock.connect(("127.0.0.1", 6666))

    def wyslij(self, fname):
        self.fname=fname
        self.fsize=os.path.getsize(self.fname)
        self.fchmod=13241

        self.string="%s %s" % (self.fname,self.fsize)
        self.sock.send(self.string)
        self.srvresponse=self.sock.recv(256)
        print self.srvresponse
        self.ilepaczek,self.zostalo=self.srvresponse.split()
        self.ilepaczek,self.zostalo=int(self.ilepaczek),int(self.zostalo)

        self.file_open=open(self.fname,"r")
#        self.file_write=open(os.path.join(mydest,self.fname),"w")


        for h in range(self.ilepaczek):
            self.paczka=self.file_open.read(1024)
            #self.file_write.write(self.paczka)
            self.sock.send(self.paczka)

        if self.zostalo:
            self.paczka=file_open.read(self.zostalo)
            #self.file_write.write(self.paczka)
            self.sock.send(self.paczka)

        self.sock.close()
        self.file_open.close()
        #self.file_write.close()

class SocketSub():

        def __init__(self):

            self.TcpPort = 8888
            self.TcpAddr =' 127.0.0.1'
            self.MySocket =socket.socket()
            self.InitBanner = ""

        def OpenComm(self):
            try:
                self.MySocket.connect((TcpAddr, TcpPort))
            except:
                print "DUPA"

        def InitBannerTemplate(self):
            return string("%s %s" % (self.fname,self.fsize))

        def SendInitBanner(self):
            try:
                self.SendPackOfData(InitBannerTemplate)
            except:
                print "DUPA"

        def GetServerResponse(self)


        def ReceivePackOfData(self, RPSize):
            try:
                return self.Mysocket.recv(RPSize)
            except:
                print "DUPASOCKET"


        def SendPackOfData(self, SContent):
            try:
                self.MySocket.send(Scontent)
                return len(Scontent)
            except:
                print "DUPASOCKET"

        def CloseComm(self):
            try:
                return self.MySocket.close
            except:
                print "DUPA SOCKET"

class FileHandler():
        def __init__(self):
            pass

        def Open(self,filename,mode):
            try:
                return open(filename, mode)
            except:
                print "DUPA FILE"

        def Close(self):
            try:
                return self.close()
            except:
                print "DUPA FILE"

        def Write(self, membuffer):
            try:
                return self.write(membuffer)
            except:
                print "PLIKA NIEDOBRA"

        def Read(self, BSize):
            try:
                return self.read(BSize)
            except:
                print "PLIKA NIEDOBRA"




class SendManager():
        def __init__(self,  ListOfFIles):
            self.ListOfFiles=ListOfFIles


class NameProcessing():

        def __init__(self,workdir):
            self.entries = 0
            self.workdir = workdir
            self.ListOfFiles = []
            self.CounterA = 0

        def GetNextName_(self,FileName):
            return self.GetNextFile7Name()

        def CountFilesToProceed(self,ListOfFiles):
            return self.ListOfFiles.len()

        def MergeSingleName(self, TabedNames, FileNameToMerge):
            return self.TabedNames.extend(FileNameToMerge)


class DirectoryOperation():

        def __init__(self):
            self.CurrentDir = self.GetCurrentDir()
            self.counterA = 0
            self.FileSize = 0
            self.Index = 0
            self.MergedItems = []


        def GetCurrentDir(self):
            return os.getcwd()


        def AquireNames(self, CurrentDir):
            return glob.glob(os.path.join(CurrentDir,'*'))

        def CountFilesInList(self, ListOfFiles):
            return ListOfFiles().count

        def PrintListOfFiles(self, ListOfFiles):
            for g in ListOfFiles:
                print (g)

        def MergeFileNameAndSize(self, ListOfFiles):
            for self.FileName in ListOfFiles:
                self.MergedItems.extend([self.FileName, self.GetFileSize(self.FileName)])

            return tuple(self.MergedItems)

        def SliceList(self, ListOfFiles, Index):
            return ListOfFiles[Index]


        def GetFileSize(self, NameOfFile):
            try:
                self.FileSize = os.path.getsize(str(NameOfFile))
                return self.FileSize
            except:
                 return 1




Directory = DirectoryOperation()
Files = Directory.AquireNames(".")
Data = Directory.MergeFileNameAndSize(Files)


