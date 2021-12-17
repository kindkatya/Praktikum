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
![image](https://user-images.githubusercontent.com/90453727/144825466-227c4bd6-162d-4e22-8355-4e1a4752d8a1.png)
![image](https://user-images.githubusercontent.com/90453727/144825496-e637886e-10b1-46e6-ac6f-15ec8480ce83.png)


Скопировать файл с сервера на клиент;
![image](https://user-images.githubusercontent.com/90453727/144826140-8bcfacf4-5358-4e4e-b92a-d858eec412ca.png)
![image](https://user-images.githubusercontent.com/90453727/144826183-36a2f05f-0e78-4a35-8328-ff84970d9503.png)


Клиент запущен в корневой директории сервера поэтому получается, что скопировали в рабобую директорию клиент, которая является и рабочей директорией сервера
![image](https://user-images.githubusercontent.com/90453727/144826249-c57b1c06-dc83-438d-8685-c61d30d70d56.png)


Выход (отключение клиента от сервера);
командой exit закрывается клиентское приложение

Дополнительные задания:
Ограничьте возможности пользователя рамками одной определенной директории. Внутри нее он может делать все, что хочет: создавать и удалять любые файлы и папки. Нужно проследить, чтобы пользователь не мог совершить никаких действий вне пределов этой директории. Пользователь, в идеале, вообще не должен догадываться, что за пределами этой директории что-то есть. Как видно было из предыдщуих скринов выйти за пределы папки - корня не может, а это рабочая папка пользователя у admin эта папка - корень сервера.
![image](https://user-images.githubusercontent.com/90453727/144826420-e8f17e7c-a194-442a-a657-dab34af43275.png)
![image](https://user-images.githubusercontent.com/90453727/144826440-b1491810-f882-4a17-8912-ba8606153348.png)


Добавьте логирование всех действий сервера в файл. Можете использовать разные файлы для разных действий, например: подключения, авторизации, операции с файлами. Логи пишутся в файл корень сервера log.txt
![image](https://user-images.githubusercontent.com/90453727/144826508-24744e73-1d68-452f-a7f4-ba0e1b4ae3ab.png)
![image](https://user-images.githubusercontent.com/90453727/144826548-c1ae00cc-94eb-464b-8999-4594f3ec10ec.png)


Добавьте возможность авторизации пользователя на сервере.
Добавьте возможность регистрации новых пользователей на сервере. При регистрации для пользователя создается новая рабочая папка (проще всего для ее имени использовать логин пользователя) и сфера деятельности этого пользователя ограничивается этой папкой. пользоваталь вводит логин пароль, если такой пользователь не существует - то создается, если существует, то проверяется корректность введенных данных.
![image](https://user-images.githubusercontent.com/90453727/144826810-1d930081-a1cd-48b2-939b-441c9262847f.png)


Неудачная авторизация 9. Реализуете квотирование дискового пространства для каждого пользователя. По 10Мб на пользователя, пример неудачной попытки:
![image](https://user-images.githubusercontent.com/90453727/144826913-65914878-074b-4b55-9478-7f6b513d5319.png)



Папка весит уже почти 9Мб. попытаемся переместить в нее файл 1,5 Гб

![image](https://user-images.githubusercontent.com/90453727/144827594-dd608ba6-704e-4b24-9ad9-8507d1e5e579.png)

Реализуйте учётную запись администратора сервера.
log/pass = admin/admin, рабочая директория - рабочая директория сервера, то есть папка с папками пользователя 13. Напишите отладочный клиент. Клиент должен подключаться к серверу и в автоматическом режиме тестировать корректность его работы. Используйте подход, аналогичный написанию модульных тестов. Клиент должен вывести предупреждающее сообщение, если сервер работает некорректно. файл ftp-test-client log/pass = test/test
![image](https://user-images.githubusercontent.com/90453727/144827674-21d2d403-56ae-43d9-aa72-e4b8fefa96b2.png)
