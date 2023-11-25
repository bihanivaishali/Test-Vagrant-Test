basket = {
    "Leather wallet": {"quantity": 1, "unit_price": 1100, "gst":18},
    "Cigarette": {"quantity": 4, "unit_price": 900, "gst":12},
    "Umbrella": {"quantity": 12, "unit_price": 200, "gst":8},
    "Haney": {"quantity": 28, "unit_price": 100, "gst":0},
}

max_gst_product = None
max_gst_amount = 0

for product, details in basket.items():
    quantity = details["quantity"]
    unit_price = details["unit_price"]
    gst_amount = details["gst"] * (quantity * unit_price) 

    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product

total_amount = sum(details["quantity"] * details["unit_price"] for details in basket.values())

# Print the output
print("Product with maximum GST:", max_gst_product)
print("Maximum GST amount:", max_gst_amount)
print("Total amount to be paid:", total_amount)