# Task_labQA
## Задание:
Ссылка на страницу Text Box: https://demoqa.com/text-box
Форма: Text Box
- Написать фрейморк для тестирования этой формы с использованием шаблон проектирования PageObject.
### Короткий план:
- Заполнить все поля рандомными данными (можно использовать дополнительные библиотеки).
- Нажать кнопку Submit
- Сравнить введенные данные с полученными данными из поля в котором будут все заполненные данные.
- Фремйворк закинуть в репозиторий и дать ссылку.


## Для запуска
### Версия Python 3.11.2


- 1.Открыть командную строку (нажать сочетание клавиш ```Win+R```) ввести в появившемся окне ```/cmd``` и нажать ```OK```
- 2.Для проверки установлен ли Python на вашем компьютере, ввести в командную строку ```python --version``` и нажать ```ENTER```
- 3.Если Python не установлен, то переходим по ссылке: https://www.python.org/downloads/ и устанавливаем подходящую версию.
- 4.После установки или, если Python уже установлен на ваш компьютер:
- 5.Скопируйте ```https://github.com/lambotik/Task_labQA.git``` в командную строку и нажмите ```ENTER```
- 6.Скопируйте ```cd Task_labQA``` в командную строку и нажмите ```ENTER```
- 7.Скопируйте ```pip3 install -r requirements.txt``` в командную строку и нажмите ```ENTER```
- 8.Скопируйте ```pytest --alluredir=test_result/ tests/``` в командную строку и нажмите ```ENTER```
- 9.Скопируйте ```allure serve test_result``` в командную строку и нажмите ```ENTER```
