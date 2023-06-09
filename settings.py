import os

SHOP_URL = os.getenv("SHOP_URL", "SHOPNAM.myshopify.com")
TOKEN = os.getenv("ADMIN_KEY") # Admin token
VERSION = "2023-04"
SCOPES = [
    "write_order_edits", "read_order_edits", "write_orders", "read_orders",
    "read_products", "write_products", "read_draft_orders",
    "write_draft_orders"
]
