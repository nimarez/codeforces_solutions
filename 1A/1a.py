import math

def main():
   line = input()
   m, n , a = (int(s) for s in line.split(" "))
   print(math.ceil(m / a) * math.ceil(n / a))

if __name__ == '__main__':
   main()