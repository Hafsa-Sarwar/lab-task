class Product:
  def _init_(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity can't be less than 1.")
        
        if quantity < 10:
            discount_amount = 0
        elif 10 <= quantity < 100:
            discount_amount = actual_price * 0.10 
        else:
            discount_amount = actual_price * 0.20  
        
        final_price = actual_price - discount_amount
        
        return final_price

    except ValueError as e:
        print("Price calculation failed:", e)
        return None  
    # any other exception
    except Exception as e:
        print("Price calculation failed:", e)
        return None

  def make_purchase(self, quantity):
      pass

product = Product("Laptop", 20, 50000)

product.make_purchase(100)
product.make_purchase(-5)
product.make_purchase(0)

product1 = Product("Watch", 10, 2000)

product1.make_purchase(100)
product1.make_purchase(-5)
product1.make_purchase(0)