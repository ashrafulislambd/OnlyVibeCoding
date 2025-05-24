def get_all_products_summary():
    from .models import Product  # make sure it's in the same app or import correctly
    products = Product.objects.all()

    if not products:
        return "No products available."

    summary = ""

    for product in products:
        summary += f"""
🔹 Product Name: {product.name}
   - Type: {'Service' if product.listing_type == 'service' else 'Physical Product'}
   - Pricing: {dict(Product.PRICING_TYPES).get(product.pricing_type)}
   - Visibility: {dict(Product.VISIBILITY_MODES).get(product.visibility)}
   - Category: {product.category.name if product.category else 'Uncategorized'}
   - Price: ${product.price}
   - Starting Bid: ${product.starting_bid if product.starting_bid else 'N/A'}
   - Posted By: {product.user.username}
   - Description: {product.description[:100]}...
   - Image: {'Available' if product.image else 'No Image'}
---------------------------------------------------
"""
    return summary
