# Modify this function to return a list of strings as defined above
def list_benefits():
    benefits = ["More organized code", "More readable code", "Easier code reuse",
                "Allowing programmers to share and connect code together"]
    return benefits


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()


# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kwargs):
    return True if kwargs.get('magicnumber') == 7 else False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
