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

    def __str__(self):
        return str(self.stack)

# Nhập dữ liệu từ bàn phím
capacity = int(input("Nhập dung lượng tối đa của ngăn xếp: "))
stack = Stack(capacity)

while True:
    action = input("Nhập 'push', 'pop', 'count' hoặc 'exit': ").strip().lower()

    if action == 'push':
        try:
            value = float(input("Nhập phần tử cần thêm: "))
            stack.push(value)
            print(f"Ngăn xếp: {stack}")
        except Exception as e:
            print(e)

    elif action == 'pop':
        try:
            print(f"Phần tử lấy ra: {stack.pop()}")
            print(f"Ngăn xếp: {stack}")
        except Exception as e:
            print(e)

    elif action == 'count':
        print(f"Số phần tử trong ngăn xếp: {stack.count()}")

    elif action == 'exit':
        print("Thoát chương trình.")
        break

    else:
        print("Hành động không hợp lệ.")
