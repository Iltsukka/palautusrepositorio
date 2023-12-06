from matchers import All, PlaysIn, HasAtLeast, And, HasFewerThan, Or

class Querybuilder:

    def __init__(self, query = None, queries = None):
        self.queries = []
        if queries is not None:
            self.queries = queries
        if query is not None:
            self.queries.append(query)
        

    def playsIn(self, team):
        return Querybuilder(PlaysIn(team), self.queries)
    
    def HasAtLeast(self, value, attribute):
        return Querybuilder(HasAtLeast(value, attribute), self.queries)
    def HasFewerThan(self, value, attribute):
        return Querybuilder(HasFewerThan(value, attribute), self.queries)
    
    def oneOf(self, *matchers):
        return Querybuilder(Or(*matchers), self.queries)


    def build(self):
        if not self.queries:
            return All()
        return And(*self.queries)


# class Querybuilder:

#     queries = []

#     def __init__(self, query = None):
        
#         if query is not None:
#             self.queries.append(query)
#             print(self.queries)
        

#     def playsIn(self, team):
#         return Querybuilder(PlaysIn(team))
    
#     def HasAtLeast(self, value, attribute):
#         return Querybuilder(HasAtLeast(value, attribute))
#     def HasFewerThan(self, value, attribute):
#         return Querybuilder(HasFewerThan(value, attribute))

#     def build(self):
#         if not self.queries:
#             return All()
#         print(self.queries)
#         return And(*self.queries)


