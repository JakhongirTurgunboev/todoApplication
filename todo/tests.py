from django.test import TestCase
from .models import Task
from account.models import CustomUser


class TaskTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(username="john",
                                         password="1234john",
                                         email="john@example.com")
        Task.objects.create(
            title="Dars qilish",
            task_text='Python bo\'yicha uyga vazifa qilish',
            user=user)

    def test_task(self):
        """Task saved properly"""
        task1 = Task.objects.filter(title="Dars qilish")[0]
        self.assertEqual(task1.task_text, 'Python bo\'yicha uyga vazifa qilish')
