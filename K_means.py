import matplotlib.pyplot as plt
import numpy as np
import random
from math import sqrt

#Fonction qui va attribuer les points de la liste Points au différents clusters de la liste Clusters
def attribution_cluster(Clusters, Points, Colors, Plot) :
    Distance=[]
    for k in range (len(Points)) :
            for l in range (len(Clusters)) :
                Distance.append(sqrt((Points[k][0] - Clusters[l][0])**2 + (Points[k][1] - Clusters[l][1])**2))
            Plot.plot(Points[k][0], Points[k][1], marker = "o", color = Colors[Distance.index(min(Distance))])
            Points[k][2] = Colors[Distance.index(min(Distance))]
            Distance.clear()

#Fonction qui va trouver les centres de masse des clusters composées des points de la liste Points 
def center_de_masse(Points, Colors) :
    Nouveau_Centres_de_Masse = []
    for couleur in Colors :
            center_masse_x, center_masse_y, compteur = 0, 0, 0
            for x in range (len(Points)) :
                if Points[x][2] == couleur :
                    compteur += 1
                    center_masse_x += Points[x][0]
            center_masse_x /= compteur
            compteur = 0
            for y in range (len(Points)) :
                if Points[y][2] == couleur :
                    compteur += 1
                    center_masse_y += Points[y][1]
            center_masse_y /= compteur
            Nouveau_Centres_de_Masse.append([center_masse_x, center_masse_y])
            plt.plot(center_masse_x, center_masse_y, markersize = 10, marker = "o", color = "black", zorder=1000)
    for point in range (len(Points)) :
            plt.plot(Points[point][0], Points[point][1], marker = "o", color = Points[point][2])
    return(Nouveau_Centres_de_Masse)

#Algorithme de clusterisation selon la méthode des K-moyennes avec un nombre de points et de clusters à définir
def k_mean(points, clusters, iteration) :
    hexa = "0123456789ABCDEF"
    Points=[]
    Clusters=[]
    Colors=[]
    Distance=[]
    if (points == 0 and clusters == 0) :
        print("Rien")
    elif (clusters == 0) :
        print("Il n'y a pas clusters pour regrouper les points")
    elif (points ==0) :
        print("Il n'y a pas de points à ajouter aux clusters")
    else :
        plt.rcParams.update({"figure.max_open_warning": 0})
        plt.axis([0, 1000, 0, 1000])
        for i in range(points) :
            x_point = random.randrange(0, 1000)
            y_point = random.randrange(0, 1000)
            Points.append([x_point, y_point, "black"])
            plt.plot(x_point, y_point, "ko")
        for i in range(clusters) : 
            color = "#"
            for j in range(6) :
                color = color + hexa[random.randint(0,15)]
            Colors.append(color)
            x_cluster = random.randrange(0, 1000)
            y_cluster = random.randrange(0, 1000)
            Clusters.append([x_cluster, y_cluster, color])
            plt.plot(x_cluster, y_cluster, marker = "o" ,color = color)
        plt.figure()
        for k in range (len(Points)) :
            for l in range (len(Clusters)) :
                Distance.append(sqrt((Points[k][0] - Clusters[l][0])**2 + (Points[k][1] - Clusters[l][1])**2))
            plt.plot(Points[k][0], Points[k][1], marker = "o", color = Colors[Distance.index(min(Distance))])
            Points[k][2] = Colors[Distance.index(min(Distance))]
            Distance.clear()
        plt.figure()
        Nouveau_Centres_de_Masse = []
        for couleur in Colors :
            center_masse_x, center_masse_y, compteur = 0, 0, 0
            for x in range (points) :
                if Points[x][2] == couleur :
                    compteur += 1
                    center_masse_x += Points[x][0]
            center_masse_x /= compteur
            compteur = 0
            for y in range (points) :
                if Points[y][2] == couleur :
                    compteur += 1
                    center_masse_y += Points[y][1]
            center_masse_y /= compteur
            Nouveau_Centres_de_Masse.append([center_masse_x, center_masse_y])
            plt.plot(center_masse_x, center_masse_y, markersize = 10, marker = "o", color = "black", zorder=1000)
        for point in range (len(Points)) :
            plt.plot(Points[point][0], Points[point][1], marker = "o", color = Points[point][2])
        plt.figure()
        attribution_cluster(Nouveau_Centres_de_Masse, Points, Colors, plt)
        plt.figure()
        for i in range(iteration) :
            print(i)
            Centre = center_de_masse(Points, Colors)
            attribution_cluster(Centre, Points, Colors, plt)
            plt.figure()
        plt.show()
k_mean(3000, 5, 4)