# Курсовой проект по парсингу

main.py - первый вариант запуска

main2.py - второй вариант запуска (использовал PANDAS)

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

poetry install (или pip install -r requirements.txt)

===================================================

9) Проверяем зависимости

poetry show --tree

10) запускаем

python3 main.py (или python main.py)

===================================================

pylint

pylint $(git ls-files '*.py')

С – конвенция (convention)

R – рефакторинг (refactor)

W – предупреждение (warning)

E – ошибка (error)
