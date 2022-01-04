
class dsa:
    
    
    
    def get_even(self,ls):
        for i in ls:
            if i%2!=0:
                continue
            print(i)
            
    def cal_itr(self, number):
        """calculating the sqr of a number using the method of iteration 

        Args:
            number ([int]): [number to start the counter from]
        """
        while number >0:
            result = number**2
            print(result)
            number-=1
        
    def calc_sqr_recursive(self, number):
        if number > 0:
            results = number**2
            print(results)
            # print(number)
            return self.calc_sqr_recursive(number-1)
        
    def tree_recursion(self, number):
            if number > 0:
                self.tree_recursion(number - 1)
                res = number ** 2
                print(res)
                self.tree_recursion(number - 1)
                
    def sum_n_numbers(self, n):
        if n!=0:
            return self.sum_n_numbers(n-1)+n
        return 0
              
even = dsa()
print(even.sum_n_numbers(2))