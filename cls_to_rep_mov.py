class Movie:
    def __init__(self,title,director,rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __repr__(self):
        return f"Title: {self.title} , Director: {self.director} , Rating = {self.rating}"
    
t1 = Movie(title = "Inception", director = "Christopher Nolan",rating = 8.8)
print(t1)