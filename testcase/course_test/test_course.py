# @Time：2024/8/5 13:53
# @Author: Allan
import datetime
import time
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import pytest
import allure
from common.yaml_config import GentConf
from common.logger import logger
from common.Publicmethods import login, import_learning_courses, download_specified_directory
from positioned_element import element

page = DrissionpageDriverConfig().driver_config()
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


@pytest.fixture(scope="class", autouse=True)
def some_data():
    login()
    yield
    page.close()


@allure.feature("供应商管理")
class TestContent:
    @pytest.mark.content1
    @allure.story("课通云")
    def test_create_learning_course(self):
        try:
            # 导入课通云
            import_learning_courses('test.xlsx')
            page.ele(element.operate(GentConf().get_env('course_name'))).next(6).child(1).child(1).click()
            # 编辑
            page.ele(element.编辑).click()
            time.sleep(1)
            page.ele(element.职业工种).clear()
            page.ele(element.职业工种).input('测试')
            page.ele(element.级别).click()
            time.sleep(1)
            page.ele(element.级别).child(4).click()
            page.ele(element.确认按钮).click()
            page.ele(element.供应商).child(1).click()
            career = page.ele(element.operate(GentConf().get_env('course_name'))).next(2).text
            grade = page.ele(element.operate(GentConf().get_env('course_name'))).next(3).text
            logger.info(f"职业/工种：{career},级别：{grade}")
            assert career == '测试' and grade == '高级'
            download_specified_directory(GentConf().get_env('course_name'), './Downloads',
                                         element.operate(GentConf().get_env('course_name')))
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")

    @pytest.mark.content2
    @allure.story("格莱森")
    def test_gleason(self):
        try:
            # 重新加载
            page.ele(element.供应商).child(2).click()
            page.ele(element.重新载入).click()
            page.ele(element.重新载入确认).click()
            time.sleep(5)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            time1 = page.ele(element.operate(GentConf().get_env('gls_name'))).next(5).text
            assert time1 == current_time
            logger.info(f"当前时间为:{current_time},实际获取载入时间为:{time1}")
            page.ele(element.operate(GentConf().get_env('gls_name'))).next(6).child(1).child(1).click()
            page.ele(element.编辑).click()
            time.sleep(1)
            page.ele(element.职业工种).clear()
            page.ele(element.职业工种).input('测试')
            page.ele(element.级别).click()
            time.sleep(1)
            page.ele(element.级别).child(4).click()
            page.ele(element.确认按钮).click()
            page.ele(element.供应商).child(2).click()
            career = page.ele(element.operate(GentConf().get_env('gls_name'))).next(2).text
            grade = page.ele(element.operate(GentConf().get_env('gls_name'))).next(3).text
            logger.info(f"职业/工种：{career},级别：{grade}")
            assert career == '测试' and grade == '高级'
            download_specified_directory(GentConf().get_env('gls_name'), './Downloads',
                                         element.operate(GentConf().get_env('gls_name')))
            page.ele(element.operate(GentConf().get_env('gls_name'))).next(6).child(1).child(3).click()
            page.ele(element.重新载入确认).click()
            time.sleep(3)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            time1 = page.ele(element.operate(GentConf().get_env('gls_name'))).next(5).text
            assert time1 == current_time
            logger.info(f"当前时间为:{current_time},实际获取载入时间为:{time1}")
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")
