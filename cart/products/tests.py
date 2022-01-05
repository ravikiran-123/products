from django.test import TestCase
from . models import product_details


class Basictest(TestCase):
    def setup(self):
        product_details.objects.create(Name="Home Appliances",
                                       Description="All types of Appliances are available",
                                       Cost_per_item= 4999,
                                       Stock_quantity= 10,
                                       Volume= 49990)

    def test_get_method(self):
        url="http://127.0.0.1:8000/products/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=product_details.objects.filter(Name="Home Appliances")
        self.assertEqual(qs.count(),0)