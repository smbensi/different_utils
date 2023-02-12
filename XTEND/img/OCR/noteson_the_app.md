# Streaming

1. j'ai essaye de jouer sur le parametre de `cv2`  CAP_PROP_BUFFERSIZE pour eviter de garder un **buffer** et quand on pause le stream de reprendre le stream au frame de l'instant et pas reprendre la ou on a fait la pause. \
Cependant , cela semble pas stable **A APPROFONDIR**

2. Du coup on recommence le stream a chaque fois que l'on recommence une recherche de carte mais cela peut presenter 2 problemes:
    * rajoute 4k de memoires dans le docker a chaque fois qu'on recommence le stream
    * parfois ne choque pas directement le stream surement parce quil met du temps a trouver un **keyframe** voir si on peut pas jouer sur le stream lui-meme (allez voir how video works)

3. important de noter qu'on a pas de problemes quand on se connecte directement a la camera on peut mettre en pause le stream et revenir sans problemes

# APPLICATION

# Bugs

1. encore problemes avec les espaces
2. Californie : confusions entre DOB et license_number
3. Inversions prenom, nom de famille
4. Attention  quand il ya d'autres textes dans l'image

# Ameliorations possibles

1. faire des batch
2. eviter les frames flous
3. trouver les meileurs facons d'afficher les cartes 