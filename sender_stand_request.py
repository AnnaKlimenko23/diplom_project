import configuration
import requests
import data

# функция запроса на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body)  # тут тело

#response = post_new_order(data.order_body)
#print(response.json())