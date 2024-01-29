Описание

Данный проект представляет инструмент для сбора данных о работодателях и их вакансиях с сайта hh.ru. 
Основная задача проекта - получить информацию о 10 крупнейших ИТ-компаниях в России. 
Полученные данные о вакансиях и работодателях затем добавляются в таблицы базы данных 
PostgreSQL с использованием библиотеки psycopg2 для взаимодействия с базой данных.

Установка и настройка

Перед использованием приложения требуется создать файл "database.ini" в каталоге "data" для настройки 
доступа к локальной базе данных PostgreSQL и внести необходимые для создания базы данных данные. В текущей версии уже
присутствует файл "database.ini" с перечнем необходимых параметров, которые можно использовать за исключением пароля, 
который необходимо придумать для подключения к PostgreSQL.

Использование

Для работы с базой данных предусмотрен класс DBManager, который содержит следующие методы:

- Получение списка всех компаний и количества вакансий для каждой компании.
- Получение списка всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию.
- Получение средней зарплаты по вакансиям.
- Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
- Получение списка всех вакансий, заголовки которых содержат переданные ключевые слова.

Зависимости

Python 3.x

PostgreSQL

Библиотека psycopg2 для работы с PostgreSQL

database.ini

