import requests
from aiogram import Bot, Dispatcher, types

# Настройки бота
bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)


# Функция для получения прогноза погоды
def get_weather(city):
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR_API_KEY&units=metric".format(city)
    )
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temperature": data["main"]["temp"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "wind": {
                "speed": data["wind"]["speed"],
                "direction": data["wind"]["deg"],
            },
            "clouds": data["clouds"]["all"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        return None


# Обработчик команды /weather
@dp.message_handler(commands=["weather"])
async def get_weather_command(message: types.Message):
    city = message.text.split()[1]
    weather = get_weather(city)
    if weather is not None:
        await message.answer(
            f"Погода в городе {city}:\n\nТемпература: {weather['temperature']} °C\nДавление: {weather['pressure']} мм рт. ст.\nВлажность: {weather['humidity']}%\nСкорость ветра: {weather['wind']['speed']} м/с\nНаправление ветра: {weather['wind']['direction']}°\nОблачность: {weather['clouds']}%\nОписание: {weather['description']}"
        )
    else:
        await message.answer("Не могу найти информацию о погоде в этом городе.")

# Запускаем бота
dp.start_polling()