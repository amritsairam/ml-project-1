import logging #any execution that happens we should be able to log that here
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 




#this line is written to generate the file name, whose name would be the time stamp 
#of when it was created and we append .log at the end to indicate that it is a log file.
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#this will create a path for us os.getcwd()will get the currect working directory,then it will create
#a folder named logs and in that the LOG_FILE which was created will be stored
os.makedirs(log_path,exist_ok=True)#it will create the logs folder in the specified path 

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    )


##The current timestamp will be used to generate a log file name in the format "mm_dd_yyyy_hh_mm_ss.log". For example, if the current date and time are June 22, 2023, 10:30:45, the log file name will be "06_22_2023_10_30_45.log".

# A directory named "logs" will be created in the current working directory (cwd).

# The complete file path of the log file will be constructed by joining the current working directory, the "logs" directory, and the log file name. For example, if the current working directory is "downloads/mlproject", the complete file path will be "downloads/mlproject/logs/06_22_2023_10_30_45.log".

# The basicConfig() function from the logging module will be called to configure the logging. The configuration will include:

# Specifying the filename as the complete file path of the log file.
# Setting the log message format to "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s". This format includes the timestamp, line number, logger name, log level, and the actual log message.
# Setting the logging level to INFO, which means log messages with a level of INFO and above will be recorded.
