from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)

search = driver.find_element_by_id("kw")
search.send_keys("selenium")
btn = driver.find_element_by_id("su")
btn.click()

time.sleep(3)

result = driver.find_element_by_xpath('//*[@id="content_left"]').text
print("结果:/n", result)


