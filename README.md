# GNU5BUSTER!!!!!

그누보드5를 아직도 쓰는 사람들이 많더라구요,, 근데 가끔 기본 페이지가 그대로 구성되어 있어서 사용하지 않음에도 접근이 가능한 경우가 있고, 또 그 페이지를 통해 서비스의 취지에 맞지 않는 여러 악성 행위가 가능하기도 합니다. 

저는 그 녀석들을 잡고 싶어요

## Nutrition Facts
```
gnu5buster.py : 그누보드 기본 폴더에 접근하고 response를 print하는 내용 입니다... 뭐 아직 별거 없죠
getgnu.py : 그누보드5 최신버전을 받아서 압축도 풀고 지지고 볶는 내용입니다.... 그냥 그렇다구요..
```

# 개발 계획 & 일정 
누구나 그럴듯한 계획을 가지고 있지... 더보기 <----------------------- 클릭한 흑우들 없제

## 완료된 작업들

**2021-12-01**
```
- 개발 계획
```

**2021-12-08**
```
- 그누보드5 AWS에 설치(게시판, 로그인, 회원가입 정도로 디폴트하게) 후 간단하게 페이지 기능 분석
```

**2021-12-15**
```
- 그누보드5 기본 페이지 및 경로 리스트 작성해서 for문으로 요청 보내기
- github 구성해서 코드 올리기
- 파이선 단에서 gnuboard 최신버전 받도록 코딩
```

## 남은 작업들...

**금방 끝나는 것**
1~2시간이면 완료 가능하고, 길어도 하루면 될 것을 아직도 미루고 있는 작업들
```
- 각 페이지 Response별로 결과 나누어 출력하기
- 인자(검사할 폴더, 확장자 등) 받아서 검사하도록 정리하기
- 결과 워드나 엑셀 파일로 Export 하기
- 각 분석 기능별로 모듈 나누기
- 함수, 메소드별로 주석 달기
- 불필요한 코드 정리하기
- 타 환경에서 정상 동작 여부 확인하기
- 배포하면서 커뮤니티에 피드백(에러가 난다거나, 원하는 기능이 있다거나 등등) 요청 및 자랑
```

**오래 걸리는 것**
하루 이상, 길면 몇 주 걸리는 작업들

```
- 기타 그누보드 관련 취약점 있는지 조사
- WPScan 써보고 및 쓸만한 기능 확인, 벤치마킹(이라 쓰고 표절이라 읽는다)
- XSS, SQLi 등 입력 값 검증 미흡으로 발생하는 취약점 필터링 여부"만" 판단하는 기능 추가(GET, POST 요청, SQLi 가능 여부 어떻게 찾아낼건지)
- 취약점 가능성 여부 어떻게 판별할건지
- 그누보드 기존 패치 로그 확인해서 이미 조치 완료된 취약점 중에 추가할 수 있는 기능 있는지 검토
- Admin 권한 탈취(php Magic hash 활용), SQLi 등 알려진 취약점 진단 기능 추가 가능성 검토
```


