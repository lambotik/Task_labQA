# Task_labQA
### Задание:
Ссылка на страницу Text Box: https://demoqa.com/text-box

Форма: Text Box

Задание:
Написать фрейморк для тестирования этой формы с использованием шаблон проектирования PageObject.

Короткий план:
Заполнить все поля рандомными данными (можно использовать дополнительные библиотеки).
Нажать кнопку Submit
Сравнить введенные данные с полученными данными из поля в котором будут все заполненные данные.

Фремйворк закинуть в репозиторий и дать ссылку.

Примерное время выполнения 1-2 часа.


- 1.Open command line (Win+R)
- 2.For check python version at the command line type : ```python --version```
- 3.If python is not installed: https://www.python.org/downloads/
- 4.After installed python
- 5.Copy this line in command line and press enter: 
```https://github.com/lambotik/Task_labQA.git```
- 6.At the command line, type: ```cd small_test_task_from_ritm```
- 7.At the command line, type: ```pip3 install -r requirements.txt```
- 8.At the command line, type: ```pytest --alluredir=test_result/ tests/```
- 9.At the command line, type: ```allure serve test_result```
