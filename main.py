import requests
from bs4 import BeautifulSoup

def fetch_and_save_html(url, filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        html = str(soup)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"HTMLを {filename} に保存しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    url = "https://example.com"  # 取得したいWebサイトのURLを指定
    fetch_and_save_html(url, "output.html")
