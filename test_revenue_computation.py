import unittest
import pandas as pd
from io import StringIO
from main import read_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_10_customers_by_revenue

class TestRevenueComputation(unittest.TestCase):

    def setUp(self):
        data = StringIO("""
        order_id,customer_id,order_date,product_id,product_name,product_price,quantity
        1,1,2023-01-01,101,ProductA,10.0,2
        2,1,2023-02-01,102,ProductB,20.0,1
        3,2,2023-01-15,101,ProductA,10.0,1
        4,2,2023-03-10,103,ProductC,30.0,1
        5,3,2023-03-05,101,ProductA,10.0,3
        """)
        self.df = pd.read_csv(data)

    def test_monthly_revenue(self):
        result = compute_monthly_revenue(self.df)
        expected = pd.DataFrame({
            'year_month': pd.to_datetime(['2023-01', '2023-02', '2023-03'], format='%Y-%m').to_period('M'),
            'revenue': [30.0, 20.0, 60.0]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_product_revenue(self):
        result = compute_product_revenue(self.df)
        expected = pd.DataFrame({
            'product_id': [101, 102, 103],
            'revenue': [60.0, 20.0, 30.0]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_customer_revenue(self):
        result = compute_customer_revenue(self.df)
        expected = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'revenue': [40.0, 40.0, 30.0]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_top_10_customers(self):
        customer_revenue = compute_customer_revenue(self.df)
        result = top_10_customers_by_revenue(customer_revenue)
        expected = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'revenue': [40.0, 40.0, 30.0]
        }).sort_values(by='revenue', ascending=False).head(10)
        pd.testing.assert_frame_equal(result, expected)

if __name__ == "__main__":
    unittest.main()
