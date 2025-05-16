# Operation: Avoid Deep Nesting by Using Helper Functions

# Bad practice: Nested conditionals
def process_order(order):
    if order.status == "paid":
        if order.delivery_time < 3:
            if order.items_available:
                process_payment(order)
            else:
                handle_unavailable_items(order)

# Improved with helper functions
def is_order_paid(order):
    return order.status == "paid"

def is_delivery_time_ok(order):
    return order.delivery_time < 3

def are_items_available(order):
    return order.items_available

def process_order(order):
    if is_order_paid(order) and is_delivery_time_ok(order) and are_items_available(order):
        process_payment(order)
    else:
        handle_unavailable_items(order)

# Output:
# The code is more readable, with each condition encapsulated in its own function.
