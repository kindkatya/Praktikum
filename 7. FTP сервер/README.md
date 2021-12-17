# Основные задания:

Посмотреть содержимое папки; 
клиент
![image](https://user-images.githubusercontent.com/90270843/146607988-5157e492-5d94-4dc6-a4bf-e22e09d023da.png)
сервер
![image](https://user-images.githubusercontent.com/90270843/146608057-6b9a50ec-c20f-407c-8968-885ddc6d4677.png)


Создать папку;

![image](https://user-images.githubusercontent.com/90270843/146608131-73a976c7-23cb-47dd-8eaa-c480e7c9dc6e.png)
![image](https://user-images.githubusercontent.com/90270843/146608190-b3a5f22f-5975-489e-acda-c62c9199de6f.png)



Домашняя папка пользователя
![image](https://user-images.githubusercontent.com/90270843/146608354-628e70d3-df63-4443-af60-70eb6f09a221.png)

В ней созданная нами
![image](https://user-images.githubusercontent.com/90270843/146608247-db0c5c7a-b2f7-45ba-9610-a2fb5a80c0e8.png)


Удалить папку;

![image](https://user-images.githubusercontent.com/90270843/146608563-72652f9c-2b3b-4e70-8ffa-43380355d586.png)
![image](https://user-images.githubusercontent.com/90270843/146608594-2aceeaa9-0a97-4330-b92a-db9d83a686cc.png)
![image](https://user-images.githubusercontent.com/90270843/146608630-f5cac95c-827f-4eb6-a930-8d2cc45a9d07.png)


Создание и переименование далее
Переименовать файл;
![image](https://user-images.githubusercontent.com/90270843/146608756-0cb4650f-ad0a-41cd-823b-6ac97eaa1a1a.png)
![image](https://user-images.githubusercontent.com/90270843/146608796-c1615df1-0c5d-4be9-aeb5-e90faae67341.png)
![image](https://user-images.githubusercontent.com/90270843/146608859-9b3eabbb-1db0-49a2-bf0d-ba93f855736e.png)
![image](https://user-images.githubusercontent.com/90270843/146608895-3846bc63-be4b-4e78-93c2-7abf3976c3ce.png)
![image](https://user-images.githubusercontent.com/90270843/146608931-dc448d62-85a1-4f65-8ead-0330efdabaff.png)

Удалить файл;

![image](https://user-images.githubusercontent.com/90270843/146609180-9ebbb825-c4cb-4c72-ac4b-ca34ed659d27.png)
![image](https://user-images.githubusercontent.com/90270843/146609206-7dd6f76a-b0a6-454d-b6cf-c15e1b39a789.png)


Скопировать файл с клиента на сервер;
![image](https://user-images.githubusercontent.com/90270843/146609712-c1103eb4-99e0-484e-b5a5-e23a661d1d3f.png)
![image](https://user-images.githubusercontent.com/90270843/146609748-0e67d233-ef16-40c6-80df-5e48df766a3d.png)


Скопировать файл с сервера на клиент;
![image](https://user-images.githubusercontent.com/90270843/146610064-76f84759-88aa-4845-83bf-61f65feae12d.png)
![image](https://user-images.githubusercontent.com/90270843/146610136-b5b88a21-b584-41b0-ad4e-44e73b813c23.png)


Клиент запущен в корневой директории сервера поэтому получается, что скопировали в рабобую директорию клиент, которая является и рабочей директорией сервера
![image](https://user-images.githubusercontent.com/90270843/146610182-afc6caeb-a746-4cca-968f-dcb045db2417.png)


Выход (отключение клиента от сервера);
командой exit закрывается клиентское приложение

Дополнительные задания:
Ограничьте возможности пользователя рамками одной определенной директории. Внутри нее он может делать все, что хочет: создавать и удалять любые файлы и папки. Нужно проследить, чтобы пользователь не мог совершить никаких действий вне пределов этой директории. Пользователь, в идеале, вообще не должен догадываться, что за пределами этой директории что-то есть. Как видно было из предыдщуих скринов выйти за пределы папки - корня не может, а это рабочая папка пользователя у admin эта папка - корень сервера.
![image](https://user-images.githubusercontent.com/90270843/146610443-fcaed98f-5bce-4e1d-b1ef-e5261c29b6e7.png)
![image](https://user-images.githubusercontent.com/90270843/146610466-a2da0050-f0a8-47fe-8ef6-1e0e4782c267.png)


Добавьте логирование всех действий сервера в файл. Можете использовать разные файлы для разных действий, например: подключения, авторизации, операции с файлами. Логи пишутся в файл корень сервера log.txt
![image](https://user-images.githubusercontent.com/90270843/146610693-f4660373-123d-4917-9a1f-360e7c8a5033.png)
![image](https://user-images.githubusercontent.com/90270843/146610741-771cd0ad-650c-44cd-936b-3ecdd2c8221a.png)


Добавьте возможность авторизации пользователя на сервере.
Добавьте возможность регистрации новых пользователей на сервере. При регистрации для пользователя создается новая рабочая папка (проще всего для ее имени использовать логин пользователя) и сфера деятельности этого пользователя ограничивается этой папкой. пользоваталь вводит логин пароль, если такой пользователь не существует - то создается, если существует, то проверяется корректность введенных данных.
![image](https://user-images.githubusercontent.com/90270843/146611034-a3f7aedd-2dbf-44ad-845a-e1f7e5c5a582.png)


Неудачная авторизация 9. Реализуете квотирование дискового пространства для каждого пользователя. По 10Мб на пользователя, пример неудачной попытки:
![image](https://user-images.githubusercontent.com/90270843/146611136-9785725d-d7af-48c5-a12b-09f627cdf27f.png)



Папка весит уже почти 9Мб. попытаемся переместить в нее файл 1,5 Гб

![image](https://user-images.githubusercontent.com/90453727/144827594-dd608ba6-704e-4b24-9ad9-8507d1e5e579.png)

Реализуйте учётную запись администратора сервера.
log/pass = admin/admin, рабочая директория - рабочая директория сервера, то есть папка с папками пользователя 13. Напишите отладочный клиент. Клиент должен подключаться к серверу и в автоматическом режиме тестировать корректность его работы. Используйте подход, аналогичный написанию модульных тестов. Клиент должен вывести предупреждающее сообщение, если сервер работает некорректно. файл ftp-test-client log/pass = test/test
![image](https://user-images.githubusercontent.com/90270843/146611825-efb76595-cb33-4d3d-bb11-3d0d049b20fa.png)
![image](https://user-images.githubusercontent.com/90270843/146611849-66a87e13-1fe5-4010-8e73-8349dc807bd7.png)

