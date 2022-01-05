import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from engine.scan import *

# 로고를 출ㅋ력ㅋ
def printLogo():
    print("_________________________________________________________________")
    print("    ____                ____   ____               _              ")
    print("   / ___| _ __   _   _ | ___| | __ )  _   _  ___ | |_  ___  _ __ ")
    print("  | |  _ | '_ \ | | | ||___ \ |  _ \ | | | |/ __|| __|/ _ \| '__|")
    print("  | |_| || | | || |_| | ___) || |_) || |_| |\__ \| |_|  __/| |   ")
    print("   \____||_| |_| \__,_||____/ |____/  \__,_||___/ \__|\___||_|   ")
    print("                                                                 ")
    print(" Gnuboard5 scanner based on Wordpresscan - @v1nc3ntryu           ")
    print("_________________________________________________________________")
    print("\n")
        
# 명령 인자 정리
def initParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', action ='store', type=str, help='Target URL')
    parser.add_argument('--scan', '-s', action ='store', type=int, default='3', help='Which scan do you want? (1. Picky scan, 2. Scan everything, 3. Skip scans)')
    parser.add_argument('--xss', '-x', action ='store', type=str, default='n', help='Do you want to check xss points? (y/n)')
    parser.add_argument('--inject', '-i', action ='store', type=str, default='n', help='Do you want to check SQLi points? (y/n)')
    parser.add_argument('--bypass', '-b', action ='store', type=str, default='n', help='Do you want to check Bypass points? (y/n)')
    return parser.parse_args()

# 시작!!
def main():
    printLogo()
    results = initParser()

    # url 입력 없으면 HELP 출력
    if(results.url != ''): 
    
        # 디렉터리 스캔 1: 싹다 스캔, 2: 일부만 스캔, 3: 스캔 안함
        if(results.scan != 3):
            scan(results.url, results.scan)
        
        # XSS 가능성 검사 Y: 사용, N: 안사용
        if(results.xss == 'y'):
            print('[-] Still on the work...')
        
        # 인젝션 가능성 검사 Y: 사용, N: 안사용
        if(results.inject == 'y'):
            print('[-] Still on the work...')

        # 인증우회 가능성 검사 Y: 사용, N: 안사용
        if(results.bypass == 'y'):
            print('[-] Still on the work...')

    # 아무것도 입력하지 않으면 아무것도 할 수가 없어...
    else:
        parser.print_help()

if __name__ == '__main__':
    main()




