bad_words = ["дурак", "лрлрлрлрлр"]


class Post:
    def __init__(self, name: str, date: str, likes: list, text: str, comments: dict):
        self.name = name
        self.date = date
        self.likes = likes
        self.text = text
        self.comments = comments
        for badWord in bad_words:
            gratings = "#" * len(badWord)
            self.text = self.text.replace(badWord, gratings)

    def like(self, name: str):
        if name not in self.likes:
            self.likes.append(name)
        else:
            self.likes.remove(name)
        return len(self.likes)

    def writeaComment(self, name: str, text: str):
        self.comments[name] = text


#TODO: сделать список словарей со списками в comments. Типа [ {name1:["комент1", "коммент2"]}, {name2:["комент1", "коммент2"]} ]

post1 = Post("oleg", "20.04.88", ["user"], "Ты дурак, лрлрлрлрлр", {"user": "cогл"})
print(post1.like("user"))
print(post1.text)
