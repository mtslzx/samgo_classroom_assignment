# 반배정을 내놔라

버전 : 0.2 Alpha

고등학교의 반배정 확인 시스템에 생일을 무차별 대입해 찾아내주는 프로그램입니다.

## 어떻게 사용하나요?
우선 크롬 드라이버를 자신이 사용하는 크롬에 맞는 버전으로 교체해주세요.

`driver.get('X')` X에 학교 반배정을 찾는 웹 페이지의 링크를 입력해주세요.

그런 다음 자신의 학교 반배정을 알려주는 사이트로 이동하여 알맞는 XPath를 지정하여 주세요.

**이름.txt**에 간격이나 줄바꿈 **없이** 3글자씩 입력하여 주세요.

`for i in range(X):` X에 이름의 갯수를 입력하여 주세요.

그리고 실행하면 **반배정.txt**에 결과값이 차례차례 입력될거에요.

## 체인지 로그
- v0.2 2021 삼천포고등학교에 맞는 양식 변경 및 크롬 88버전 대응 크롬 드라이버 업데이트

- v0.1 첫 릴리즈

---

제작자 : mtslzx (mtslzx@gmail.com)
