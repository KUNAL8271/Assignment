def calculate_discount(product, quantity, total_quantity):
    discount = 0
    discount_name = ""

    # Check discount rules
    if total_quantity > 30 and quantity > 15:
         # 50% discount for quantity exceeding 15 in a product and total quantity exceeding 30
        discount = 0.5 
        discount_name = "tiered_50_discount"
    elif total_quantity > 20:
        discount = 0.1  # 10% discount for total quantity exceeding 20 units
        discount_name = "bulk_10_discount"
    elif quantity > 10:
        discount = 0.05  # 5% discount for quantity exceeding 10 units
        discount_name = "bulk_5_discount"
    elif total_quantity > 15:
        discount = 0.5  # 50% discount for total quantity exceeding 15 units
        discount_name = "tiered_50_discount"
    elif total_quantity > 10:
        discount = 0.05  # 5% discount for total quantity exceeding 10 units
        discount_name = "bulk_5_discount"
    elif total_quantity > 200:
        discount = 10  # $10 flat discount for total cart exceeding $200
        discount_name = "flat_10_discount"

    return discount, discount_name


def calculate_gift_wrap_fee(quantity):
    return 1 * quantity  # $1 per unit


def calculate_shipping_fee(quantity):
    packages = quantity // 10
    if quantity % 10 != 0:
        packages += 1
    return 5 * packages  # $5 per package


def main():
    products = {"Product A": 20, "Product B": 40, "Product C": 50}

    quantities = {}
    gift_wrap = {}
    total_quantity = 0

    for product in products:
        quantities[product] = int(input(f"Enter quantity for {product}: "))
        total_quantity += quantities[product]
        gift_wrap[product] = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"

    subtotal = 0
    total_discount = 0

    for product, price in products.items():
        quantity = quantities[product]
        total_price = quantity * price
        subtotal += total_price

        discount, discount_name = calculate_discount(product, quantity, total_quantity)
        if discount > total_discount:
            total_discount = discount

        print(f"{product}: {quantity} units - ${total_price}")

    subtotal_after_discount = subtotal - (subtotal * total_discount)

    gift_wrap_fee = sum([calculate_gift_wrap_fee(qty) for qty in quantities.values() if gift_wrap[product]])
    shipping_fee = calculate_shipping_fee(sum(quantities.values()))

    total = subtotal_after_discount + shipping_fee + gift_wrap_fee

    print("\nSubtotal: ${:.2f}".format(subtotal))
    print("Discount Applied: {} - ${:.2f}".format(discount_name, subtotal * total_discount))
    print("Shipping Fee: ${:.2f}".format(shipping_fee))
    print("Gift Wrap Fee: ${:.2f}".format(gift_wrap_fee))
    print("Total: ${:.2f}".format(total))


if __name__ == "__main__":
    main()
