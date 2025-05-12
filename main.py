import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # �C�ӂ�URL�ɕύX

# HTML���擾
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()
try:
    soup = BeautifulSoup(response.content, "html.parser")
except Exception as e:
    print(f"Error parsing HTML: {e}")

# HTML�S�̂𕶎���Ƃ��Ď擾
html_all = str(soup)

# �܂��͐��`���Ď擾
html_all_prettified = soup.prettify()

# �t�@�C���ɕۑ�
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_all)
