import logging
import datetime

class Logger():
    startTime = None
    endTime = None
    def __init__(self, name, testInfo):
        logging.basicConfig(format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%Y-%m-%d %I:%M:%S",
                            filename='{}.log'.format(name), filemode='w', level=logging.DEBUG)
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("botocore").setLevel(logging.WARNING)
        self.startTime = datetime.datetime.now()
        self.testCaseDesc = testInfo.testcaseDesc
        self.start()

    def info(self, msg):
        logging.info(msg=msg)

    def debug(self, msg):
        logging.debug(msg=msg)

    def warning(self, msg):
        logging.warning(msg=msg)

    def error(self, msg):
        logging.error(msg=msg)

    def start(self):
        self.debug("*************************************************"\
                  "****************************************************")
        self.debug("*************************************** Execute Tests "\
                    "***********************************************")
        self.debug(" ******************************************************"\
                    "***********************************************")
        msg = "Run Started at : " + str(self.startTime)
        self.debug(msg)
        self.debug(" ")
        self.debug(" ")
        self.debug("************************************ Running {} "
                    "*************************************".format(self.testCaseDesc))
        self.debug(" ")
        self.debug("Run Configuration information follows")
        self.debug(" ")
        msg = "Test Target  : " + str("http://test_url")
        self.debug(msg)

    def end(self):
        self.debug("********************************************** Run Complete "\
                  "******************************************")
        self.debug("Starttime : " + str(self.startTime) + " Endtime : " + str(datetime.datetime.now()))