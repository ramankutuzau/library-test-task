![img_1.png](img_1.png)
Сервис "Библиотека" - Описание и Руководство
Описание
Проект "Библиотека" представляет собой систему автоматизации учета выдачи книг читателям. Сервис позволяет удобно вести учет книг, читателей, а также контролировать процесс выдачи и возврата книг.

Функционал
Создание книг: Книги могут быть созданы с указанием названия и автора. У каждого автора может быть несколько книг.

Учет читателей: Читатели регистрируются в системе с указанием Фамилии, Имени и Отчества. Один читатель может быть зарегистрирован только один раз. Читатели могут одновременно иметь несколько книг.

Учет выдачи книг: Система фиксирует дату выдачи и возврата книги читателю.

Учет хранения книг: Пользователь может проверить остатки книг в библиотеке и узнать, какие книги находятся у читателей.

Используемые Технологии
Backend: Python (Django)
Frontend: JavaScript, Bootstrap 5 (модальные окна)
База данных: SQLite (по умолчанию в Django)
Администрирование: Логин - admin, Пароль - test

Запуск Приложения
Установка Django: Если у вас еще нет Django, вы можете установить его с помощью команды:


pip install django
Скачивание Проекта: Скачайте проект из репозитория:


git clone https://github.com/ramankutuzau/library.git
Создание и Применение Миграций: Перейдите в папку с проектом и выполните команды:


cd library
python manage.py makemigrations
python manage.py migrate
Запуск Сервера: Запустите встроенный сервер разработки Django:
python manage.py runserver




Доступ к Админке: Перейдите в браузере по адресу http://86.57.178.104:11111/admin/. Войдите, используя логин admin и пароль test.

Запуск Приложения: Перейдите в браузере по адресу http://86.57.178.104:11111 для доступа к вашему приложению "Библиотека".

