import requests
from bs4 import BeautifulSoup
import re
import os

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
url1 = 'https://music.163.com/discover/toplist?id=3778678'
url2='https://music.163.com/discover/toplist?id=2884035'
url3='https://music.163.com/discover/toplist?id=3779629'
url4= 'https://music.163.com/discover/toplist?id=19723756'
url5= 'https://music.163.com/discover/toplist?id=991319590'
url_list=[url1,url2,url3,url4,url5]
def main_163():
    for i in range(0,6):
        response = requests.get(url_list[i], headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            infor = re.findall(r'<li><a href="/song\?id=(\d+)">(.*?)</a>', str(soup))

            download_path = "d:\\download\\"
            if not os.path.exists(download_path):
                os.makedirs(download_path)

            for title_id, title in infor:
                music_url = f'http://music.163.com/song/media/outer/url?id={title_id}.mp3'
                file_path = os.path.join(download_path, title + '.mp3')

                music_request = requests.get(music_url, headers=header).content
                with open(file_path, "wb") as f:
                    f.write(music_request)

                if os.path.getsize(file_path) < 1024 * 1024:  
                    os.remove(file_path)  
                    print(f"无效文件已删除: {title} {title_id}")
                else:
                    print(f"下载成功: {title}")
