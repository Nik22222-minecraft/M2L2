import telebot
import random
import os
from bot_logic import gen_pass
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("токен")
    
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'''Привет! Я бот {bot.get_me().first_name}!
если что то непонятно пиши /help''')

#Загрезнение окружающей среды и как это исправить
@bot.message_handler(commands=['problem_ecology'])
def send_welcome(message):
    bot.reply_to(message, f'''Проблема загрязнения окружающей среды  — 
это сложная глобальная проблема,
характеризующаяся введением
в окружающую среду вредных веществ и факторов,
                  которые негативно влияют на здоровье человека,
                  животных, растений и экосистемы в целом
/ecology_1 - больше информации для подростка (Начало борьбы с загрезнением)
/ecology_2 - больше информации для взрослого (Начало борьбы с загрезнением)
/ecology_3 - больше информации для того, кто уже начал бороться с загрезнением
/ecology_mem - мем про окружающую среду
''')
    
@bot.message_handler(commands=['ecology_1'])
def send_welcome(message):
    bot.reply_to(message, f'''1.Сортировка мусора:
Это самый простой и эффективный шаг.
Начните сортировать мусор дома,
узнайте, какие виды отходов принимаются
для переработки в вашем городе.
                 
2.Экономия ресурсов:
Выключайте свет, когда выходите из комнаты,
меньше используйте воду,
выбирайте энергосберегающие приборы.

3.Многоразовые вещи:
Используйте многоразовые сумки для покупок,
бутылки для воды, стаканы для кофе.
Откажитесь от одноразовой посуды.
                 
4.Рациональные покупки:
Перед покупкой подумайте,
на самом ли деле вам это нужно.
Выбирайте товары с минимальной упаковкой
или из переработанных материалов.
                 
5.Общественный транспорт:
Если возможно, откажитесь от использования автомобиля
или общественного транспорта,
заместо этого можно ездить на велосипеде
или доходить до нужного вам места пешком.
''')


@bot.message_handler(commands=['ecology_2'])
def send_welcome(message):
    bot.reply_to(message, f'''1. Проведите аудит своего дома:
Определите основные источники загрязнения в вашем доме:
энергопотребление, потребление воды, образование отходов.

2.Проанализируйте свой транспорт:
Какой транспорт вы используете чаще всего?
Есть ли возможность сократить количество поездок на автомобиле?

3.Оцените свой рацион:
Какое количество продуктов животного происхождения вы потребляете?
Откуда поступают продукты в ваш рацион?
Можно ли перейти на более устойчивое питание?
                 
4.Подумайте о своих покупках:
Сколько вещей вы покупаете импульсивно?
Можно ли сократить потребление,
выбирая более качественные и долговечные товары?

''')


@bot.message_handler(commands=['ecology_3'])
def send_welcome(message):
    bot.reply_to(message, f'''1.Сортировка мусора:
Цветовые обозначения:

желтый – пластик;
зеленый – несортированные коммунальные отходы;
оранжевый – опасные отходы;
синий – макулатура;
красный – стекло;
серый – электрооборудование, вышедшее из строя.

2.Заведите дневник:
Заведите дневник или блокнот для 
отслеживания своих экологических действий.
Анализ данных поможет увидеть,
что работает хорошо, а что можно улучшить.

3.Экономия природных ресурсов:
Пытайтесь уменьшить трату электро-энергии или воды

4.Не сдавайтесь:
Изменения требуют времени и усилий.
Не расстраивайтесь из-за неудач,
а воспринимайте их как опыт и возможность для улучшения.
Празднуйте свои успехи, чтобы поддерживать мотивацию.

5.Рациональное потребление:
Перед покупкой любого товара задавайте себе вопрос:
действительно ли он мне нужен?
Можно ли найти альтернативу,
которая менее вредна для окружающей среды?
''')

#Картинки
@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem1'])
def send_mem1(message):
    images = os.listdir('images_0')
    img_name = random.choice(images)
    with open(f'images_0/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['ecology_mem'])
def send_ecology_mem(message):
    images = os.listdir('images_1')
    img_name = random.choice(images)
    with open(f'images_1/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """Что умеет этот бот: 
/start - Запуск бота
/heh - команда которая вскоре будет секретной(запомни команду)
/heh число - команда которая вскоре будет секретной(запомни команду)
/word - Модные слова
/password - Генерация рандомного пароля
/mem - мемы програмиста  (каждый раз появляется рандомный мем)
/mem1 - мемы с котами (каждый раз появляется рандомный мем)
/problem_ecology - экологические проблемы и как их исправить
                 """)

@bot.message_handler(commands=['word'])
def send_hello(message):
    
    bot.reply_to(message, """Модные слова:
Кринж - Что то странное или стыдное
Лол - что то очень смешное
Рофл - шутка
Щищ - одобрение или восторг
Криповый - страшный или пугающий
Агрится - злится
Токсик - агресивное, негативное поведение в онлайне
Спойлер - информация, которая раскрывает ключевые сюжетные повороты или концовку книги, фильма, игры и т.д.
""")

@bot.message_handler(commands=['password'])
def test(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()
