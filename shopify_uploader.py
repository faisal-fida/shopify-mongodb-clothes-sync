import os

import shopify


def activate_session():
    """Open a Shopify Admin API session from environment variables."""
    session = shopify.Session(
        os.environ["SHOPIFY_URL"],
        os.environ["API_VERSION"],
        os.environ["ADMIN_API_KEY"],
    )
    shopify.ShopifyResource.activate_session(session)


def upload_data_to_shopify(data):
    """Create one Shopify product per item in data."""
    activate_session()

    for item in data:
        product = shopify.Product()
        product.title = item['title']
        product.body_html = item['description']
        product.product_type = "Women's Clothing"
        product.vendor = os.environ.get("SHOPIFY_VENDOR", "Your Vendor Name")

        variant = shopify.Variant({'option1': item['size'], 'price': item['price']})
        product.variants = [variant]

        product.save()
