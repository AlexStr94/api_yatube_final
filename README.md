### Описание проекта api_final

Api к учебному проекту сервису блогов Yatube. Сервис реализован на Django, а для API использован Django REST Framework. API позволяет всем пользователям получать Token авторизации; администратору создавать, редактировать и удалять группы постов, посты, комментарии; всем остальным пользователям создавать посты и комментарии, редактировать их. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_yatube_final.git
```

```
cd api_yatube_final
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

Создание публикации:

```
{
    "text": "Текст публикации",
    "group": 1
} 
