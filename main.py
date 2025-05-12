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
        print(f"HTTP�G���[: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"�ڑ��G���[: {conn_err}")
    except requests.exceptions.Timeout:
        print("�^�C���A�E�g�G���[")
    except requests.exceptions.RequestException as req_err:
        print(f"���N�G�X�g�G���[: {req_err}")
    except Exception as e:
        print(f"�\�����ʃG���[: {e}")
    return None

def parse_data(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # �����Œ��o�������f�[�^�̃��W�b�N���L�q
        # ��: �^�C�g���Ɩ{���𒊏o
        data = []
        for item in soup.find_all('h2'):  # �K�X�^�O��class����ύX
            text = item.get_text(strip=True)
            data.append([text])
        return data
    except AttributeError:
        print('�K�v�ȗv�f��������܂���BHTML�\�����ς�����\��������܂��B')
    except Exception as e:
        print(f"�p�[�X���̃G���[: {e}")
    return []

def save_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"CSV�t�@�C���Ƃ��ĕۑ����܂���: {filename}")
    except Exception as e:
        print(f"CSV�ۑ����̃G���[: {e}")

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        print(f"JSON�t�@�C���Ƃ��ĕۑ����܂���: {filename}")
    except Exception as e:
        print(f"JSON�ۑ����̃G���[: {e}")

if __name__ == "__main__":
    url = "https://example.com"  # �������擾�Ώۂ�URL�ɕύX
    html = fetch_page(url)
    if html:
        data = parse_data(html)
        if data:
            save_to_csv(data, 'scraped_data.csv')
            save_to_json(data, 'scraped_data.json')
