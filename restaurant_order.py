# Task 1.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Cannot dequeue from an empty queue')

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Cannot peek from an empty queue')

    def size(self):
        return len(self.items)


# Task 2, 3, 4.

class Order:
    def __init__(self, order_id, items, customer):
        self.order_id = order_id
        self.items = items
        self.customer = customer


class Restaurant:
    def __init__(self):
        self.kitchen_queue = Queue()
        self.customer_queue = Queue()
        self.order_counter = 0

    def place_order(self, items, customer):
        self.order_counter += 1
        order = Order(self.order_counter, items, customer)
        self.kitchen_queue.enqueue(order)
        print(f"Order {order.order_id} has been placed for customer {order.customer}")

    def process_order(self):
        if not self.kitchen_queue.is_empty():
            order = self.kitchen_queue.dequeue()
            print(f"Processing order {order.order_id} for customer {order.customer}")
            self.customer_queue.enqueue(order)
        else:
            print("No orders in the kitchen queue")

    def deliver_order(self):
        if not self.customer_queue.is_empty():
            order = self.customer_queue.dequeue()
            print(f"Order {order.order_id} is ready for customer {order.customer}")
        else:
            print("No orders in the customer queue")


# Task 5.

# Example usage
restaurant = Restaurant()

restaurant.place_order(["Burger", "Fries"], "John")
restaurant.process_order()
restaurant.place_order(["Pizza", "Salad"], "Emma")
restaurant.deliver_order()
restaurant.process_order()
restaurant.place_order(["Pasta", "Garlic Bread"], "Alex")
restaurant.deliver_order()
restaurant.process_order()
restaurant.deliver_order()