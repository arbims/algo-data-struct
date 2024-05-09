nblivre = int(input())
lmin = int(input())

for i in range(nblivre):
  titre = input()
  description = input()
  if (len(description) < lmin):
    print(titre)
