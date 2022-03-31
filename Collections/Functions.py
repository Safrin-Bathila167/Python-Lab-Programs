Prime Number Checking:
  def prime_check(n):
  c=0
  if n!=1:
    for i in range (1,n+1):
      if(n%i==0):
        c=c+1
  if(c==2):
    print("it is a prime number")
  else:
    print("it is not a prime number")

n=int(input("enter a number : "))
prime_check(n)
Count Vowels:
  word=input("Enter the string:")
def word_count(word):
  vowel= 0
  consonant=0
  for j in word:
      if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
        vowel=vowel+1
      else:
        consonant=consonant+1
  print("Number of vowels in the word:",vowel)
  print("Number of consonants in the word:",consonant)
word_count(word)
Count Positive and Negative Number:
  list=[-71,-10,56,24,-90,43,-16]
def numbers(num):
  pos= 0
  neg=0
  for j in num:
      if(j>0):
        pos=pos+1
      else:
        neg=neg+1
  print("Number of positive numbers:",pos)
  print("Number of negative number:",neg)
numbers(list)
Range from 1 to 25:
  def num(range):
  a=1
  b=25
  for i in range(a,b+1):
    if (i%5!=0):
      print(i)
num(range)
Return Product:
  def product_or_sum(p,q):
  sum=0
  rem=0
  product=p*q
  if(product > 500):
    print("product of ",p," and ",q," is greter than 500 ")
    print("product is : ",product)
    while(product>0):
      rem = product % 10
      sum=sum+rem
      product=product//10
    print("sum of their product is ",sum)
  else:
    print("product is : ",product)

n1=int(input("enter n1 value : "))
n2=int(input("enter n2 value : "))
product_or_sum(n1,n2)
