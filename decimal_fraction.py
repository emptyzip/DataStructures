from os import replace
class Fraction:
  def __init__(self, num):
    self.decimal = num
    self.decimal_fraction(self.decimal)

  def __str__(self):
    return str(self.num) + "/" +str(self.den)
  
  def gcd(self, a, b):
    while a % b != 0:
      a, b = b, a%b
    return b

  def decimal_fraction(self, decimal):
    num = decimal.find('.') # num
    num = len(decimal) - num - 1; #소수점 이하 자리수
    dem="1"
    new_num = int(decimal.replace(".","")) #소수
    new_dem = int(dem.ljust(num+1,"0"))
    new_num, new_dem = self.abbreviation(new_num, new_dem)

    print("실수", self.decimal,"의 분수 표현:", new_num, "/", new_dem)

  def abbreviation(self, new_num, new_dem):
      common = self.gcd(new_num, new_dem)
      return (new_num//common,new_dem//common)

num = input("실수를 입력하세요: ")
num1 = Fraction(num)