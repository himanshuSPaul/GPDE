import argparse
import configparser
import datetime
import sys,os
from pathlib import Path



class CustomLogger:

    __LOG_FILE_NAME__= ''
    __LOG_DIR__ = ''
    
    __config__= configparser.ConfigParser()
    __config__.read('config.ini')
    

    # If log file path is provided by user
    def __init__(self,logfilename) -> None:
        if logfilename is not None :
            self.__LOG_DIR__ = '\\'.join(logfilename.split("\\")[:-1])
            self.__LOG_FILE_NAME__= logfilename
            
        else :
            print("Using Default Log Folder")
            self.__LOG_DIR__= self.__config__.get('global','logfolder')
            logfilename = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S.log')
            logfilepath=self.__LOG_DIR__+'\\'+logfilename
            self.__LOG_FILE_NAME__= logfilepath

        print(f"Checking if Log Directory {self.__LOG_DIR__} Exist",Path(self.__LOG_DIR__).is_dir())

        if not Path(self.__LOG_DIR__).is_dir():
            print("Creating Log Dir :",self.__LOG_DIR__)
            os.mkdir(self.__LOG_DIR__)
            print("Log Directory Created : ",Path(self.__LOG_DIR__).is_dir())

    def get_log_dir_path(self):
        return self.__LOG_DIR__

    def get_log_filename(self):
        return self.__LOG_FILE_NAME__
    
    def log(self,message, writeToConsole='y',writeToLogFile='y'):
        dt = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
        
        if writeToConsole.upper()=='Y':
            print(dt + " - " + message)
        
        if writeToLogFile.upper() =='Y':
            with open(self.__LOG_FILE_NAME__,"a+") as f:
                f.write(dt + ' - '+message+'\n')
                f.flush()
                os.fsync(f.fileno())



        









if __name__ == '__main__':
    argparse=argparse.ArgumentParser()
    argparse.add_argument('-l',
                          '--logpath',
                          help='Pass Log Folder Path ')
    args= argparse.parse_args()

    if args.logpath is not None:
        if '\\' not in args.logpath:
            print("Invalid Log Path !!! Provide Absolute Log Path")
            sys.exit()
        else :
            logger =CustomLogger(args.logpath)
    else :
        logger =CustomLogger(None)
    # print("LogDir Name : ",logger.get_log_dir_path())
    # print("LogFile Name : ",logger.get_log_filename())
    logger.log("Hello LOg")
