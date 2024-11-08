# @Time：2024/8/5 13:53
# @Author: Allan
import datetime
import time
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import pytest
import allure
from common.yaml_config import GentConf
from common.logger import logger
from common.Publicmethods import login, import_learning_courses
from positioned_element import element

page = DrissionpageDriverConfig().driver_config()
current_date = datetime.datetime.now().strftime("%Y-%m-%d")


@pytest.fixture(scope="class", autouse=True)
def some_data():
    login()
    yield
    page.close()
    pass


@allure.feature("供应商管理")
class TestContent:
    @pytest.mark.content2
    @allure.story("课通云")
    def test_create_learning_course(self):
        try:
            # 导入课通云
            # import_learning_courses('test.xlsx')
            page.ele(element.operate(GentConf().get_env('Course_Name'))).next(6).child(1).child(1).click()
            # 编辑
            page.ele(element.编辑).click()
            time.sleep(1)
            page.ele(element.职业工种).clear()
            page.ele(element.职业工种).input('测试')
            page.ele(element.级别).click()
            time.sleep(1)
            page.ele(element.级别).child(4).click()
            page.ele(element.确认按钮).click()
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")

