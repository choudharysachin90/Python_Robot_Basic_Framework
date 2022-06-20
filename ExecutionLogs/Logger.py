import os
import datetime

class Logger:
    rootDirectory="D:\\TestExecutionLogs"
    flag= True
    suiteFolder= ''
    testLogPath=''

    def checkDirectory(self):
        if(not(os.path.isdir(Logger.rootDirectory))):
            os.mkdir(Logger.rootDirectory)
        if(Logger.flag):
            date_time = datetime.datetime.now()
            timeStamp = date_time.strftime("%m%d%Y_%H%M%S")
            Logger.suiteFolder= Logger.rootDirectory+ "\\" +"ExecuteSuite"+ timeStamp
            os.mkdir(Logger.suiteFolder)
            Logger.flag=False


    def Initialize(self,testName):
        self.checkDirectory()
        Logger.testLogPath= Logger.suiteFolder +"\\"+testName+'.log'
        self.testLogFileWriter = open(Logger.testLogPath, 'a')

    def WriteStepInfo(self, MsgType, msg):
        date_time = datetime.datetime.now()
        timeStamp = date_time.strftime("%m:%d:%Y-%H:%M:%S")
        try:
            self.testLogFileWriter.write('{}'.format(timeStamp));
            self.testLogFileWriter.write("  ")
            self.testLogFileWriter.write('{}'.format(MsgType))
            self.testLogFileWriter.write("  ")
            self.testLogFileWriter.write(msg)
        except Exception as e:
            self.testLogFileWriter.write('{}'.format(timeStamp));
            self.testLogFileWriter.write("  ")
            self.testLogFileWriter.write('{}'.format(MsgType.Error))
            self.testLogFileWriter.write("  ")
            self.testLogFileWriter.write(e)

        finally:
            self.testLogFileWriter.close()


    def CloseFile(self):
        self.testLogFileWriter.close()
        self.testLogFileWriter.flush()






