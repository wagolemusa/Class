class fibNumbers:
                                 
  # function print fibonacil numbers
  def fibonaccil(self, number):
    num = [1,2]
    for i in range (2, number):
      num.append(num[i-2]+num[i-1])
    return num

  # function print fibonacil even numbers less than 4000000
  def sum_even_fibonaccil(self, number=1000):
    sum = 0
    for i in self.fibonaccil(number):
      if i % 2 == 0 and i < 4000000:
        sum  = sum+i
    return sum

test = fibNumbers()
print (test.sum_even_fibonaccil())