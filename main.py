import hashlib

# Simulated database (in real apps, this would be a real DB)
users_db = {
    "shaheer": hashlib.sha256("mypassword123".encode()).hexdigest()
}    
def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

def login():           
  username = input("Enter username: ")
  password = input("Enter password: ")                  

  if username in users_db:
    hashed_input_password = hash_password(password)

    if users_db[username] == hashed_input_password:                                                

      print("✅ Login successful!")                                                        
    else:         
      print("❌ Incorrect password.")                                                                  
  else:                                                                                
    print("❌ User not found.")                                                                                
login()
