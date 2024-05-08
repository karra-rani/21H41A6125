from flask import Flask, jsonify, request
from product_aggregator import ProductAggregator

app = Flask(__name__)
cache = cachetools.TTLCache(maxsize=100, ttl=60) # Cache with max size 100 and TTL of 1 minute

product_aggregator = ProductAggregator()

@app.route('/categories/<categoryname>/products', methods=['GET'])
def get_products(categoryname):
    n = request.args.get('n', 10, type=int)  # Default n=10
    page = request.args.get('page', 1, type=int)  # Default page=1
    sort = request.args.get('sort')  # Optional sort criteria
    order = request.args.get('order', 'asc')  # Optional sort order (asc/desc)

    cache_key = f"{categoryname}-{n}-{page}-{sort}-{order}"

    if cache_key in cache:
        products = cache.get(cache_key)
    else:
        products = product_aggregator.get_products(categoryname, n, page, sort, order)
        cache.set(cache_key, products)

    return jsonify(products)

@app.route('/categories/<categoryname>/products/<productid>', methods=['GET'])
def get_product_details(categoryname, productid):
    product = product_aggregator.get_product_details(productid)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


PRODUCT AGGREGATOR

import requests
from uuid import uuid4

class ProductAggregator:

    def __init__(self):
        # Replace with actual e-commerce API access details
        self.ecomm_api_urls = {
            "ecomm1": "https://api.ecomm1.com/products",
            "ecomm2": "https://api.ecomm2.com/products",
        }

    def get_products(self, categoryname, n, page, sort, order):
        all_products = []
        for url in self.ecomm_api_urls.values():
            # Simulate API call and data retrieval from each e-commerce platform
            # (Replace with actual API calls and data parsing)
            response = requests.get(url, params={"category": categoryname})
            products = response.json()
            all_products.extend(products)

        # Filter top N products, apply sorting, etc. (logic omitted for brevity)
        filtered_products = self._filter_and_sort_products(all_products, n, page, sort, order)

        # Assign unique IDs to products
        for product in filtered_products:
            product["id"] = str(uuid4())

        return filtered_products

    def get_product_details(self, productid):
        # Simulate API call to retrieve details for specific product ID
        # (Replace with actual API call and data retrieval)
        # ...
        return product_details  # Return product details or None if not found

    def _filter_and_sort_products(self, products, n, page, sort, order):
        # Implement filtering (top N) and sorting logic based on user-specified criteria
        # (Logic omitted for brevity)
        pass
