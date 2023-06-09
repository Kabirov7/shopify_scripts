from dto.data_classes import Product
from utils import print_list_of_dataclass


def get_products(shopify):
    try:
        products = shopify.Product.find()
    except Exception as e:
        print(f"Trouble with getting products. {e}")
        return None
    products = [Product.from_shopifyProduct(p.attributes)
                for p in products]

    print_list_of_dataclass(products)

    return products


def get_product(shopify, id_: int) -> Product:
    try:
        return Product.from_shopifyProduct(
            shopify.Product.find(id_).attributes
        )
    except Exception as e:
        print(f"Trouble with getting product with id {id_}. {e}")
        return None
