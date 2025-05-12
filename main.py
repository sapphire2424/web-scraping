from bs4 import BeautifulSoup
import requests

#データ収集するurl
url = "https://google.com/"

#web情報を取得
try:
    response = requests.get(url) #urlを適宜変更
    soup = BeautifulSoup(response.content, 'html.parser')
except requests.exceptions.RequestException as e:
    print(f"データ取得中にエラーが発生しました( {url} ): {e}")
    exit()

#保存先のファイルを作成
f = open("data.txt", "w", encoding="utf-8")
f.write(str(soup))