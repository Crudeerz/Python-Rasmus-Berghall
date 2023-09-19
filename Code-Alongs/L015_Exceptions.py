'''

SyntaxError- fel syntax, t.ex. fattas parantes osv
RuntimeError
    NameError- t.ex. printa ut en odefinerad variabel
    TypeError- Concatinera sträng med int osv    
LogicalError- allt körs men resultatet blir inte som tänkt

'''

def user_input_point(prompt = "Input: "):
    while True:    
        try:
            inp = int(input(prompt))
            if 0 < inp:
                return inp
        except ValueError:
            print(f'Your input is not an integer value! Try again')
             
        else: 
            print(f"Your input can not be a negative value! Try again")

            


age = user_input_point("Input age: ")
height = user_input_point("Input height: ")
weight = user_input_point()
print(f"age = {age}, height = {height}, {weight}")


        
             