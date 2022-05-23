import os
from time import sleep, strftime, localtime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = f"{os.getcwd()}/msedgedriver.exe"
driver = webdriver.Edge(PATH)
print(f'{strftime("%H:%M:%S", localtime())} 初始化腳本瀏覽器...')

def debugTime():
    return strftime("%H:%M:%S", localtime())

def eCareEvaluate():
    eCareUrl = "https://ecare.nfu.edu.tw/"
    driver.get(eCareUrl)
    print(f"{debugTime()} 請輸入帳號密碼及驗證碼並進行登入...")
    try:
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CLASS_NAME, "sidebar-menu")))
    except:
        print(f"{debugTime()} 登入失敗，請重新執行程式...")
        driver.quit()
    driver.get(f"{eCareUrl}aaiqry/poll")
    print(f"{debugTime()} eCare系統登入成功...")
    print(f"{debugTime()} 進入評量系統...")
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CLASS_NAME, "tab_content")))
    print(f"{debugTime()} 取得評量按鈕...")
    sleep(0.3)
    while True:
        try:
            driver.find_element(by=By.LINK_TEXT, value="點此進入期末評量").click()
        except:
            print(f"{debugTime()} 已完成所有評量...")
            driver.quit()
            break
        
        print(f"{debugTime()} 進入評量頁面...")
        sleep(0.3)
        print(f"{debugTime()} 開始執行自動填寫評量...")
        driver.execute_script("""
        $("input[value='5']").click();
        $(".ansA[value='2']").click();
        $(".ansB[value='2']").click();
        $(".ansC[value='1']").click();
        $(".ansD[value='2']").click();
        $(".ansE[value='2']").click();
        $(".ansF[value='1']").click();
        """)
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/section[2]/div/div/b/table/tbody/tr/td/form/textarea[1]").send_keys("無")
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/section[2]/div/div/b/table/tbody/tr/td/form/textarea[2]").send_keys("投影機、麥克風、電腦")
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/section[2]/div/div/b/table/tbody/tr/td/form/textarea[3]").send_keys("無")
        print(f"{debugTime()} 填寫評量完畢...")
        sleep(0.3)
        driver.find_element(by=By.ID, value="submit").click()
        print(f"{debugTime()} 送出評量結果...")
        sleep(0.3)
        driver.find_element(by=By.LINK_TEXT, value="按此回評量列表").click()
        print(f"{debugTime()} 回到評量列表...")
        sleep(0.3)

if __name__ == "__main__":
    eCareEvaluate()