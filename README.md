# Исправление данных в Электронном дневнике

Вы можете исправить оценки (двойки-тройки на **пятёрки**), убрать плохие пометки, добавить похвалу к выбранному предмету.
* Этот код связан с [электронным дневником](https://github.com/devmanorg/e-diary/tree/master). Необходимо развернуть сайт, подключить БД

## Описание функций
```python
def fix_marks(schoolkid):
```
Эта функция исправляет плохие оценки (2, 3 на 5). Для запуска укажите `fix_chastisements("ФИО ученика")`


```python
def fix_chastisements(schoolkid):
```
Эта функция удаляет плохие пометки. Для запуска укажите `fix_chastisements("ФИО ученика")`

```python
def create_commendation(name='', subject=''):
```
Эта функция записывает похвалу за урок. Для запуска укажите `create_commendation('ФИО ученика', 'Предмет')`

## Как использовать
Подразумевается что Python версии 3.5 или более, у вас уже установлен.
Необходимо зайти в `shell` сайта электронного дневника командой
```properties
python manage.py shell
```
Чтобы запустить скрипт: 
1. Можно его целиком “копипастнуть” в `shell`
2. Можно положить файл с кодом рядом с `manage.py` и подключить через `import`.

Второй путь удобнее и надёжнее.




## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте Devman.