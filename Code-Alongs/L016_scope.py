# In python we have 2 types of scope, (life-time of variable)
# Local scope: Only available locally in a function
# Global scope: available through execution of program


name = "Rasmus"

def main():
    name = "Kalle"
    print(name)

print(name)
main()
print(name)


# Python doesn't have block scope, but this is used in most other languages, such as C#, C++, Java
# if name == "Rasmus":
#     last_name = "Berghäll"

# print(last_name)

# for i in range(3):
#     print(i)


# print(f'{i = }')

