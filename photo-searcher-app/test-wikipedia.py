import wikipedia

page = wikipedia.page("beach", auto_suggest=False)
print(len(page.images))
print(page.images[0])
