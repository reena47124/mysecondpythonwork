#oops in python.
#create a movie class with a rating method.
class Movie:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating

    def fun_rating(self):
        if self.rating>=8:
            print(f"{self.name} is excellent movie.")
        elif self.rating>=5:
            print(f"{self.name} is average movie.")
        else:
            print(f"{self.name} is poor movie.")

m1=Movie("kkhh",9)
m2=Movie("tiger",7)
m3=Movie("queen",9)
m1.fun_rating()
m2.fun_rating()
m3.fun_rating()
