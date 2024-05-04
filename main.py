bad_words = ["дурак", "лрлрлрлрлр"]


class Post:
    def __init__(self, name: str, date: str, likes: list, text: str, comments: list):
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

    def writeComment(self, user: str, text: str):
        for item in self.comments:
            for name in item:
                if name == user:
                    item[name].append(text)
        return self.comments


post1 = Post("oleg", "20.04.88", ["user"], "Ты дурак, лрлрлрлрлр",
             [{"name1": ["коммент1", "коммент2"]}, {"name2": ["комент1", "коммент2"]}])
print(post1.like("user"))
print(post1.writeComment("name1", "коммент3"))
