import sqlite3
import stripe


def create_database(api_key,name_database):

# Thiết lập kết nối với cơ sở dữ liệu SQLite
  conn = sqlite3.connect(name_database)
  cursor = conn.cursor()

  # Tạo bảng để lưu trữ thông tin khách hàng từ Stripe
  cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                    customer_id TEXT PRIMARY KEY,
                    name TEXT,
                    email TEXT    
                  )''')

  # Thiết lập Stripe API key
  stripe.api_key = api_key

  # Lấy danh sách khách hàng từ Stripe
  customers = stripe.Customer.list()

# Lặp qua danh sách khách hàng và lưu thông tin vào cơ sở dữ liệu
  for customer in customers.auto_paging_iter():
    cursor.execute('''INSERT OR REPLACE INTO customers (customer_id, name, email)
                      VALUES (?, ?, ?)''',
                      (customer.id, customer.name, customer.email))

  # Lưu các thay đổi vào cơ sở dữ liệu
  conn.commit()

  # Đóng kết nối với cơ sở dữ liệu
  return conn.close()
