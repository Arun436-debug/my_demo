
def even_or_odd(num) -> str:
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'
while True:
    num = int(input('Enter the number : '))
    res = even_or_odd(num)
    print(res)