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
      def make_purchase(self, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity can't be less than 1.")
            if quantity > self.amount:
                raise ValueError(f"out of stock. Only {self.amount} items.")
            
            total_price = self.get_price(quantity)
            if total_price:
                self.amount -= quantity
                print(f"purchase successfull. Total price: {total_price}")
                print(f"Remaining stock: {self.amount} items")
        
        except ValueError as e:
            print("Purchase failed:", e)
        except Exception as e:
            print("error: " ,e)
