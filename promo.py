import random
import string,os,json


# Function random promocode generator
def genrate_promocode(length=8):
    # Generate random promocode
    promocode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return promocode

# Class to manage promocode
class PromoCodeManager:
    def __init__(self,discout_rate,data_file="promocode.json"):
        self.discout_rate = discout_rate
        self.data_file = data_file
        self.promocode = self.load_promocode()
        
    # Function to load promocode from file
    def load_promocode(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file,'r') as f:
                    return json.load(f)
            else:
                return {}
        except:
            return []
        
    # Function to save promocode to file
    def save_promocode(self):
        with open(self.data_file,'w') as f:
            json.dump(self.promocode,f)

    # Create new promocode
    def create_promocode(self):
        promocode = genrate_promocode()
        self.promocode[promocode] = {
            "discount_rate": self.discout_rate,
            "usage": 0
        }
        self.save_promocode()
        return promocode
    
    # Apply promocode
    def apply_promocode(self,promocode):
        if promocode in self.promocode:
            self.promocode[promocode]['usage'] += 1
            self.save_promocode()
            return self.promocode[promocode]['discount_rate']
        return 0
    
# Function to handle user input and apply promocode
def validate_promocode(promocode):
    user_promocode = input("Enter promocode: ").strip()
    discount = promocode.apply_promocode(user_promocode)
    if discount:
        print(f"Promocode applied successfully. Discount rate: {discount}")
    else:
        print("Invalid promocode")
            
        
# Main function
if __name__ == "__main__":
    promocode = PromoCodeManager(discout_rate=0.60)
    new_promocode = promocode.create_promocode()
    print(f"New promocode created: {new_promocode}")
    
    # Validate promocode
    validate_promocode(promocode) 