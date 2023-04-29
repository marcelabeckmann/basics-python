
def hello_world():
    print("Hello, World!")

def hello_world_name(first_name):
    print(f"Hello, {first_name}!")

def hello_world_args(*args):
    first_name=args[0]
    second_name=args[1]
    thrid_name=args[2]

    #print(args)
    #print(type(args))
    #print(first_name)
    print(f"Hello, {first_name} / {second_name} / {thrid_name} !")

def hello_world_keyword_args(first_person, second_person):
    print(f"Hello, {first_person} / {second_person}")

def hello_world_arbitrary_keyword_args(**kwargs):
    #print(kwargs)
    #print(kwargs.get('second_person'))
    #print(kwargs.get('first_person'))
    if kwargs.get('second_person') is None:
        print("No hay segunda persona")
    else:
        print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']}!")

#hello_world()
#hello_world_name("Marcela")
#hello_world_name("Laura")
#hello_world_args("Sebastian", "Daniel", "Vanessa")
#hello_world_keyword_args(first_person="Marcela", second_person="Laura")
hello_world_arbitrary_keyword_args(first_person="Vanessa", second_person="Jose")
hello_world_arbitrary_keyword_args(first_person="Vanessa")
