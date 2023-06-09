from dto.data_classes import Order
from utils import print_list_of_dataclass


def get_orders(shopify):
    try:
        orders = shopify.DraftOrder.find()
    except Exception as e:
        print(f"Trouble with getting orders. {e}")
        return None

    orders = [Order.from_shopifyOrder(o.attributes)
              for o in orders]

    print_list_of_dataclass(orders)

    return orders


def get_order(shopify, id_: int):
    try:
        return Order.from_shopifyOrder(
            shopify.DraftOrder.find(id_).attributes
        )
    except Exception as e:
        print(f"Trouble with getting order with id {id_}. {e}")
        return None
