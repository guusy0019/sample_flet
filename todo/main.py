import flet as ft

class ToDoApp:
    def __init__(self, page):
        self.page = page
        self.tasks = []
        self.task_input = ft.TextField(label="Add a new task", width=300)
        self.task_list = ft.Column()

    def add_task(self, e):
        if self.task_input.value.strip():
            new_task = Task(self.task_input.value, self.remove_task)
            self.tasks.append(new_task)
            self.task_list.controls.append(new_task.view)
            self.task_input.value = ""
            self.page.update()

    def remove_task(self, task):
        self.tasks.remove(task)
        self.task_list.controls.remove(task.view)
        self.page.update()

    def build(self):
        return ft.Column(
            controls=[
                self.task_input,
                ft.ElevatedButton(text="Add Task", on_click=self.add_task),
                self.task_list,
            ]
        )

class Task:
    def __init__(self, name, remove_callback):
        self.name = name
        self.remove_callback = remove_callback
        self.view = self.build_view()

    def build_view(self):
        return ft.Row(
            controls=[
                ft.Checkbox(label=self.name),
                ft.IconButton(
                    icon=ft.icons.DELETE, 
                    on_click=lambda e: self.remove_callback(self)
                )
            ]
        )

def main(page: ft.Page):
    page.title = "ToDo List"
    todo_app = ToDoApp(page)
    page.add(todo_app.build())

ft.app(target=main)
