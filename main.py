import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def compute_monthly_revenue(df):
    df['revenue'] = df['product_price'] * df['quantity']
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year_month'] = df['order_date'].dt.to_period('M')
    return df.groupby('year_month')['revenue'].sum().reset_index()

def compute_product_revenue(df):
    df['revenue'] = df['product_price'] * df['quantity']
    return df.groupby('product_id')['revenue'].sum().reset_index()

def compute_customer_revenue(df):
    df['revenue'] = df['product_price'] * df['quantity']
    return df.groupby('customer_id')['revenue'].sum().reset_index()

def top_10_customers_by_revenue(customer_revenue):
    return customer_revenue.sort_values(by='revenue', ascending=False).head(10)

if __name__ == "__main__":
    df = read_data('orders.csv')
    
    monthly_revenue = compute_monthly_revenue(df)
    print("Monthly Revenue:\n", monthly_revenue)
    
    product_revenue = compute_product_revenue(df)
    print("Product Revenue:\n", product_revenue)
    
    customer_revenue = compute_customer_revenue(df)
    print("Customer Revenue:\n", customer_revenue)
    
    top_10_customers = top_10_customers_by_revenue(customer_revenue)
    print("Top 10 Customers:\n", top_10_customers)
