# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class ChatroomTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_chatroom(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #注册
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        print ("注册成功")
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("input.content-form-signup").click()
        driver.implicitly_wait(30)
        #弹框点击确定
        alert = driver.switch_to_alert()
        alert.accept()
        #登陆
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_css_selector("input.content-form-signup").click()
        print ("登陆成功")
        #打开新窗口
        newwindow = 'window.open("http://localhost:8080/")'
        driver.execute_script(newwindow)
        #移动句柄，对新打开页面进行操作
        driver.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(30)

        #注册
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test2")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("input.content-form-signup").click()
        driver.implicitly_wait(30)
        #弹框点击确定
        alert = driver.switch_to_alert()
        alert.accept()
        #登陆
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test2")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_css_selector("input.content-form-signup").click()


        #打开新窗口
        newwindow = 'window.open("http://localhost:8080/")'
        driver.execute_script(newwindow)
        #移动句柄，对新打开页面进行操作
        driver.switch_to_window(driver.window_handles[2])
        driver.implicitly_wait(30)

        #注册
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test3")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("input.content-form-signup").click()
        driver.implicitly_wait(30)
        #弹框点击确定
        alert = driver.switch_to_alert()
        alert.accept()
        #登陆
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test3")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_css_selector("input.content-form-signup").click()

        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='dope']").clear();
        driver.find_element_by_xpath("//*[@id='dope']").send_keys("hello,yours")#群聊
        driver.find_element_by_id("fasong").click()#点击发送
        time.sleep(2)

        driver.find_element_by_id("1").click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_xpath("//*[@id='dope']").clear();
        driver.find_element_by_xpath("//*[@id='dope']").send_keys("hello")#私聊
        driver.find_element_by_id("fasong").click()#点击发送

        #不关闭，要移动到上一个页面，我们要移动句柄
        driver.switch_to_window(driver.window_handles[1])
        if(driver.find_element_by_class_name("news").is_displayed()):
            print ("群聊成功")
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[0])
        if(driver.find_element_by_class_name("news").is_displayed()):
            print ("私聊成功")


if __name__ == "__main__":
    unittest.main()
