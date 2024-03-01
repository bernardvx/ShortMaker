from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



driver = webdriver.Firefox()
#open login page
driver.get("https://login.aliexpress.com/?return_url=https%3A%2F%2Fwww.aliexpress.com%2Fp%2Ftrade%2Fconfirm.html%3FobjectId%3D1005001877136240%26from%3Daliexpress%26countryCode%3DAL%26shippingCompany%3DAE_CN_SUPER_ECONOMY_G%26provinceCode%3D%26cityCode%3D%26promiseId%3D%26aeOrderFrom%3Dmain_detail%26skuAttr%3D200000182%253A691%26skuId%3D12000017992224772%26skucustomAttr%3D%26quantity%3D1%26spm%3Da2g0o.detail.0.0%26curPageLogUid%3D1674297657599_y3bIJY%26curPagePriceUid%3D1674297657599_y3bIJY")
time.sleep(10)
username =  driver.find_element(By.ID, "fm-login-id")
username.send_keys('evaleka111@gmail.com')

password = driver.find_element(By.ID, "fm-login-password")
password.send_keys('Automated1!')

login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()
time.sleep(20)
try:
    slider = EC.presence_of_element_located((By.XPATH, "//span[@id='nc_1_n1z']"))
#    slider_end = EC.presence_of_element_located((By.XPATH, "//div[@class=' custom-dialog-wrapper']"))
    slide = ActionChains(driver)
 #   slide.drag_and_drop_by_offset(slider, 60, 0).perform()
finally:
    print('worked')

#get product page only by excact link
driver.get("https://www.aliexpress.com/p/trade/confirm.html?objectId=1005002350952975&from=aliexpress&countryCode=AL&shippingCompany=CAINIAO_STANDARD&provinceCode=&cityCode=&aeOrderFrom=main_detail&skuAttr=200000182%3A193&skuId=12000023368692244&skucustomAttr=&quantity=1&spm=a2g0o.detail.0.0&curPageLogUid=")

#addres of order
time.sleep(15)
add_address = driver.find_element(By.XPATH, "//button[@class='comet-btn comet-btn-link pl-address-item__new-btn']")
add_address.click()

time.sleep(20)
country = driver.find_element(By.XPATH, "//span[@class='next-select-values next-input-text-field']")
time.sleep(10)
#add_country = driver.find_element(By.XPATH, "//span[@class='next-select-values next-input-text-field']")
country.send_keys("France")
country.send_keys(Keys.Return)

#driver.get("https://www.aliexpress.com/item/32854016267.html?spm=a2g0o.productlist.main.89.16961c20orUtfj&algo_pvid=0ea5e87f-b090-468c-b802-c82b6048d47a&algo_exp_id=0ea5e87f-b090-468c-b802-c82b6048d47a-44&pdp_ext_f=%7B%22sku_id%22%3A%2265445776002%22%7D&pdp_npi=2%40dis%21ALL%21612.2%21428.54%21%21%21%21%21%40211bd7d616744281049078830d06d9%2165445776002%21sea&curPageLogUid=Qs3IqLJLnVbS")
#driver.quit()

