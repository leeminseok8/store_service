# Store Service
온라인 스토어 서비스의 백엔드 API를 개발하여 제공합니다.

---

## 목차
1. [사용법](#사용법)
2. [사용 기술 스택](#사용-기술-스택)
3. [MVP Service](#MVP-Service)
4. [ERD](#ERD)
5. [API 명세서](#API-명세서)
6. [기능 명세서 및 분석](#기능-명세서-및-분석)

<br>

---

## 사용법
- [가상 환경 설치](#가상-환경-설치)부터는 프로젝트 최상위 디렉토리(store_service)에서 명령어를 입력하셔야 합니다.

### 프로젝트 로컬 설치
```
> git clone https://github.com/leeminseok8/store_service.git

> cd --project_name
```

### 가상 환경 설치
> pipenv를 사용하였습니다.
```
프로젝트 최상위 디렉토리(Pipfile)에서 실행)
> pwd
~/.../store_service


pipenv가 없으시다면)
> pip install pipenv

> pipenv shell


pipenv가 있으시다면)
> pipenv shell
```

### DB 생성
```
프로젝트 최상위 디렉토리(manage.py)에서 실행)
> pwd
~/.../store_service

> python manage.py makemigrations

> python manage.py migrate
```

### Batch 파일로 데이터 삽입
```
프로젝트 최상위 디렉토리에서 실행)
> pwd
~/.../store_service

> python uploader.py
```

### 로컬(개발용) 서버 실행
```
> python manage.py runserver
```

---

## 사용 기술 스택
- back-end : <img src="https://img.shields.io/badge/Python-3.10.0-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Django REST framework-092E20?style=flat-square&logo=Django REST framework&logoColor=white"/> 

- DataBase : <img src="https://img.shields.io/badge/MySQL-003B57?style=flat-square&logo=MySQL&logoColor=white"/> 

- formater : <img src="https://img.shields.io/badge/Black-003B57?style=flat-square&logo=Black&logoColor=white"/> 

<br>

---

## MVP Service
### 계정
> 슈퍼유저를 관리자로 생성할 수 있습니다.<br>
관리자 권한 : 상품, 주문, 결제에 대한 CRUD 권한을 가지고 있습니다.<br>
이용자 권한 : 회원가입, 주문, 결제 외 상품에 대해서 R 권한을 가지고 있습니다.
- 이용자 및 관리자 생성
    - 이용자와 관리자의 권한에 따라 기능을 제한하였습니다.
### 상품
> 관리자 권한 : 상품 생성, 조회, 수정, 삭제 <br>
  이용자 권한 : 상품 조회
- 상품 생성
    - 상품의 제목, 내용, 가격, 원산지, 이미지를 등록할 수 있습니다.
- 상품 조회
    - 상품 리스트를 조회할 수 있습니다. <br>
    (제목, 가격)
    - 상품 디테일 조회가 가능합니다. <br>
    (제목, 내용, 가격, 원산지, 이미지)
- 상품 수정
    - 상품의 제목, 내용, 가격, 원산지를 수정할 수 있습니다.
- 상품 삭제
    - 상품을 삭제할 수 있습니다.

### 주문
- 주문 생성
    - 수량, 총 가격, 배달비를 포함한 주문을 생성할 수 있습니다.
- 주문 리스트 조회
    - 로그인 된 유저의 완료된 주문 내역을 조회할 수 있습니다.
- 주문 수정
    - 결제 전 수량을 변경할 수 있습니다.
- 주문 삭제
    - 결제 전 주문을 취소할 수 있습니다.

### 결제
- 결제 완료
    - 결제 방법, 결제 상태를 생성할 수 있습니다.
        - 결제 상태( True:완료 / False:취소)
    - 결제 완료 시 주문번호를 생성합니다.
- 결제 취소
    - 결제 상태를 취소로 변경할 수 있습니다.

<br>

---

## ERD
<img width="875" alt="스크린샷 2022-10-03 오후 11 24 30" src="https://user-images.githubusercontent.com/93478318/193601807-55c7023e-9029-4b5d-8b29-e0ee21679805.png">

<br>

---

## API 명세서
| Domain | endpoint | Method | 기능 | 권한 |
| --- | --- | --- | --- | --- |
| **Users** | accounts/signin/ | POST | 로그인 | - |
|  | accounts/signup/ | POST | 회원가입 | - |
| - |  |  |  |  |
| **Products** | products/ | POST | 상품생성 | 관리자 |
|  | products/ | GET | 상품 리스트 조회 | - |
|  | products/id/ | GET | 상품 상세 조회 | - |
|  | products/id/ | PATCH/PUT | 상품 수정 | 관리자 |
|  | products/id/ | DELETE | 상품 삭제 | 관리자 |
| - |  |  |  |  |
| **Orders** | orders/ | POST | 주문 생성 | 사용자/관리자 |
|  | orders/ | GET | 주문 리스트 조회 | 사용자/관리자 |
|  | orders/id/ | PATCH/PUT | 주문 수정 | 사용자/관리자 |
|  | orders/id/ | DELETE | 주문 삭제 | 사용자/관리자 |
|  | orders/id/ | GET | 주문 상세 조회 | 사용자/관리자 |
| - |  |  |  |  |
| **Payments** | payments/ | POST | 주문 생성 | 사용자/관리자 |
|  | payments/id/ | PATCH/PUT | 주문 삭제 | 사용자/관리자 |


<br>

---

## 기능 명세서 및 분석

### 회원가입
<img width="953" alt="스크린샷 2022-10-04 오후 3 03 34" src="https://user-images.githubusercontent.com/93478318/193746003-a0873f61-9036-40b6-a98a-343f6f3f1b12.png">

- 커머스 서버스를 구현하였으므로 배송 시 문자와 배송 장소를 위해 핸드폰 번호와 주소는 필수 입력하도록 하였습니다.

- 비밀번호는 DB에 암호화되어 저장됩니다.

<img width="957" alt="스크린샷 2022-10-04 오후 3 05 56" src="https://user-images.githubusercontent.com/93478318/193746327-73db9caf-6ddd-4961-9546-da1ad95a525a.png">

- 회원가입 성공 시 Response 입니다.

<br>

### 로그인
<img width="961" alt="스크린샷 2022-10-04 오후 3 08 13" src="https://user-images.githubusercontent.com/93478318/193746652-a25923d1-20e5-489b-bae6-3aee0e487eb1.png">

- 아이디, 비밀번호를 입력하여 로그인할 수 있습니다.
- 클라이언트에 엑세스 토큰과 리프레시 토큰을 발급합니다.

<br>

### 상품 등록
> 상품 관련 CRUD 권한은 관리자만 가지고 있고, 이용자는 R 권한만 있습니다.

<img width="954" alt="스크린샷 2022-10-04 오후 3 11 10" src="https://user-images.githubusercontent.com/93478318/193747062-c4f39d06-516a-4bbb-b00c-7e3bd4226494.png">

- is_seller 상태가 True(관리자)인 경우 상품을 등록할 수 있습니다.

<br>

### 상품 리스트 조회
<img width="960" alt="스크린샷 2022-10-04 오후 3 14 47" src="https://user-images.githubusercontent.com/93478318/193747617-d9bf373a-7257-4d77-9902-f795ba368b05.png">

- 현재 등록된 상품 전체를 조회할 수 있습니다.<br>
-> 제목, 가격

<br>

### 상품 디테일 조회
<img width="960" alt="스크린샷 2022-10-04 오후 3 16 03" src="https://user-images.githubusercontent.com/93478318/193747785-3d8062b2-f9e0-48c0-b687-c20273cc96a5.png">

- 선택한 상품의 디테일을 조회할 수 있습니다.

<br>

### 상품 수정
<img width="959" alt="스크린샷 2022-10-04 오후 3 18 09" src="https://user-images.githubusercontent.com/93478318/193748101-5572f715-d14f-45be-ba5f-509e0bd9b7b6.png">

- is_seller 상태가 True(관리자)인 경우 상품을 수정할 수 있습니다.

<br>

### 상품 삭제
> 별도의 Response를 제공하지 않습니다.
- is_seller 상태가 True(관리자)인 경우 상품을 삭제할 수 있습니다.

<br>

### 주문 등록
<img width="956" alt="스크린샷 2022-10-04 오후 3 22 50" src="https://user-images.githubusercontent.com/93478318/193748803-3eb12c65-df59-416d-b65b-1aa54165fd6c.png">

<img width="958" alt="스크린샷 2022-10-04 오후 3 21 35" src="https://user-images.githubusercontent.com/93478318/193748613-39bfc0af-a96b-4883-8aad-96fc294bd0e6.png">

- 수량을 체크하면 누구나 주문을 등록할 수 있습니다.
- 구매 총 금액이 30,000원 이상일 경우 **배송비 무료**입니다.

<br>

### 주문 리스트 조회
<img width="957" alt="스크린샷 2022-10-04 오후 5 04 55" src="https://user-images.githubusercontent.com/93478318/193767190-30bc0122-b93d-42b5-a6ea-ce784c76638b.png">

- 주문 내역 리스트를 볼 수 있습니다.
- 결제 완료, 취소 상태와 주문번호를 추가적으로 확인할 수 있습니다.

### 주문 디테일 조회
<img width="960" alt="스크린샷 2022-10-04 오후 5 28 48" src="https://user-images.githubusercontent.com/93478318/193772045-3699a086-904b-42e0-95a3-16fc23384cbc.png">

- 주문 내역의 상세 정보를 볼 수 있습니다.
- 현재는 order 테이블을 호출하지만 주문 내역 리스트에서 디테일을 호출할 시 product의 디테일을 불러오도록 기획하였습니다.(프론트와 협업 시 클라이언트에서 구현)

### 주문 수정
> 주문 수정은 따로 구현하지 않았습니다.
- 현재 구현된 기능은 장바구니를 제외한 커머스 서비스로 주문 수정 기능은 필요하지 않다고 판단하였습니다. 클라이언트에서 수량(quantity)를 patch로 구현하여 post를 요청한다면 서버에서 주문 생성하는 로직으로 구현하였습니다.

### 주문 삭제
> 별도의 Response를 제공하지 않습니다.
- 주문 생성 후 결제 화면으로 이동하는데 결제 화면에서 결제 취소를 입력하면 생성된 주문이 삭제되는 로직으로 구현하였습니다.

### 결제 생성
<img width="960" alt="스크린샷 2022-10-04 오후 5 42 46" src="https://user-images.githubusercontent.com/93478318/193775078-b2af0ec2-d555-4c54-9dbc-a2700c0359b8.png">

- 주문 생성 후 결제 화면에서 결제 방법 선택 후 결제를 완료할 수 있습니다.
- 결제 완료 시 결제 완료와 함께 주문번호가 함께 생성됩니다.
- 결제 화면에서 결제 취소 버튼을 누를 시 [주문 삭제](#주문-삭제) API가 호출됩니다.

### 결제 취소
<img width="964" alt="스크린샷 2022-10-04 오후 6 09 09" src="https://user-images.githubusercontent.com/93478318/193781029-0e0a924c-e4c0-4348-9806-66059edf21bc.png">

- 결제 등록 시 payment_state가 True로 생성됩니다.

<img width="962" alt="스크린샷 2022-10-04 오후 6 10 55" src="https://user-images.githubusercontent.com/93478318/193781393-36cf0c8c-b59f-48d1-9a7b-21f68cbc91a0.png">

- 결제 취소 요청 시 payment_state가 False로 수정됩니다.
