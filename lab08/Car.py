class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
                    else:
                        return False
                else:
                    if self.year > rhs.year:
                        return True
                    else:
                        return False
            else:
                if self.model > rhs.model:
                    return True
                else:
                    return False
        else:
            if self.make > rhs.make:
                return True
            else:
                return False

    def __lt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
                    else:
                        return False
                else:
                    if self.year < rhs.year:
                        return True
                    else:
                        return False
            else:
                if self.model < rhs.model:
                    return True
                else:
                    return False
        else:
            if self.make < rhs.make:
                return True
            else:
                return False

    def __eq__(self, rhs):
        if rhs == None:
            return False
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}'



    
