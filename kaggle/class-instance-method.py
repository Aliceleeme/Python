# Difference between class and instance 
# Date 2019/02/12 

# reference: https://wikidocs.net/1744
#            https://wikidocs.net/85


class Account;                    # class : defined by class at the first line 
  num_accounts = 0 
  def __init__(self, name):       # def A = method on the class 
      self.name= = name           # Self.variable = instance 
      Account.num_accounts += 1
  def __del__(self):
      Account.num_accounts -= 1
      
 
 kim = Account("kim")
 lee = Account("lee")
 
 kim.name       # binding on the name, the instance variable. 
 lee.name       
 
 kim.num_accounts 
 lee.num_accounts   
   
