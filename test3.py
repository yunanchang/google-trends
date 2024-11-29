from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def scrape_twitch():
    options = Options()
    options.add_argument("--headless")  # 無頭模式
    options.add_argument("--disable-gpu")  # 禁用 GPU
    options.add_argument("--no-sandbox")  # 禁用沙箱模式
    options.add_argument("--disable-software-rasterizer")  # 禁用軟體光柵化
    options.add_argument("window-size=1920,1080")  # 設置窗口大小

    driver_path = r"chromedriver.exe" 
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 打開 Google Trends 網頁
        url = "https://trends.google.com.tw/trending?geo=TW&hl=zh-TW&hours=4"
        driver.get(url)

        # 增加等待時間，確保頁面加載完成
        driver_wait = WebDriverWait(driver, 10)

        # 抓取主要資料
        mZ3RIc_elements = driver_wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "mZ3RIc"))
        )
        lqv0Cb_elements = driver_wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "lqv0Cb"))
        )
        vdw3Ld_elements = driver_wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "vdw3Ld"))
        )

        # 抓取詳細資料
        td_elements = driver.find_elements(By.CLASS_NAME, "enOdEe-wZVHld-aOtOmf.xm9Xec")
        detailed_data = []
        for td in td_elements:
            try:
                # 尋找所有 `mUIrbf-vQzf8d` 資料
                detailed_infos = td.find_elements(By.CLASS_NAME, "mUIrbf-vQzf8d")
                # 抓取每個子元素的文本並存入列表
                details = [info.text for info in detailed_infos]
            except NoSuchElementException:
                # 若無資料，設定為空列表
                details = []
            detailed_data.append(details)

        # 輸出結果
        for i in range(len(mZ3RIc_elements)):
            if i < len(lqv0Cb_elements) and i < len(vdw3Ld_elements) and i < len(detailed_data):
                details_str = ", ".join(detailed_data[i]) if detailed_data[i] else "無詳細資料"
                print(f"{mZ3RIc_elements[i].text} | {lqv0Cb_elements[i].text} | {vdw3Ld_elements[i].text} | {details_str}")

    except TimeoutException as te:
        print(f"超過等待時間: {te}")
    except Exception as e:
        print(f"抓取資料時發生錯誤: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_twitch()
