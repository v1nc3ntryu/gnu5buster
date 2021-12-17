import os, requests, time, getgnu
from bs4 import BeautifulSoup

def checkGnuExist():
    if os.path.isdir("gnuboard5-master"):
        print('_' * 50 + '\n[*] Gnuboard5 is exist')
    else:
        print('_' * 50 + '\n[*] Gnuboard5 isn\'t exist. initiate download')
        getgnu.main() # getgnu.py 실행


def getPtag(html): # 무슨 경고를 보여주면서 접근이 안되는지 확인하기 위한 메소드, 경고 메시지 String 리턴
    soup = BeautifulSoup(html, 'html.parser')
    pTag = soup.find('p', 'cbg')   
    
    if pTag is None:     
        return '[>>>] No specified reponse'
    else:
        return '[>>>] ' + pTag.text.strip()  


def setFiles(path, path_idx): # 어떤 파일을 크롤링 할지 정리하는 메소드, 파일 List 리턴
    files = []
    for _ in path_idx:
        for a in os.listdir(path + _): 
            if '.php' in a:
                files.append(_ + a)
                
    return files


def requestFiles(URL, target): # setFiles의 파일들 하나하나 요청 보내는 메소드
    request_idx = 1
    for _ in target:
        print('_' * 50 + '\n[*] (%s/%s) Request to %s'%(request_idx, len(target), _))
        response = requests.get(URL + _)
        
        if (response.status_code != 200): # 200 응답이 아닌 경우
            print('[>>>] Response is bad %s'%response.status_code)
        elif ('<p class="cbg">' in response.text): # p 태그 내 안내 문구 출력과 함께 접근 불가한 경우
            print(getPtag(response.text))
        elif(response.text == '' or response.text == '0'): # 응답 내용이 없는 경우
            print('[>>>] No response')
        elif(len(response.text) > 50): # 응답 내용이 긴 경우
            print('[>>>] The length of response is too big -> [%s]'%len(response.text))
        else : # 그 외
            print(response.text)
        
        time.sleep(0.5)
        request_idx += 1
        
        
def main():
    checkGnuExist() # 그누보드가 없으면 다운 받아야지..
    dir = './gnuboard5-master/' # Gnuboard5 경로
    scan_dirs = ['', 'bbs/'] # 스캔할 폴더
    scan_URL = 'http://127.0.0.1/gnuboard5/'
    requestFiles(scan_URL, setFiles(dir, scan_dirs)) # requestFiles(크롤링 URL, 크롤링 대상 파일 List),   setFiles(요청 보낼 파일 경로, 중에 어떤 폴더 요청할지)
    
    
if __name__ == '__main__':
    main()



