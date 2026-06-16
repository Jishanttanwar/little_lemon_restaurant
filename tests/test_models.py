from django.test import TestCase
from restaurant.models import Menu 


class MenuTest(TestCase):

    def test_instance(self):
        item = Menu.objects.create(
            Title="Pizza",
            Price=12.99,
            Inventory=100
        )

        self.assertEqual(str(item), "Pizza")