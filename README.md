 1. Наименование проекта

**Информационная система "Цветы"**

 2. Краткое описание

Разработана информационная система для управления и анализа данных о цветах, их характеристиках, сезоне цветения, поставщиках и продавцах. Система позволяет выполнять поиск и выдачу сведений по различным запросам, а также добавлять и удалять информацию о цветах для заданных поставщиков.

 3. Анализ предметной области

Проект "Цветы" предназначен для работы с базой данных, содержащей информацию о различных типах цветов (садовый или комнатный), их характеристиках, сезоне цветения, стране происхождения, поставщиках и продавцах. Система предоставляет возможность поиска и выдачи сведений, проведения различных запросов, добавления и удаления информации.

Основные функции системы:
- Ведение обобщенных списков информации:
  - Сведения о цветах.
  - Сведения о поставщиках.
  - Сведения о продавцах.
  
- Реализация различных запросов:
  - Списки цветов для каждого из поставщиков.
  - Список цветов с заданным сезоном цветения.
  - Список цветов, выведенных в заданной стране.
  - У кого можно купить заданный сорт.
  - Продавцы самых дорогих цветов.
  - Совпадающие поставщики у продавцов.
  
- Возможность добавления и удаления цветов для заданного поставщика.

Файл views.py определяет конечные точки API, с которыми могут взаимодействовать клиенты. Каждая конечная точка соответствует URL-адресу и методу HTTP (GET, POST, PUT, DELETE), который определяет операцию, которая будет выполняться при обращении к конечной точке.
  - Create: Конечные точки для создания новых записей в базе данных.
  - Read: Конечные точки для извлечения данных из базы данных.
  - Update: Конечные точки для обновления существующих записей.
  - Delete: Конечные точки для удаления записей.

![image](https://github.com/Lek14/flower-32-/assets/125027733/83bddcb3-09f0-4722-a90c-8fcbae6c783b)


ERD


![image](https://github.com/Lek14/flower-32-/assets/125027733/3776f1c6-2dda-49c7-bc21-1c27163e9fc4)


DFD диаграмма


![image](https://github.com/Lek14/flower-32-/assets/125027733/c8020907-35e2-4fa7-814b-9e5e4a9b64de)


useCase


![image](https://github.com/Lek14/flower-32-/assets/125027733/8574c06c-265c-4ede-9f43-3e78ae00267c)


![image](https://github.com/Lek14/flower-32-/assets/125027733/5d841bed-eca4-4a84-9a61-5eb67b436e33)

(Начальная страница , пользовательможет взаимодействовать с навигационной панелью в зависимости от его задач)

![image](https://github.com/Lek14/flower-32-/assets/125027733/2e8ba0db-1c4a-4529-9d12-9b664bc06b62)


(На этой вкладке можно посмотреть цветы для каждого из поставщиков)

![image](https://github.com/Lek14/flower-32-/assets/125027733/ad4075ba-5344-4636-8cfd-845aa5dbf8ca)


(Create Flower страница создания и привязки цветка к определенному поставщику)

                                     
![image](https://github.com/Lek14/flower-32-/assets/125027733/b50d1797-b972-4378-b15e-5b47786109d2)


(Delete Flower сраница удаления цветка у заданного поставщика)


![image](https://github.com/Lek14/flower-32-/assets/125027733/cf879ebc-cbd7-4b27-8679-87f0276fd2e4)
(Get Vendors(будет переименована как и другие старницы) реализовывает поиск цветка по сорту и и цене если это нужно)
