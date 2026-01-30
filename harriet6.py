name = "Bob"
if name == "Bob":
 print("hello,Bob!")
else:
 print("I don't know you")


 
def personal_greet(name): 
    # This function should print personal greet "hello,alice!welcome to python"
    print(f"hello,{name}!Welcome to python")   
personal_greet("Alice")
personal_greet("Charlie")

numbers = [1,2,3,4,5]
if (count := len(numbers)) > 3:
    print(f"list has {count} elements")

x = 5
y = 3
print(x == y)
print(x !=y)
print( x > y)
print(x < y)
print(x >= y)
print(x <=  y)

x = 5
print(1 < x <10)
print(1 < x and x < 10)

x = 5
print(x < 5 and x > 10)

x = 5
print(not(x > 3 and x < 10))


x=["apple","banana"]
y=["apple", "banana"]
z=x
print(x is y)
print(x is z)
print(x==y)

x=["apple","banana"]
y=["apple", "banana"]
print(x is not y)

x = [1,2,3]
y = [1,2,3]
print(x==y)
print(x  is y)

fruits=("apple, banana, cheery")
print("pineapple"not in fruits)

txt = "hello,world"
print("h" in txt)
print("hello" in txt)
print("z" not in txt)
print(6 ^ 3)
print( 100 + 5 * 3)

print(5+4-7+3)