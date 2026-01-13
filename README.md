Необходимо установить зависимости: pip install pytest selenium allure-pytest
Чтобы сгенерировать отчёт в Allure нужно проделать следующие шаги:
Запустить тесты с помощью команды pytest --alluredir allure-result
Эта команда запустит тесты с помощью Pytest в исходной дериктории и сохранит результаты в папку allure-result
Выполнить команду allure serve allure-result 
Она сгенерирует отчёт и папки allure-result и поднимет сервер для просмотра через браузер