f = open('../idwiki-latest-pages-articles.xml')
a = []
i = 0

while True:
    try:
        line = f.readline()
        if line == '':
            break
        a.append(line)
    except:
        continue
    i += 1
    if i % 100000 == 0:
        print(i, 'lines read')
        
f.close()

f = open('../idwiki-latest-pages-articles-full.xml', 'w')

i = 0

for line in a:
    f.write(line + '\n')
    i += 1
    if i % 100000 == 0:
        print(i, 'lines written')    

f.close()
