<h1 align="center"><a href="https://skillfactory.ru"><img src="https://github.com/LEgorro/SF-Hackathon.2023/blob/main/assets/SkillFactory.png" align="center" height="22" width="270" ></a></br>Мегахакатон 2023</h1>


Привет!
Меня зовут Егор, я тестировщик-автоматизатор на Python.

Здесь моя работа по тестированию кейса №10 из Мегахакатона 2023.

В кейсе №10 для тестирования предоставлена только одна страница сайта, на которой есть несколько ссылок. В связи с этим решил взять для себя более сложную задачу: заняться автотестированием. Помимо этого захотелось так же научится чему-то новому, и сделать то, чего раньше не далал, а именно построить процесс автотестирования включая CI/CD. Собственно этому и посвятил всё время.
Был создан этот репозиторий. В IDE Aqua от JetBrains были подцеплены PyTest. Разработаны парочка тестов на проверку работоспособности ссылок. Настроен CI/CD через GitHub Actions (написан базовый .github/workflows.config.yml)
Также настроено создание Allure-отчётов с сохранением истории запусков и трендом.

Процесс запуска тестов:
Тесты настроены с помощью GitHub Actions. Необходимо перейти во вкладку Actions, выбрать UI Tests и запустить Workflow:

<img src="https://github.com/LEgorro/SF-Hackathon.2023/blob/main/assets/Screenshoot_1.JPG">

Далее можно наблюдать процесс создания виртуальных машин, сбора артефактов для создания Allure-отчётов, непосредственно прохождение тестов и в конце генерация и публикация отчёта:

<img src="https://github.com/LEgorro/SF-Hackathon.2023/blob/main/assets/Screenshoot_2.JPG">
<img src="https://github.com/LEgorro/SF-Hackathon.2023/blob/main/assets/Screenshoot_2.1.JPG">

Все шаги успешно пройдены:
<img src="https://github.com/LEgorro/SF-Hackathon.2023/blob/main/assets/Screenshoot_3.JPG">
