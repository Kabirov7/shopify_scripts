import shopify
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from settings import SHOP_URL, VERSION, TOKEN, SCOPES
from services import (
    get_orders,
    get_order,
    get_products,
    get_product
)

session = shopify.Session(SHOP_URL, VERSION, TOKEN, SCOPES)

shopify.ShopifyResource.activate_session(session)

shop = shopify.Shop.current

print(get_products(shopify))
print(get_product(shopify, 8361012986177))
print(get_product(shopify, 83610129861700))  # not exists

print(get_orders(shopify))
print(get_order(shopify, 1117430513985))
print(get_order(shopify, 1))  # not exists
