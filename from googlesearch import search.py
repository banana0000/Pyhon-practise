from googlesearch import search
results = search(term="Python", num_results=5, lang="en")
results = list(results)
print(results)
