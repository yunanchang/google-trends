from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def scrape_twitch():
    options = Options()
    options.add_argument("--headless")  # 無頭模式
    options.add_argument("--disable-gpu")  # 禁用 GPU
    options.add_argument("--no-sandbox")  # 禁用沙箱模式
    options.add_argument("--disable-software-rasterizer")  # 禁用軟體光柵化
    options.add_argument("window-size=1920,1080")  # 設置窗口大小

    driver_path = r"chromedriver.exe"  # 請確保已經放置好正確的 chromedriver 路徑
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 打開 Google Trends 網頁
        url = "https://trends.google.com.tw/trending?geo=TW&hl=zh-TW&hours=4"
        driver.get(url)

        # 增加等待時間，確保頁面加載完成
        driver_wait = WebDriverWait(driver, 10)  # 增加等待時間為10秒

        # 等待所有 class="mZ3RIc" 的元素可見
        elements = driver_wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "mZ3RIc"))
        )

        # 遍歷所有抓取到的元素並打印它們的文本內容
        for element in elements:
            print(element.text)  # 打印每個元素的文本內容

    except TimeoutException as te:
        print(f"超過等待時間: {te}")
    except Exception as e:
        print(f"抓取資料時發生錯誤: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_twitch()
