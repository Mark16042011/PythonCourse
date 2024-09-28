from PostSchemas import PostSchema, Comment

bad_words = ["дурак", "лрлрлрлрлр"]


class Post:
    def __init__(self, post: PostSchema):
        self.user = post.user
        self.date = post.date
        self.likes = post.likes
        self.text = post.text
        self.comments = post.comments
        for badWord in bad_words:
            gratings = "#" * len(badWord)
            self.text = self.text.replace(badWord, gratings)

    def like(self, name: str):
        if name not in self.likes:
            self.likes.append(name)
        else:
            self.likes.remove(name)
        return len(self.likes)

    def writeComment(self, comment: Comment):
        for item in self.comments:
            for name in item:
                if name == comment.user:
                    item[name].append(comment.text)
        return self.comments


post1 = Post(PostSchema(user="oleg",
                        date="20.04.88",
                        likes=["user"],
                        text="Ты дурак, лрлрлрлрлр",
                        comments=[{"name1": ["коммент1", "коммент2"]}, {"name2": ["комент1", "коммент2"]}]))
print(post1.like("user"))
print(post1.writeComment(Comment(user='user1',
                                 content='213')))
