nblivre = int(input())

lprev = 0
for i in range(nblivre):
    titre = input()
    if (len(titre) > lprev):
        print(titre)
        lprev = len(titre)