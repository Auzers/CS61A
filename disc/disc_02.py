# not complete
def make_keeper(n): 
    
    def f(cond):
        i = 1
        while(i <= n):
                if(cond(i)):
                     print(i)
                i += 1
    return f

def cond(x):
     if(x % 2 == 0):
          return True
     return False
            
def find_digit(k):
    assert k > 0 ,' k must be equal or greater than zero'
    def find(x):
         return x // 10**(k - 1) % 10
    return find

def digits_account(k):
     count = 0
     while(k != 0):
          count += 1
          k //= 10
     return count

def match_maker(k):
     assert k > 0 , 'k must be equal or greater than zero'
     def find(x):
          digits_num = digits_account(x)
          digit = 1
          while(digit <= k):
               i = digit
               get_digit = find_digit(digit)  
               curr = get_digit(x)
               while(i <= digits_num):
                    if(find_digit(i)(x) != curr):
                         return False
                    i += k
               digit += 1
          return True
     return find

 # 实现match_maker更简单的方法
def match_k(k):
     def check(x):
         while x // (10 ** k) > 0:
             if (x % 10) != (x // (10 ** k)) % 10:
                 return False
             x //= 10
         return True
     return check



              
                    
                    

          




















































































         
    
        