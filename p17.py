import inflect
p = inflect.engine()
print(sum([len(p.number_to_words(i, andword="and").replace(' ','').replace('-','')) for i in range(1,1001)]))