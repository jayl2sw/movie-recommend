# Final Project

## 주요 기능

### 메인 페이지

![image-20220520194620245](C:\Users\Jay Lee\AppData\Roaming\Typora\typora-user-images\image-20220520194620245.png)

* on_main 필드를 사용하여 관리자가 메인으로 지정해 놓은 컬렉션들을 무작위 순서로 정렬하여 보여줌

  

### 컬렉션 페이지

![image-20220520164454389](C:\Users\Jay Lee\AppData\Roaming\Typora\typora-user-images\image-20220520164454389.png)

* 2주내에 생성된 컬렉션 중에 좋아요가 많은 순으로 보여줍니다.



### 프로필 페이지

![image-20220520172235392](C:\Users\Jay Lee\AppData\Roaming\Typora\typora-user-images\image-20220520172235392.png)

* 유저가 만든 컬렉션을 좋아요 많은 순으로 제공합니다.



### 프로필사진 추가

![image-20220520201533289](Final Project.assets/image-20220520201533289.png)

* dj_rest_auth에서 사용하는 ResgisterSerializer를 커스텀하여 profile_image를 작성할 수 있도록 함

![image-20220520201653749](Final Project.assets/image-20220520201653749.png)

* 어댑터를 사용하여 해당 정보가 데이터베이스에 저장 될 수 있도록 설정함

  