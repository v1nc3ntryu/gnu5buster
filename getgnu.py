# 그누보드5를 같이 올리려니 용량도 크고 버전업 따라가기 아주 귀찮습니다..
# 그래서 그냥 매번 그누보드 깃에서 다운 받게 짰어유
import requests, os
from zipfile import ZipFile

def download(URL): # URL에서 zip파일 다운로드
    file = requests.get(URL, stream = True)
      
    with open("target.zip","wb") as zip:
        for chunk in file.iter_content(chunk_size=1024):
            if chunk:
                zip.write(chunk)
        print('-' * 50 + '\n[*] Gnuboard5 has been downloaded')
    
    
def unzip(): # ZIP 파일 압축 해제
    with ZipFile('target.zip', 'r') as zip:
        #zip.printdir()
        zip.extractall()
        print('-' * 50 + '\n[*] Gnuboard5 has uzipped')
        
        
def delete(): # 압축 해제 후 ZIP파일 삭제
    os.remove('target.zip')
    print('-' * 50 + '\n[*] target.zip has deleted')
    
    
def main():
    download('http://github.com/gnuboard/gnuboard5/archive/refs/heads/master.zip')
    unzip()
    delete()


if __name__ == '__main__': # 부르지도 않았는데 튀어오는 코드를 방ㅋ지ㅋ 하자
    main()
