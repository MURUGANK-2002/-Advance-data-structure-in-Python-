from collections import deque

class CustomerServiceQueue:
    def __init__(self):
        self.customer_queue = deque()

    def add_customer(self, customer_name):
        self.customer_queue.append(customer_name)
        print(f"Customer '{customer_name}' added to the queue.")

    def serve_customer(self):
        if self.customer_queue:
            customer = self.customer_queue.popleft()
            print(f"Serving customer: {customer}")
        else:
            print("No customers in the queue.")

    def view_queue(self):
        if self.customer_queue:
            print("Customers in queue:", list(self.customer_queue))
        else:
            print("The queue is empty.")

if __name__ == "__main__":
    service_queue = CustomerServiceQueue()
    while True:
        print("\n--- Customer Service Menu ---")
        print("1. Add a Customer to Queue")
        print("2. Serve a Customer")
        print("3. View Queue")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter the customer name: ")
            service_queue.add_customer(customer_name)
        elif choice == "2":
            service_queue.serve_customer()
        elif choice == "3":
            service_queue.view_queue()
        elif choice == "4":
            print("Exiting the Customer Service System.")
            break
        else:
            print("Invalid choice! Please try again.")
