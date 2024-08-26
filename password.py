import random 
import string

def generate_password(length):
   characters = string.ascii_letters +string.digits
   password =''.join(random.choice(characters) for _ in  range(length))

   return password

def is_strong_password(password):
   if len(password) < 8:
      return False
   has_letter = any(c.isalpha() for c in password)
   has_digit = any(c.isdigit() for c in password)
   return has_letter and has_digit

def main():
   while True:
        try:
         password = input("Enter your password: ")
         if not is_strong_password(password):
            print("password should be at least 8 characters long and contain both letters and number.please try again.")
            continue
         
         length = len(password)
         generated_password = generate_password(length)
         print(f"Entered password: {password}")
         print("Entered password: " + "*" *len(password))
         break

        except KeyboardInterrupt:
           print("\nprocess interrupted.Exiting...")
           return
        except Exception as e:
           print(f"An error occurred: {e}")
            
if __name__ == " __main__ ":
  main() 
