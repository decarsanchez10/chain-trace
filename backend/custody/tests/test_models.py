from django.test import TestCase
from custody.models import Asset, Handler

class ModelTestCase(TestCase):
    def test_asset_creation(self):
        asset = Asset.objects.create(asset_uid="AST-001", name="Test Asset")
        self.assertEqual(str(asset), "Test Asset (AST-001)")
