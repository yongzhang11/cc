import time

from config.BrowserDriver import drissionpage_driver
from common.yaml_config import GentConf

page_driver = drissionpage_driver.DrissionpageDriverConfig.driver_config(self=None)


def login():
    page_driver.get(GentConf().get_env("CC_URL"))
    page_driver.ele("#username").input(GentConf().get_env("username"))
    page_driver.ele("#pwd").input(GentConf().get_env("password"))
    page_driver.ele("@class=btn btn-primary btn-block ").click()


def import_learning_courses(zipname):
    page_driver.ele('@class=btn btn-primary').check()
    page_driver.set.upload_files('./file/{}'.format(zipname))
    page_driver('#excelfile-upload-area').click()
    page_driver.wait.upload_paths_inputted()
    page_driver.ele('#import-excel').click()
    time.sleep(2)
    page_driver.ele('@class=btn  btn-primary').click()
