from dataclasses import dataclass
from datetime import datetime
from typing import List

import shopify

import utils


@dataclass
class Product:
    name: str
    description: str
    shopify_id: str  # Add the internal Shopify id here
    created_at: datetime

    @classmethod
    def from_shopifyProduct(cls, product: dict):
        return cls(
            name=product.get("title"),
            description=product.get("body_html"),
            shopify_id=product.get("vendor"),
            created_at=utils.datetime_string_to_datetime(
                product.get("created_at")),
        )


@dataclass
class Address:
    address_1: str
    address_2: str
    city: str
    state: str
    country: str
    zip: str

    @classmethod
    def from_shopifyAddress(cls, address: dict):
        return cls(
            address_1=address.get("address1"),
            address_2=address.get("address2"),
            city=address.get("city"),
            state=address.get("province"),
            country=address.get("country"),
            zip=address.get("zip"),
        )


@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str

    @classmethod
    def from_shopifyCustomer(cls, customer: dict):
        return cls(
            first_name=customer.get("first_name"),
            last_name=customer.get("last_name"),
            email=customer.get("email"),
        )

@dataclass
class Order:
    customer_name: str
    customer_address_1: str
    customer_address_2: str
    customer_address_city: str
    customer_address_state: str
    customer_address_country: str
    customer_address_zip: str
    total_price: float
    created_at: datetime

    @classmethod
    def from_shopifyOrder(cls, order: dict):
        customer = Customer.from_shopifyCustomer(
            order.get("customer").attributes
        )
        if customer:
            address = Address.from_shopifyAddress(
                order.get("shipping_address").attributes
            )
            return cls(
                customer_name=customer.first_name,
                customer_address_1=address.address_1,
                customer_address_2=address.address_2,
                customer_address_city=address.city,
                customer_address_state=address.state,
                customer_address_country=address.country,
                customer_address_zip=address.zip,
                total_price=float(order.get("total_price")),
                created_at=utils.datetime_string_to_datetime(
                    order.get("created_at")),

            )
        return None


@dataclass
class OrderItem:
    product: Product
    order: Order
    quantity: int
    price: float

    @classmethod
    def from_shopifyLineItem(cls, item: shopify.LineItem):
        return cls(
            product=Product.from_shopifyProduct(item.attributes),
            order=Order.from_shopifyOrder(item.attributes),
            quantity=item.get("quantity"),
            price=float(item.get("price")),

                   )