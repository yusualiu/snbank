#Display login and close options
def showLoginAndClose():
  # {1:'Login',2:'Close App'}
  while True:
    try:      
      print("1. Login \n2. Close App")
      options = int(input("Please choose option 1 or 2? "))
      if(options == 1):
        username = input("What is your username ?")
        password = input("What is your password ?")
        staffData = fetchUserDetails()
        enteredUsername = [staffData[0].strip('\n'),staffData[4].strip('\n')]
        enteredPassword = [staffData[1].strip('\n'),staffData[5].strip('\n')]
        
        if(username in enteredUsername and password in enteredPassword) :
          print("----------You are logged in--------------") 
          #store user data in file sessions
          newSession = storeUserSession(username,password) 
          #Display account opitions        
          showAccountOptions(newSession)            
        else:
          print("------------Please Try again---------------\nYour credentials do not match any record")     
      elif(options == 2):
        print("Closing App ...")
        break
      else:        
          print("------------Please Try again---------------")
    except ValueError:
      print("******Please Enter a valid number******")


# Fetch user credentials from staff files
def fetchUserDetails():  
  with open('staff.txt') as f:
    read_data = f.readlines()
    f.close()
    return read_data


      
def storeUserSession(user,pwd):
  with open("session.txt", "w", encoding='utf-8') as f:
    f.write('{}\n'.format(user))
    f.write('{}\n'.format(pwd))
    sessionsCreated = [user,pwd]
    return sessionsCreated

def loadUserSession():
  with open("session.txt", "r", encoding='utf-8') as f:
    username  = f.readline().rstrip() 
    password  = f.readline().rstrip()
    usersessions = [username,password]
    return usersessions

def removeSession(filename):
  import os
  if os.path.exists(filename):
    os.remove(filename)

def storeAccountDetails(acctList):
  with open('customer.txt', 'w') as file_handler:
    for item in acctList:
      file_handler.write("{}\n".format(item))


def fetchAccountDetails(acctno):
  # KeyWord =['word', 'word1', 'word3']
  with open('customer.txt', 'r') as f:
      read_data = f.readlines()
      f.close()
      if(acctno == read_data[4]):
        return read_data

      

  

def generateAccountNo(n):
  from random import randint
  start = 10**(n-1)
  end = (10**n)-1
  return randint(start,end)

  
      
# storeUserSession()
# print(loadUserSession())

def showAccountOptions(session):  
  try:
    print("1. Create new bank account \n2. Check Account Details \n3. Logout ")
    accountOptions = int(input("Please choose option 1 or 2 or 3? "))
    if(accountOptions == 1):        
      #get user account details for creating account
      accountName = input("Please provide your Account name")
      openingBalance = input("Please provide your Opening balance")
      accountType = input("Please provide your Account Type")
      accountEmail = input("Please provide your Account Email")
      accountNumber = generateAccountNo(10)
      accountDetails = [accountName,openingBalance,accountType,accountEmail,accountNumber]
      # Store details in customer file
      storeAccountDetails(accountDetails)
      print(f'Your account has been created with account number {accountNumber}')
      
      showAccountOptions(session)        
      # print("Account created")
    elif(accountOptions == 2):      
      while(session):
        enteredaccountNumber = input("Please provide your Account Number")
        print("These are your Account details")      
        userAcctDetails = fetchAccountDetails(enteredaccountNumber)
        print(f"1. Your account name is {userAcctDetails[0]} \n2.Your opening balance is {userAcctDetails[1]} \n3. Your account email is {userAcctDetails[2]} \n4. Your account type is {userAcctDetails[3]} \n5. Your account number is {userAcctDetails[4]}")
        
        showAccountOptions(session)
    elif(accountOptions == 3):
      print("------------Please You are logged out---------------")       
      #delete user sessions
      removeSession('session.txt')
    else:
      print("------------Please Try again---------------")
  except ValueError:
    print("******Please Enter a valid number******")
       




# fetchUserDetails()
# print(fetchUserDetails())
showLoginAndClose()