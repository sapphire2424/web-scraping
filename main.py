import requests
from bs4 import BeautifulSoup

url = "https://google.com/"  # �K�X�ύX

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # HTTP�G���[���O�Ƃ��Ĉ���
    soup = BeautifulSoup(response.content, 'html.parser')
except requests.exceptions.RequestException as e:
    print(f"�f�[�^�擾���ɃG���[���������܂���({url}): {e}")
    exit()

# ��: �^�C�g���������o���ĕۑ�
title = soup.title.string if soup.title else "No Title"

try:
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(title)
except Exception as e:
    print(f"�t�@�C���ۑ����ɃG���[���������܂���: {e}")