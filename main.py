from bs4 import BeautifulSoup
import requests

#�f�[�^���W����url
url = "https://google.com/"

#web�����擾
response = requests.get(url) #url��K�X�ύX
soup = BeautifulSoup(response.content, 'html.parser')

#�ۑ���̃t�@�C�����쐬
f = open("data.txt", "w", encoding="utf-8")
f.write(str(soup))