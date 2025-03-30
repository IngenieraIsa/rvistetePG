from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):

    def setUp(self):
        self.item = Item.objects.create(
            name="Test Item",
            description="A test item for circular fashion.",
            price=20.00,
            category="Clothing",
            is_for_sale=True,
            is_for_rent=False
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.description, "A test item for circular fashion.")
        self.assertEqual(self.item.price, 20.00)
        self.assertEqual(self.item.category, "Clothing")
        self.assertTrue(self.item.is_for_sale)
        self.assertFalse(self.item.is_for_rent)

    def test_item_str(self):
        self.assertEqual(str(self.item), "Test Item")