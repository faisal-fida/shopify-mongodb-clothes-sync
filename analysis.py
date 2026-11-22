import shopify

from shopify_uploader import activate_session


def analyze_shopify_results():
    """
    This function analyzes the results of the shopify scraper.
    """
    activate_session()

    total_products = len(shopify.Product.find())
    print(f"Total number of products: {total_products}")


def main():
    analyze_shopify_results()


if __name__ == '__main__':
    main()
