from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            Title="Pizza",
            Price=9.00,
            Inventory=10
        )
        Menu.objects.create(
            Title="Burger",
            Price=7.00,
            Inventory=20
        )

    def test_getall(self):
        items = Menu.objects.all()
        serialized = MenuItemSerializer(items, many=True)

        self.assertEqual(serialized.data[0]['Title'], "Pizza")
        self.assertEqual(serialized.data[1]['Title'], "Burger")