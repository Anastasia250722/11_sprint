import requests
import configuration
import data

#1. Создание заказа пользователя с помощью Post-запроса

def post_new_order(order_body): #Объявление функции def post_new_order, которая на вход получает данные и создает заказ

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDERS,  # В теле функции указывается ключевое слово return, после ключевого слова указывается название пакета requests и вызов функции post()
                                                                                     # В качестве аргумента передаются: URL + путь к таблице order
                         json=order_body) # тело запроса

response_order=post_new_order(data.order_body)

assert response_order.status_code==201  #проверяем, что статус ответа 201

print(response_order.status_code)
print(response_order.json())

#2. Сохранение номера заказа
track=response_order.json()["track"]

#3. Запрос на получение заказа по треку заказа

def get_order_track():
    return requests.get(configuration.URL_SERVICE+configuration.GET_ORDER_TRACK)
response=get_order_track()

print(response.status_code)
print(response.json())

#3. Проверяем, что код ответа равен 200

if response.status_code == 200:
    print("Вот заказ по номеру трека")
else:
    print("Провал")

assert response.status_code==200




