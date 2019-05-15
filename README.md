# VShaurme

Каркас для социальной сети «ВШаурме»

## Как установить локально

### Скачать исходный код

Сделать это можно тремя путями:

- командой `$ git clone https://github.com/400-badrequestteam/vshaurme`
- с помощью [Github Desktop](https://desktop.github.com)
- скачать zip-архивом с помощью кнопки «Download as Zip»

**download_repo.jpg**

### Скачать зависимости

Убедитесь, что вы находитесь в папке с проектом:

```
$ cd vshaurme
```

и установите зависимости:

```
$ pip install -r requirements.txt
```

### Запустить

Дело за малым: наполнить сайт фейковыми данными и запустить:

```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

Сайт будет доступен по адресу `http://127.0.0.1:5000/`.


<<<<<<< HEAD
## Как задеплоить изменения на хостинг pythonanywhere.com

**Схема - следующая:**

  Разработка ведется локально на машинах. После внесения изменений в код и локального коммита, изменения пушатся на удаленный github-репозиторий.
  Далее, необходимо убедиться, что изменения доехали до репозитория. В репозиторий должен подтянуться ваш коммит:
  
  **commit_is_ok.jpg**   
  
  Если все в порядке, тогда переходим к следующим шагам:
 

- Логинимся на [pythonanywhere.com](https://www.pythonanywhere.com) под пользователем `400badrequestteam`
- Переходим во вкладку `consoles` -> `Your consoles` и кликаем на экземпляр консоли:

**go_to_console.jpg**

- Переходим в директорию проекта:  
    `cd /home/400badrequestteam/vshaurme`
- Приглашение командной строки должно выглядеть так:  
`(vshaurme-venv) 08:45 ~/vshaurme (master)$`  
- Выполняем команду `git pull`. Результат должен быть примерно такой:


**git_pull.jpg**

- Переходим во вкладку `web`:

**go_to_web.jpg** 

- Кликаем `Reload` (перезагружаем приложение):

**reload_app.jpg**

- Проверяем, что [сайт](http://400badrequestteam.pythonanywhere.com/) работает. Ошибок быть не должно.


## Как откатить неудачные обновления
- В первую очередь проверяем и анализируем логи сервера на предмет ошибок:  
  [Access log](400badrequestteam.pythonanywhere.com.access.log)  
  [Error log](400badrequestteam.pythonanywhere.com.error.log)  
  [Server log](400badrequestteam.pythonanywhere.com.server.log)
  
- Переходим во вкладку `consoles` -> `Your consoles` и кликаем на экземпляр консоли
- Переходим в директорию проекта:  
    `cd /home/400badrequestteam/vshaurme`
- Приглашение командной строки должно выглядеть так:  
`(vshaurme-venv) 08:45 ~/vshaurme (master)$`
- Выполняем команду `git reset --hard HEAD@{1}`.   
Вывод должен быть примерно такой:  
`(vshaurme-venv) 09:39 ~/vshaurme (master)$ git reset --hard HEAD@{1}`                                                                                         
`HEAD is now at e268ef1 configure main.py for pythonanywhere deploy`
- Перезагружаем приложение и убеждаемся, что [сайт](http://400badrequestteam.pythonanywhere.com/) работает 
=======
## Как задеплоить изменения на хостинг на Repl.it

1. Залогиниться на [pythonanywhere.com](https://www.pythonanywhere.com) под пользователем `400badrequestteam`
2. Перейти во вкладку `consoles` -> `Your consoles` и кликнуть на экземпляр консоли


>>>>>>> 6d8d4600b2e654846e614d1a26f6b56d13d919a4


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке [Devman](http://dvmn.org).
