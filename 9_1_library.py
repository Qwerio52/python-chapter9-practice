# 9.1 图书馆系统程序
class Book:
    def __init__(self, book_name, author, isbn):
        self.book_name = book_name
        self.author = author
        self.isbn = isbn
        self.can_borrow = True

    def borrow(self):
        if self.can_borrow:
            self.can_borrow = False
            print(f"《{self.book_name}》借书成功")
        else:
            print(f"《{self.book_name}》已经借出，暂时不可借")

    def return_book(self):
        if not self.can_borrow:
            self.can_borrow = True
            print(f"《{self.book_name}》还书成功")
        else:
            print(f"《{self.book_name}》未借出，无需归还")

    def check_available(self):
        return self.can_borrow


if __name__ == "__main__":
    b1 = Book("Python编程", "张三", "123456")
    b1.borrow()
    b1.return_book()