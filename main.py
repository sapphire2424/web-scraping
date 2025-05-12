import requests
from bs4 import BeautifulSoup
import csv
import json

def fetch_page(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTPエラー: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"接続エラー: {conn_err}")
    except requests.exceptions.Timeout:
        print("タイムアウトエラー")
    except requests.exceptions.RequestException as req_err:
        print(f"リクエストエラー: {req_err}")
    except Exception as e:
        print(f"予期せぬエラー: {e}")
    return None

def parse_data(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # ここで抽出したいデータのロジックを記述
        # 例: タイトルと本文を抽出
        data = []
        for item in soup.find_all('h2'):  # 適宜タグやclass名を変更
            text = item.get_text(strip=True)
            data.append([text])
        return data
    except AttributeError:
        print('必要な要素が見つかりません。HTML構造が変わった可能性があります。')
    except Exception as e:
        print(f"パース中のエラー: {e}")
    return []

def save_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"CSVファイルとして保存しました: {filename}")
    except Exception as e:
        print(f"CSV保存時のエラー: {e}")

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        print(f"JSONファイルとして保存しました: {filename}")
    except Exception as e:
        print(f"JSON保存時のエラー: {e}")

if __name__ == "__main__":
    url = "https://example.com"  # ここを取得対象のURLに変更
    html = fetch_page(url)
    if html:
        data = parse_data(html)
        if data:
            save_to_csv(data, 'scraped_data.csv')
            save_to_json(data, 'scraped_data.json')
