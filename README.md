# Курсовой проект по парсингу

жду темы по 35. Pandas (17 января, вторник в 20:00).
Чтобы применить в проекте - сам не разобрался с этой темой

в преспективе переписать на SCRAPY используя многопоточность + контроллируя последовательность записи - но я не разобрался пока как

и Selenium - чтобы сервер не сразу мог понять, что к нему зашел не человек - но я не разобрался пока как

В итоге должен быть csv файл в кодировке windows-1251 для Excel

## Запуск
1) Проверяем версию Git 

git version

2) Переходим в нужную папку (cd) смотрим, что уже там есть (ls)

3) копируем с github.com в данную папку

git clone git@github.com:Evgeny87/Python_Project_Parsing.git

4) Переходим в проект

cd Python_Project_Parsing

5) Проверяем версию python

python3 -V (или python -V)

6) Проверяем версию pip

pip -V

7) обновляем pip

pip install --upgrade pip

===================================================

8) Устанавливаем зависимости

poetry install==1.3.1 (или pip install -r requirements.txt)

===================================================

9) Проверяем зависимости

poetry show --tree

10) запускаем

python3 main.py (или python main.py)
