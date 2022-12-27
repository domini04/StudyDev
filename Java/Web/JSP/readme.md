# JSP

[JSP Tags](https://www.notion.so/JSP-Tags-dab998fff4be4f37bbe8e72f824a3ab9)

### Java Server Page

![Untitled](JSP%20a347b84c38f54f0f955573ce99f56527/Untitled.png)

- **용도**
    - 자바 데이터를 브라우저 화면에 출력할 수 있게 제시된 스펙
    - ***MVC패턴에서 View에 해당!***
- **특징**
    - 확장자 : ***.jsp**
    - 위치 : html과 동일한 경로
        - WebContent 내부
    - jsp를 최초로 호출할 경우 web server가 **servlet으로 자동 변환**
        - 개발은 쉬우나 에러 발생시 변환된 servlet의 에러 메세지가 보이기 때문에 에러 처리가 어렵다
    - 정해진 tag들로 개발
    - 이미 자동 생성되는 **내장 객체**들 존재
        - 요청 객체, 세션 객체, 출력 객체, 응답 객체...
        - 개발자 코드는 참조 변수로만 사용하는 코드로 개발
- **JSP 내장 객체**
    - **out**
        - Printwriter에 대응
    - **request**
        - HttpServletRequest에 대응
    - **session**
        - HttpSession [쿠키 내장객체 아님]에 대응
    - **pageContext**
        - this에 대응
        - 해당 JSP페이지를 구성
- **JSP 태그**
    - 표준화 된 JSP 태그들을 사용하여 출력 처리
    - **가능하면 java 코드는 사용 최소화**