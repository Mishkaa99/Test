# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")


# class TestMainPage1():
#     def test_guest_should_see_login_link(self, browser):
#         # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")




# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():

#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         print("start test1")
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#         print("finish test1")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         print("start test2")
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#         print("finish test2")



# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")



# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     return browser


# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")



# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# class TestMainPage1():

#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.browser = webdriver.Chrome()

#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()

#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# class TestMainPage2():

#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.Chrome()

#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()

#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")




# import pytest

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException


# def test_exception1():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element_by_css_selector("button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally: 
#         browser.quit()

# def test_exception2():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element_by_css_selector("no_such_button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally: 
#         browser.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import unittest




# class TestAbs(unittest.TestCase):
    
#     def test_abs1(self):
#         link = "http://suninjuly.github.io/registration1.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
    
#         # Ваш код, который заполняет обязательные поля
#         input1 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[1]/input")
#         input1.send_keys("Petr")
    
#         input2 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/input")
#         input2.send_keys("Petrov")
    
#         input3 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[3]/input")
#         input3.send_keys("Petr1@mail.ru")
    
#         input4 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[1]/input") 
#         input4.send_keys("891779755842")
    
#         input5 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[2]/input")
#         input5.send_keys("Ru")
#         # Отправляем заполненную форму
#         button = browser.find_element_by_css_selector("button.btn")
#         button.click()
    
#         # Проверяем, что смогли зарегистрироваться
#         # ждем загрузки страницы
#         time.sleep(1)
    
#         # находим элемент, содержащий текст
#         welcome_text_elt = browser.find_element_by_tag_name("h1")
#         # записываем в переменную welcome_text текст из элемента welcome_text_elt
#         welcome_text = welcome_text_elt.text
    
#         # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
         
#         assert("Congratulations! You have successfully registered!" == welcome_text)
    
        
#     def test_abs2(self):
#         link = "http://suninjuly.github.io/registration2.html"
#         browser = webdriver.Chrome()
#         browser.get(link)

#         # Ваш код, который заполняет обязательные поля
#         input1 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[1]/input")
#         input1.send_keys("Petr")

#         input2 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/input")
#         input2.send_keys("Petrov")

#         input3 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[3]/input")
#         input3.send_keys("Petr1@mail.ru")

#         input4 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[1]/input") 
#         input4.send_keys("891779755842")

#         input5 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[2]/input")
#         input5.send_keys("Ru")
#         # Отправляем заполненную форму
#         button = browser.find_element_by_css_selector("button.btn")
#         button.click()

#         # Проверяем, что смогли зарегистрироваться
#         # ждем загрузки страницы
#         time.sleep(1)

#         # находим элемент, содержащий текст
#         welcome_text_elt = browser.find_element_by_tag_name("h1")
#         # записываем в переменную welcome_text текст из элемента welcome_text_elt
#         welcome_text = welcome_text_elt.text

#         # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

#         assert("Congratulations! You have successfully registered!" == welcome_text)

# if __name__ == "__main__":
#     unittest.main()
        


    





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import math
# import time
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     line = "http://suninjuly.github.io/explicit_wait2.html"
#     browser = webdriver.Chrome()
#     browser.get(line)

#     money = WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.ID, "price"),"$100")
#     )
#     print(money)
#     if money == True:
#         browser.find_element_by_id("book").click()

#     x = browser.find_element_by_id("input_value")
#     x_text = int(x.text)
#     y = calc(x_text)
#     input1 = browser.find_element_by_id("answer")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
#     input1.send_keys(y)

#     button = browser.find_element_by_id("solve")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()

#     # # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#     # button = WebDriverWait(browser, 5).until(
#     #     EC.element_to_be_clickable((By.ID, "verify"))
#     # )
#     # # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
#     # button = WebDriverWait(browser, 5).until_not(
#     #     EC.element_to_be_clickable((By.ID, "verify"))
#     # )

# finally:
#     # говорим WebDriver ждать все элементы в течение 5 секунд
#     # browser.implicitly_wait(15)
#     time.sleep(13)
#     browser.quit()



# from selenium import webdriver
# import time
# import math
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
    
#     input = browser.find_element_by_tag_name("button")
#     input.click()

#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)

#     x = browser.find_element_by_id("input_value")
#     x_text = int(x.text)
#     y = calc(x_text)
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     browser.find_element_by_tag_name("button").click()
    

# finally:
#     time.sleep(15)
#     browser.quit()



# from selenium import webdriver
# import time
# import math
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     button1 = browser.find_element_by_css_selector("[type='submit']")
#     button1.click()

#     alert = browser.switch_to.alert
#     alert.accept()

#     x = browser.find_element_by_id("input_value")
#     x_text = int(x.text)
#     y = calc(x_text)
#     input = browser.find_element_by_id("answer")
#     input.send_keys(y)
#     browser.find_element_by_tag_name("button").click()
    

# finally:
#     time.sleep(15)
#     browser.quit()





# from selenium import webdriver
# import time
# import os

# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     name1 = browser.find_element_by_name("firstname")
#     name1.send_keys("Max")

#     name2 = browser.find_element_by_name("lastname")
#     name2.send_keys("Pipkin")

#     mail = browser.find_element_by_name("email")
#     mail.send_keys("Pipka@mail.ru")

#     fil = browser.find_element_by_id("file")
#     file = os.path.abspath(os.path.dirname(__file__))

#     print("Otlichie:")
#     print(os.path.abspath(__file__))
#     print("===================")
#     print(os.path.abspath(os.path.dirname(__file__)))
   
#     file_path = os.path.join(file,'test.txt')
#     fil.send_keys(file_path)

#     button = browser.find_element_by_tag_name("button")
#     button.click()

# finally:
#     time.sleep(15)
#     browser.quit()





# from selenium import webdriver
# import time
# import math
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     browser = webdriver.Chrome()
#     link = "http://SunInJuly.github.io/execute_script.html"
#     browser.get(link)

#     x = browser.find_element_by_id("input_value")
#     x_text = x.text
#     x = int(x_text)
#     print(x)
#     y = calc(x)
#     y_text = y
#     input = browser.find_element_by_id("answer")
#     input.send_keys(y_text)
    
#     robo = browser.find_element_by_id("robotCheckbox")
#     robo.click()

#     rule = browser.find_element_by_id("robotsRule")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
#     rule.click()

#     button = browser.find_element_by_tag_name("button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()

# finally:
#     time.sleep(15)
#     browser.quit()






# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# try:
#   link = " http://suninjuly.github.io/selects2.html"
#   browser = webdriver.Chrome()
#   browser.get(link)
  
#   num1 = browser.find_element_by_id("num1")
#   text_num1 = num1.text
#   print(text_num1)
#   num2 = browser.find_element_by_id("num2")
#   text_num2 = num2.text
#   print(text_num2)
#   num3 = int(text_num1) + int(text_num2)
#   print(num3)
#   num33 = str(num3)
#   print(num33)
#   test = browser.find_element_by_id("dropdown")
#   test.click()


#   select = Select(browser.find_element_by_tag_name("select"))
#   select.select_by_visible_text(num33)

#   button = browser.find_element_by_class_name("btn.btn-default")
#   button.click()



# finally:
#   time.sleep(5)
#   browser.quit()




# import math
# import time
# from selenium import webdriver

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     line = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(line)

#     x_element = browser.find_element_by_id("treasure")
#     x_elementt = x_element.get_attribute("valuex") 
#     print(x_elementt)  
#     x = x_elementt
#     y = calc(x)
#     y_element = browser.find_element_by_id("answer")
#     y_element.send_keys(y)
#     chek = browser.find_element_by_id("robotCheckbox")
#     chek.click()
#     robo = browser.find_element_by_id("robotsRule")
#     robo.click()
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()


# finally:
#     time.sleep(10)
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# try: 
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element_by_class_name("form-control.first")
#     input1.send_keys("Petr")

#     input2 = browser.find_element_by_class_name("form-control.second")
#     input2.send_keys("Petrov")

#     input3 = browser.find_element_by_class_name("form-control.third")
#     input3.send_keys("Petr1@mail.ru")

#     input4 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[1]/input") 
#     input4.send_keys("891779755842")

#     input5 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[2]/input")
#     input5.send_keys("Ru")
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)

#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text

#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 

# link = "http://suninjuly.github.io/find_xpath_form"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//form/div[6]/button[@type='submit']")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла





# from selenium import webdriver
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#         element.send_keys("Мой ответ")

#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла






# from selenium import webdriver
# import time 
# import math

# link = "http://suninjuly.github.io/find_link_text"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     number = str(math.ceil(math.pow(math.pi, math.e)*10000))
#     link1 = browser.find_element_by_link_text(number)
#     link1.click()

#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла