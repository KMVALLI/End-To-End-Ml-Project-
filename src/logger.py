import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # hear log is tring  it will print 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  #  hear we will get logs folder 
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# inordeded to overried the logging functionality we need to set the basic configuration 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


if __name__ == "__main__":
    logging.info("Masthan Logging as started")