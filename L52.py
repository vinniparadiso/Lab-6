#Vinni Paradiso and Katherine O'Roark
def is_perfect_number(number):
    divide = 0
    for num in range(1, number):
        if number % num == 0:
            divide += num
    if number == divide:
        return True
    else:
        return False

def test_perfect(n):
    for num in range(1,n):
        print(is_perfect_number(num))


print (test_perfect(1000))
print (test_perfect(10000))
