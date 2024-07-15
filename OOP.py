# class student :
#     college_name = "abcd"

#     def __init__(self,name , marks): 
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome,",self.name)

#     def get_marks(self):
#         return self.marks

# s1= student ("avi",85)
# s1.welcome()
# print(s1.get_marks)        

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks 
        

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi",self.name,"your avg score is:",sum/3)   

# s1 = student("tony",[33,55,77])        
# s1.get_avg()



# static methods





class Account:
    def __init__(self,bal , acc):
      self.balance =bal
      self.account_no = acc

    def  debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance,", self.get_balance())


    def  credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance,", self.get_balance())   

    def get_balance(self):
        return self.balance
            

acc1 = Account(10000,12345)            
acc1.debit(1000)
acc1.credit(20000)





# del keyword


    



