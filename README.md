<h1>new_test</h1>

<h2>Инструкция по запуску</h2>

<h3>1. Клонируем репозиторий </h3>
&nbsp &nbsp &nbsp Команда git clone https://github.com/Gektor918/new_test

<h3>2. Создаем виртуальное окружение</h3>
&nbsp &nbsp &nbsp Команда-python3 -m venv name_venv

<h3>3. Запускаем виртуальное окружение</h3>
&nbsp &nbsp &nbsp Команда-source name_venv/bin/activate

<h3>4. Устанавливаем зависимости</h3>
&nbsp &nbsp &nbsp Команда - pip install -r requirements.txt

<hr>
<h3>5. Дополнительно </h3>
Все урлы с локального хоста:


Присутствует  swagger:  http://127.0.0.1:8000/swagger/<br>
<h5>Авторизация пользователя только по емайлу и паролю реализована через drf-auth</h5>


http://127.0.0.1:8000/add/new_office/ - Добавление новой организации<br>
Пример запроса: POST <br>
{<br>
"name": "ООО Магнит",<br>
"description": "Розничная продажа"<br>
}<br>
Пример ответа:<br>
{<br>
    "response": {<br>
        "id": 6,<br>
        "name": "ООО Магнит",<br>
        "description": "Розничная продажа"<br>
    }<br>
}<br>
<br>
<hr>
http://127.0.0.1:8000/all/users/ - Вывод списка всех пользователей и связанные с ними организаций<br>
Пример запроса: GET Нет параметров<br>
Пример ответа:<br>
{<br>
    "user_and_office": [<br>
        "d1991v8p@mail.ru",<br>
        [<br>
            "ООО РИММ",<br>
            "ИП СТРОЙМОНТАЖ"<br>
        ],<br>
        "qweqw@mail.ru",<br>
        [<br>
            "ИП СТРОЙМОНТАЖ"<br>
        ],<br>
        "fwer@mail.ru",<br>
        [],<br>
        "wer@mail.ru",<br>
        [],<br>
        "user@example.com",<br>
        []<br>
    ],<br>
    "user_all_info": [<br>
        {<br>
            "id": 1,<br>
            "password": "pbkdf2_sha256$600000$SapFXIxae6C6uBS8KgxT9K$CvpFWg1DziAB/Awtypj2oLbmd7oi9AY0LmZZavkrHqw=",<br>
            "last_login": "2023-04-29T12:15:26.847324Z",<br>
            "is_superuser": true,<br>
            "email": "d1991v8p@mail.ru",<br>
            "first_name": "ret",<br>
            "last_name": "222",<br>
            "phone": "",<br>
            "date_joined": "2023-04-28T04:11:12.733058Z",<br>
            "is_active": true,<br>
            "image": "/image/2_mQ0XS1p.png",<br>
            "is_staff": true,<br>
            "groups": [],<br>
            "user_permissions": [],<br>
            "office": [<br>
                1,<br>
                2,<br>
                1<br>
            ]<br>
        },<br>
<hr>
http://127.0.0.1:8000/office_all/ - Вывод списка всех организаций<br>
Пример запроса: GET Нет параметров<br>
Пример ответа:<br>
"all_office": [<br>
        {<br>
            "id": 1,<br>
            "name": "ООО РИММ",<br>
            "description": "Розничная продажа, оптовая продажа"<br>
        },<br>
        {<br>
            "id": 2,<br>
            "name": "ИП СТРОЙМОНТАЖ",<br>
            "description": "Строительство и монтаж окон и дверей"<br>
        },<br>
 <hr>
 http://127.0.0.1:8000/registration/ - Регистрация, полностью описана в Swagger<br>
  <hr>
http://127.0.0.1:8000/update/ - Редактирование своего профиля (изменение данных в профиле)<br>
Пример запроса: PUT Тестировал через Postman отправку image<br>
{<br>
"email": "d1991v8p@mail.ru",<br>
"first_name": "Дима",<br>
"last_name": "Пьянков"<br>
}<br>
Пример ответа:<br>
{<br>
    "response": {<br>
        "first_name": "Дима",<br>
        "last_name": "Пьянков",<br>
        "phone": "",<br>
        "image": "/image/2_mQ0XS1p.png"<br>
    }<br>
}<br>
<hr>
http://127.0.0.1:8000/user/one/ - Вывод одного пользователя по его ID, со списком связанных с ним организаций<br>
Пример запроса: POST<br>
{<br>
"id":1<br>
}<br>
Пример ответа:<br>
{<br>
    "serializer_class": {<br>
        "id": 1,<br>
        "password": "pbkdf2_sha256$600000$SapFXIxae6C6uBS8KgxT9K$CvpFWg1DziAB/Awtypj2oLbmd7oi9AY0LmZZavkrHqw=",<br>
        "last_login": "2023-04-29T12:15:26.847324Z",<br>
        "is_superuser": true,<br>
        "email": "d1991v8p@mail.ru",<br>
        "first_name": "Дима",<br>
        "last_name": "Пьянков",<br>
        "phone": "",<br>
        "date_joined": "2023-04-28T04:11:12.733058Z",<br>
        "is_active": true,<br>
        "image": "/image/2_mQ0XS1p.png",<br>
        "is_staff": true,<br>
        "groups": [],<br>
        "user_permissions": [],<br>
        "office": [<br>
            1,<br>
            2,<br>
            1<br>
        ]<br>
    },<br>
    "list_office": [<br>
        "ООО РИММ",<br>
        "ИП СТРОЙМОНТАЖ"<br>
    ]<br>
}<br>
