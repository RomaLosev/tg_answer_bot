## Telegram бот для ответа на вопросы по методу магического шара
Отвечает на вопросы с контекстом "Стоит ли мне это делать?"
 
### Установка

---
**Скопировать репозиторий на свой компъютер**
```
git clone git@github.com:RomaLosev/tg_answer_bot.git
```
---
**Перейти в папку с проектом**
```
cd tg_answer_bot
```
---
**Создать и запустить виртуальное окружение**
```
python -m venv venv
source venv/scripts/activate #for windows
. venv/bin/activate #for Mac
```
---
**Установить зависимости**
```
pip install -r requirements.txt
```
---
**Создать и заполнить файл `.env`**

`TELEGRAM_TOKEN = 'str' `

---
**Зарегистрировать бота у [BotFather](https://t.me/BotFather)**

---

Запустить файл `answer_bot.py`