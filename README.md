# Store Service
온라인 스토어 서비스의 백엔드 API를 개발하여 제공합니다.

---
## 목차
1. [사용 기술 스택](#사용-기술-스택)
2. [MVP Service](#MVP-Service)
3. [ERD](#ERD)
4. [API 명세서](#API-명세서)

<br>

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
- 주문 조회
    - 주문 내역을 조회할 수 있습니다.
- 주문 수정
    - 결제 전 수량을 변경할 수 있습니다.
- 주문 삭제
    - 결제 전 주문을 취소할 수 있습니다.

<br>

---

## ERD
<img width="864" alt="스크린샷 2022-09-16 오후 12 51 58" src="https://user-images.githubusercontent.com/93478318/190552992-b5c583b3-ea9f-4f9c-8182-519b333d4160.png">

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
<!-- | - |  |  |  |  |
| **Payments** | payments/ | POST | 주문 생성 | 사용자/관리자 |
|  | payments/ | GET | 주문 리스트 조회 | 사용자/관리자 |
|  | payments/id/ | PATCH/PUT | 주문 수정 | 사용자/관리자 |
|  | payments/id/ | DELETE | 주문 삭제 | 사용자/관리자 |
|  | payments/id/ | GET | 주문 상세 조회 | 사용자/관리자 | -->