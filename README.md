# shopify-mongodb-clothes-sync

A script that reads women's clothing records from MongoDB and creates matching products in a Shopify store.

## Features

- Reads documents with `category: "Women's Clothing"` from a MongoDB collection (`title`, `description`, `price`, `size`).
- Creates one Shopify product per record, with one variant carrying size and price.
- Prints the total number of products in the shop afterwards.

## Tech stack

Python 3.8+, pymongo, ShopifyAPI.

## Project structure

```
main.py                     read, upload, count
shopify_uploader.py         Shopify session and product creation
analysis.py                 product count
database_handler/mongodb.py MongoDB query
```

## Setup and run

Requires a running MongoDB with a `clothes-data` collection and a Shopify Admin API access token.

| Variable | Purpose |
| --- | --- |
| `SHOPIFY_URL` | Shop domain, for example `your-shop.myshopify.com` |
| `ADMIN_API_KEY` | Shopify Admin API access token |
| `API_VERSION` | Shopify API version, for example `2024-01` |
| `SHOPIFY_VENDOR` | Optional vendor name for created products |
| `MONGODB_URI` | Optional, default `mongodb://localhost:27017` |
| `MONGODB_DB` | Optional, default `tenet-clothes-data` |

```bash
pip install -r requirements.txt
export SHOPIFY_URL=... ADMIN_API_KEY=... API_VERSION=...
python main.py
```

## Limitations

- Not tested against a live shop. Running it creates real products and has no duplicate check.
- No pagination in the product count, so it reports at most one page of results.
- Collection and field names are fixed to the original dataset.
