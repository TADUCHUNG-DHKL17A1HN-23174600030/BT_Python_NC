class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, item):
        if self.is_full():
            raise Exception("Ngăn xếp đã đầy!")
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Ngăn xếp đang trống!")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Ngăn xếp đang trống!")
        return self.stack[-1]

    def count(self):
        return len(self.stack)

    def print_stack(self):
        """In nội dung của ngăn xếp."""
        if self.is_empty():
            print("Ngăn xếp đang trống.")
        else:
            print("Nội dung ngăn xếp:", self.stack)

# Nhập dữ liệu từ bàn phím
capacity = int(input("Nhập dung lượng tối đa của ngăn xếp: "))
stack = Stack(capacity)

while True:
    action = input("Nhập 'push', 'pop', 'count', 'print' hoặc 'exit': ").strip().lower()

    if action == 'push':
        try:
            value = float(input("Nhập phần tử cần thêm: "))
            stack.push(value)
            stack.print_stack()
        except Exception as e:
            print(e)

    elif action == 'pop':
        try:
            print(f"Phần tử lấy ra: {stack.pop()}")
            stack.print_stack()
        except Exception as e:
            print(e)

    elif action == 'count':
        print(f"Số phần tử trong ngăn xếp: {stack.count()}")

    elif action == 'print':
        stack.print_stack()

    elif action == 'exit':
        print("Thoát chương trình.")
        break

    else:
        print("Hành động không hợp lệ.")
