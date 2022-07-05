### ����������:
 + [�������������� ����������](#Tech)
 + [��� ��������� ������](#EasyStart)
 + [��� ������������?](#Docs)
 + [������� ��������](#RequestsList)
 + [�� ������](#About)

<br>
<a id="Tech"></a>

### �������������� ����������:

* Python 
* Django 2.2.16
* Django Rest Framework 3.12.4
* Djoser 2.1.0
* Simple JWT 4.7.2
* Pytest 6.2.4

<br>
<a id="EasyStart"></a>

### ��� ��������� ������:

����������� ����������� � ������� � ���� � ��������� ������:

```
git clone https://github.com/gras5/api_final_yatube.git
```

```
cd api_final_yatube
```

C������ � ������������ ����������� ���������:

```
python3 -m venv env
```

```
source env/bin/activate
```

���������� ����������� �� ����� requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

��������� ��������:

```
python3 manage.py migrate
```

������� �����������������:

```
python3 manage.py createsuperuser
```


��������� ������:

```
python3 manage.py runserver
```
<br>
<a name="Docs"></a>

### ��� ������������?
� ��������� ������������ ���� �������� ������ ��� ��������� ������� �������. ����� ���������� ����� �� **[��� ��������� ������](#EasyStart)** ������������ ������ ���� �������� �� ������:
http://localhost:your_port/redoc/

<br>
<a name="RequestsList"></a>

### ������� ��������
**������ �������:**
1. ��������� ������������
2. �������������� ������������
3. �������������� ������������ (������ �����)

|��������|������ �������|��� �������|������|
|:--|:-:|:-:|:--|
|�������� ������ ����������|1|GET|/api/v1/posts/ |
|������� ����� ����������|2|POST|/api/v1/posts/ |
|�������� ���������� �� id|1|GET|/api/v1/posts/{post_id}/ |
|��������\������� ���������� �� id|3|PUT, PATCH, DELETE|/api/v1/posts/{post_id}/ |
|�������� ������ ������������ �� id ����������|1|GET|/api/v1/posts/{post_id}/comments/ |
|�������� ����� ����������� �� id ����������|2|POST|/api/v1/posts/{post_id}/comments/ |
|�������� ����������� �� ��� id (+ id ����������)|1|GET|/api/v1/posts/{post_id}/comments/{comment_id}/ |
|��������\������� ����������� �� ��� id (+ id ����������)|3|PUT, PATCH, DELETE|/api/v1/posts/{post_id}/comments/{comment_id}/|
|�������� ������ �����|1|GET|/api/v1/groups/ |
|�������� ������ �� ��� id|1|GET|/api/v1/groups/{group_id}/|
|�������� �������� �������� ������������.|2|GET|/api/v1/follow/|
|����������� �� ������������ �� ��� username. ���� ������� ������ ���������:```{"following":"username"}```|2|POST|/api/v1/follow/|
|�������� JWT �����. ���� ������� ������ ���������:```{"username": "username", "password":"password"}```|1|POST|/api/v1/jwt/create/|
|�������� JWT �����. ���� ������� ������ ���������:```{"refresh": "refresh_token"}```|2|POST|/api/v1/jwt/refresh/|

������ �������������� ������������ �������� � [������������.](#Docs)

<br>
<a name="About"></a>

### �� ������
Github: https://github.com/gras5
