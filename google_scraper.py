import requests
from bs4 import BeautifulSoup

def google_search(query):
    try:
        # Google 搜尋的 URL，將查詢字串加入
        url = f"https://www.google.com/search?q={query}"
        
        # 發送 HTTP GET 請求，模擬瀏覽器的 User-Agent
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        
        # 確認請求是否成功
        if response.status_code != 200:
            print("無法抓取資料，請確認 URL 或網路狀態")
            return
        
        # 使用 BeautifulSoup 解析 HTML 內容
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 提取搜尋結果的標題
        results = soup.select("h3")  # Google 搜尋結果標題通常在 <h3> 標籤內
        
        print(f"搜尋關鍵字：{query}")
        print("結果標題：")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result.text}")
    
    except Exception as e:
        print(f"發生錯誤：{e}")

# 主程式
if __name__ == "__main__":
    keyword = input("請輸入搜尋關鍵字: ")
    google_search(keyword)
