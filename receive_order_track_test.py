#Анна Клименко, 9-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# функция для получения трека заказа

def receive_track():
    # В переменную new_order сохраняется результат запроса на создание заказа
    new_order = sender_stand_request.post_new_order(data.order_body)
    # В переменную track_number сохраняется значение трэк номера
    track_number = new_order.json()["track"]
    # возвращается значение track_number
    return track_number

#save = receive_track() # в переменную save сохраняется функция для получения трека заказа
#print(save) # вывод на экран трек заказа

# функция для получения заказа по его номеру
def truck_order_assert():
    track = receive_track()
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER_PATH + track)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200

def test_order():
    truck_order_assert