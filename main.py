def calculate_total_price(price, tax_rate, discount=0):
   discounted_price = price * (1 - discount)
   total_price = discounted_price * (1 + tax_rate)
   return total_price

def main():
     price = 100
     tax_rate = 0.07
     discount = 0.1

     total = calculate_total_price(price, tax_rate, discount)
     print("Total price after discount and tax: ", total)
     
