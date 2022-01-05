import os, requests, time, getgnu
from bs4 import BeautifulSoup

class scan:
    # 경로에 그누보드가 있는지 체크해서 없으면 다운로드
    def checkGnuExist(self):
    
        # 경로에 그누보드가 있는지 체크
        if os.path.isdir("gnuboard5-master"):
            print('_' * 50 + '\n[*] Gnuboard5 is exist')
            
        # 없으면 최신버전을 다운받기 위해 getgnu 실행
        else:
            print('_' * 50 + '\n[*] Gnuboard5 isn\'t exist. Let\'s download it')
            getgnu.main()

    # 무슨 경고를 보여주면서 접근이 안되는지 확인하기 위한 메소드, 경고 메시지 String 리턴
    def getPtag(self, html): 
        soup = BeautifulSoup(html, 'html.parser')
        pTag = soup.find('p', 'cbg')
        
        # p 태그에 경고문구가 없는 경우
        if pTag is None:     
            return '[>>>] No specified reponse'
            
        # 경고문구가 있는 경우
        else:
            return '[>>>] ' + pTag.text.strip()  

    # 어떤 파일을 크롤링 할지 정리하는 메소드, 파일 List 만들어서 리턴.
    def setFiles(self, path, path_idx):
        files = []
        for _ in path_idx:
            for a in os.listdir(path + _): 
            
                # 일단은 php 파일만 봅니다
                if '.php' in a:
                    files.append(_ + a)
                    
        return files

    # setFiles의 파일들 하나하나 요청 보내는 메소드
    def requestFiles(self, URL, target): 
        request_idx = 1
        for _ in target:
            print('_' * 50 + '\n[*] (%s/%s) Request to %s'%(request_idx, len(target), _))
            response = requests.get(URL + _)
            
            # 200 응답이 아닌 경우
            if (response.status_code != 200): 
                print('[>>>] Response is bad %s'%response.status_code)
                
            # p 태그 내 안내 문구 출력과 함께 접근 불가한 경우
            elif ('<p class="cbg">' in response.text): 
                print(self.getPtag(response.text))
                
            # 응답 내용이 없는 경우
            elif(response.text == '' or response.text == '0'): 
                print('[>>>] No response')
            
            # 응답 내용이 긴 경우
            elif(len(response.text) > 50): 
                print('[>>>] The length of response is too big -> [%s]'%len(response.text))
                
            # 그 외 위 조건에 맞지 않는 응답
            else : 
                print(response.text)
            
            time.sleep(0.5)
            request_idx += 1
            
    # 이니시를 걸자
    def __init__(self, URL, scan):
    
        # 호옥시나 전달받은 URL이 접근 불가하진 않을까..?
        if(requests.get(URL).status_code != 200):
            print('URL isn\'t well... try again')
    
        # ㅇㅋ 스캔을 시작하지
        else:
        
            # 특정 경로나 파일만 스캔
            if(scan == 1):
                print('[-] Still on the work...')
                
            # 그냥 디렉터리 내 모든 파일 스캔
            elif(scan == 2):
            
                # 그누보드가 없으면 다운 받아야지..
                self.checkGnuExist() 
                
                # 다운받은 Gnuboard5가 있는 경로
                dir = './gnuboard5-master/' 
                
                # 스캔할 폴더, 추후 다운받은 그누보드에서 디렉토리 다 뽑아서 넣을 예정
                self.scan_dirs = ['', 'bbs/', 'adm/'] 
                
                # requestFiles(크롤링 URL, 크롤링 대상 파일 List),   setFiles(요청 보낼 파일 경로, 중에 어떤 폴더 요청할지)
                self.requestFiles(URL, self.setFiles(dir, self.scan_dirs)) 
            
            
            
            