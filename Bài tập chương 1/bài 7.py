class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        if self.month in [1, 3, 5, 7, 8, 10]:  # Tháng có 31 ngày
            if self.day < 31:
                self.day += 1
            else:
                self.day = 1
                self.month += 1
        elif self.month in [4, 6, 9, 11]:  # Tháng có 30 ngày
            if self.day < 30:
                self.day += 1
            else:
                self.day = 1
                self.month += 1
        elif self.month == 2:  # Tháng 2
            if self.is_leap_year(self.year):
                if self.day < 29:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1
            else:
                if self.day < 28:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1
        if self.month > 12:  # Chuyển sang năm tiếp theo
            self.month = 1
            self.year += 1

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Ví dụ sử dụng lớp Date
date = Date(28, 2, 2020)
date.display()  # 28/02/2020
date.next()
date.display()  # 29/02/2020
date.next()
date.display()  # 01/03/2020



    
