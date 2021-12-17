# Основные задания:

Посмотреть содержимое папки; Верхнее окно - клиент, нижнее - сервер.
![image](https://user-images.githubusercontent.com/90453727/144823256-16c4cf36-eba5-4ca9-b6c6-30f382824bdd.png)
![image](https://user-images.githubusercontent.com/90453727/144823584-2628b869-051b-44c0-a7c6-1443411427cb.png)

Создать папку;
![image](https://user-images.githubusercontent.com/90453727/144823630-90353de9-3750-4001-9b05-87bfda73e1d3.png)
![image](https://user-images.githubusercontent.com/90453727/144823649-deb2dfe4-15db-4894-9ddd-e81c6e312fcd.png)
![image](https://user-images.githubusercontent.com/90453727/144823690-f65074fe-3f86-4215-a5c9-2e4206cdd047.png)


Домашняя папка пользователя
![image](https://user-images.githubusercontent.com/90453727/144823816-65979100-f512-4fdc-ae76-d3760de5347e.png)

В ней созданная нами
![image](https://user-images.githubusercontent.com/90453727/144823837-fdcb3bde-dd65-4d5d-a5a0-c8f09fcd8192.png)


Удалить папку;
![image](https://user-images.githubusercontent.com/90453727/144823938-880a9e13-4095-47e3-9439-312078b7c38d.png)
![image](https://user-images.githubusercontent.com/90453727/144823979-27e07f00-75c8-4811-8736-0c5dd4a6ba4a.png)
![image](https://user-images.githubusercontent.com/90453727/144823954-6c60771c-e4e2-4852-8128-c184089d39d6.png)


Создание и переименование далее
Переименовать файл;
![image](https://user-images.githubusercontent.com/90453727/144824926-bf700d21-9f20-4283-8a9f-d008ffcaee98.png)
![image](https://user-images.githubusercontent.com/90453727/144824953-4b8c024e-88d2-4202-8e56-89b3abfeadcb.png)
![image](https://user-images.githubusercontent.com/90453727/144825088-1c3b359d-a89d-4fd4-bb95-c9b4bf54dc35.png)
![image](https://user-images.githubusercontent.com/90453727/144825099-ba3da88f-0f3f-48fa-b1e3-0a471b88148c.png)
![image](https://user-images.githubusercontent.com/90453727/144825148-a6ea8ff5-878a-40cc-9790-906c7b47f7f2.png)
Удалить файл;
![image](https://user-images.githubusercontent.com/90453727/144825224-b0752cee-cc91-41e2-8e10-f649c8dd51e8.png)
![image](https://user-images.githubusercontent.com/90453727/144825254-f7391680-d2bb-4f78-a38d-09f28b0e7021.png)


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
