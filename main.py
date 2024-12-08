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