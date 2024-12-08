#task1
class Company:
    instances = []
    def __init__(self, employee):
        self.employee = employee
        self.left = None
        self.right = None
        Company.instances.append(self)

    @classmethod
    def get_instances(cls):
        return cls.instances

CEO = Company("Chief Executive Officer (CEO)-Іванченко Ніна Василівна")
CEO.left = Company("\n--Chief Financial Officer (CFO) - Петренко Василь Федорович")
CEO.right = Company("\n--Human Resources Manager - Залоїло Ніколь Кирилівна")
CEO.left.left = Company("\n---IT- Specialist - Самойленко Алла Ігорівна")
CEO.left.right = Company("\n---Administrative Assistant - Попков Микола Сергійович")
CEO.right.left=Company("\n---Marketing Manager - Гриб Наталя Олександрівна")
CEO.right.right=Company("\n---Sales Manager - Самойленко Івоніка Миколаївна")

instances = Company.get_instances()
for instance in instances:
    print(instance.employee)

#task2
class BookNode:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.left = None
        self.right = None

class BooksTree:
    def __init__(self):
        self.root = None

    def add_book(self, title, genre):
        new_book = BookNode(title, genre)
        if self.root is None:
            self.root = new_book
        else:
            self._add(self.root, new_book)

    def _add(self, current_node, new_book):
        if new_book.title < current_node.title:
            if current_node.left is None:
                current_node.left = new_book
            else:
                self._add(current_node.left, new_book)
        elif new_book.title > current_node.title:
            if current_node.right is None:
                current_node.right = new_book
            else:
                self._add(current_node.right, new_book)

    def search_book(self, title):
        return self._search(self.root, title)

    def _search(self, current_node, title):
        if current_node is None:
            return "Книга не найдена"
        if title == current_node.title:
            return f"Жанр книги '{title}': {current_node.genre}"
        elif title < current_node.title:
            return self._search(current_node.left, title)
        else:
            return self._search(current_node.right, title)

    def get_books_by_genre(self, genre):
        books = []
        self._get_books_by_genre(self.root, genre, books)
        return books

    def _get_books_by_genre(self, current_node, genre, books):
        if current_node is not None:
            if current_node.genre == genre:
                books.append(current_node.title)
            self._get_books_by_genre(current_node.left, genre, books)
            self._get_books_by_genre(current_node.right, genre, books)

tree = BooksTree()
tree.add_book("Воно", "Хоррор")
tree.add_book("Мартін Іден", "Класика")
tree.add_book("Хліб з шинкою", "Автобіографія")
tree.add_book("1984", "Антиутопія")
tree.add_book("Дюна", "Наукова фантастика")

print(tree.search_book("Воно"))
print(tree.search_book("Мартін Іден"))
print(tree.search_book("Дракула"))

print(tree.get_books_by_genre("Класика"))
print(tree.get_books_by_genre("Хоррор"))



