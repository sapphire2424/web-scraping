import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # 任意のURLに変更

# HTMLを取得
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()
try:
    soup = BeautifulSoup(response.content, "html.parser")
except Exception as e:
    print(f"Error parsing HTML: {e}")

# HTML全体を文字列として取得
html_all = str(soup)

# または整形して取得
html_all_prettified = soup.prettify()

# ファイルに保存
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_all)
