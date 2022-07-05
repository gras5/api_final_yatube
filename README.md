### Содержание:
 + [Использованные технологии](#Tech)
 + [Как запустить проект](#EasyStart)
 + [Где документация?](#Docs)
 + [Таблица запросов](#RequestsList)
 + [Об авторе](#About)

<br>
<a id="Tech"></a>

### Использованные технологии:

* Python 
* Django 2.2.16
* Django Rest Framework 3.12.4
* Djoser 2.1.0
* Simple JWT 4.7.2
* Pytest 6.2.4

<br>
<a id="EasyStart"></a>

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/gras5/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Создать суперпользователя:

```
python3 manage.py createsuperuser
```


Запустить проект:

```
python3 manage.py runserver
```
<br>
<a name="Docs"></a>

### Где документация?
К сожалению документация пока доступна только при локальном запуске проекта. После выполнения шагов из **[Как запустить проект](#EasyStart)** документация должна быть доступна по адресу:
http://localhost:your_port/redoc/

<br>
<a name="RequestsList"></a>

### Таблица запросов
**Уровни доступа:**
1. анонимные пользователи
2. авторизованный пользователь
3. авторизованный пользователь (только автор)

|Описание|Уровни доступа|Тип запроса|Ссылка|
|:--|:-:|:-:|:--|
|Получить список публикаций|1|GET|/api/v1/posts/ |
|Создать новую публикацию|2|POST|/api/v1/posts/ |
|Получить публикацию по id|1|GET|/api/v1/posts/{post_id}/ |
|Изменить\удалить публикацию по id|3|PUT, PATCH, DELETE|/api/v1/posts/{post_id}/ |
|Получить список комментариев по id публикации|1|GET|/api/v1/posts/{post_id}/comments/ |
|Добавить новый комментарий по id публикации|2|POST|/api/v1/posts/{post_id}/comments/ |
|Получить комментарий по его id (+ id публикации)|1|GET|/api/v1/posts/{post_id}/comments/{comment_id}/ |
|Изменить\удалить комментарий по его id (+ id публикации)|3|PUT, PATCH, DELETE|/api/v1/posts/{post_id}/comments/{comment_id}/|
|Получить список групп|1|GET|/api/v1/groups/ |
|Получить группу по его id|1|GET|/api/v1/groups/{group_id}/|
|Получить подписки текущего пользователя.|2|GET|/api/v1/follow/|
|Подписаться на пользователя по его username. Тело запроса должно содержать:```{"following":"username"}```|2|POST|/api/v1/follow/|
|Получить JWT токен. Тело запроса должно содержать:```{"username": "username", "password":"password"}```|1|POST|/api/v1/jwt/create/|
|Обновить JWT токен. Тело запроса должно содержать:```{"refresh": "refresh_token"}```|2|POST|/api/v1/jwt/refresh/|

Больше дополнительных возможностей доступны в [документации.](#Docs)

<br>
<a name="About"></a>

### Об авторе
Github: https://github.com/gras5
