import requests
from bs4 import BeautifulSoup

url = "https://google.com/"  # 適宜変更

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # HTTPエラーを例外として扱う
    soup = BeautifulSoup(response.content, 'html.parser')
except requests.exceptions.RequestException as e:
    print(f"データ取得中にエラーが発生しました({url}): {e}")
    exit()

# 例: タイトルだけ抽出して保存
title = soup.title.string if soup.title else "No Title"

try:
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(title)
except Exception as e:
    print(f"ファイル保存中にエラーが発生しました: {e}")