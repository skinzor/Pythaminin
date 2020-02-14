class BOOK(object):

    def __init__(self, title, author, pages):
        print("BOOK HAS BEEN CREATED!")

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s\nAuthor: %s\nPages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("BOOK IS DELETED")

book = BOOK('Python', 'uniminin', 199)
print(len(book))

del book
