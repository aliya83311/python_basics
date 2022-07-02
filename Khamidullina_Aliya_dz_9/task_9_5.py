class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationary):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationary):
    def draw(self):
        print("Запуск отрисовки маркером")


any_stationary = Stationary("brush")
red_pen = Pen("red_pen")
black_pencil = Pencil("black_pencil")
green_handle = Handle("green_handle")

any_stationary.draw()
red_pen.draw()
black_pencil.draw()
green_handle.draw()