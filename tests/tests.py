import datetime
import unittest
from unittest import mock
import shopify
import ssl

from dto.data_classes import Product, Order
from services import (
    get_orders,
    get_order,
    get_products,
    get_product
)

ssl._create_default_https_context = ssl._create_unverified_context


def generate_product(i: int):
    product = shopify.Product()
    product.title = 'name ' + str(i)
    product.body_html = 'body_html ' + str(i)
    product.vendor = 'name shop ' + str(i)
    product.created_at = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
    return product


def generate_address(i: int):
    address = shopify.Address()
    address.address1 = f"address1 {i}"
    address.address2 = f"address2 {i}"
    address.city = f"city {i}"
    address.province = f"province {i}"
    address.country = f"country {i}"
    address.zip = f"zip {i}"
    return address


def generate_customer(i: int):
    address = shopify.Address()
    address.first_name = f"first_name {i}"
    address.last_name = f"last_name {i}"
    address.email = f"email {i}"
    return address


def generate_order(i: int):
    order = shopify.DraftOrder()
    order.customer = generate_customer(i)
    order.shipping_address = generate_address(i)
    order.total_price = str(i*199.2)
    order.created_at = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
    return order


class ProductTests(unittest.TestCase):

    @mock.patch('shopify.Product.find')
    def test_get_products(self, mock_find_products):
        mock_find_products.return_value = [generate_product(i) for i in
                                           range(5)]
        products = get_products(shopify)
        self.assertEqual(len(products), 5)
        generated_products = [
            Product.from_shopifyProduct(generate_product(i).attributes) for i
            in range(5)
        ]
        self.assertEqual(products, generated_products)

    @mock.patch('shopify.Product.find')
    def test_get_product_success(self, mock_find_products):
        mock_find_products.return_value = generate_product(1)
        product = get_product(shopify, 1)
        product_data = Product.from_shopifyProduct(
            generate_product(1).attributes)

        self.assertEqual(product, product_data)

    @mock.patch('shopify.Product.find')
    def test_get_product_not_found(self, mock_find_product):
        mock_find_product.side_effect = Exception("Not found.")
        self.assertEqual(get_product(shopify, 1), None)


class OrderTests(unittest.TestCase):

    @mock.patch('shopify.DraftOrder.find')
    def test_get_orders(self, mock_find_orders):
        mock_find_orders.return_value = [generate_order(i) for i in
                                         range(5)]
        orders = get_orders(shopify)
        self.assertEqual(len(orders), 5)
        generate_orders = [
            Order.from_shopifyOrder(generate_order(i).attributes) for i
            in range(5)
        ]
        self.assertEqual(orders, generate_orders)

    @mock.patch('shopify.DraftOrder.find')
    def test_get_product_success(self, mock_find_order):
        mock_find_order.return_value = generate_order(1)
        order = get_order(shopify, 1)
        order_data = Order.from_shopifyOrder(
            generate_order(1).attributes)

        self.assertEqual(order, order_data)

    @mock.patch('shopify.DraftOrder.find')
    def test_get_product_not_found(self, mock_find_order):
        mock_find_order.side_effect = Exception("Not found.")
        self.assertEqual(get_order(shopify, 1), None)


if __name__ == '__main__':
    unittest.main()
