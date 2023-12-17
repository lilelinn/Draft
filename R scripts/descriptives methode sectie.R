#descriptives methode sectie

install.packages("readODS")
library(readODS)

# inladen van de twee excel sheets
Beoordelingen <- read_ods("C:/Users/verka/Desktop/Onderzoek van interactieve systemen/groepsproject/Beoordelingen.ods")
Resultaten <- read_ods("C:/Users/verka/Desktop/Onderzoek van interactieve systemen/groepsproject/Resultaten.ods")

# Joinen op de kolom 'Naam'
samengevoegde_dataset <- merge(Beoordelingen, Resultaten, by = 'Naam', all.x = TRUE)

# subsets maken van de twee condities
subset_Boek <- samengevoegde_dataset[samengevoegde_dataset$methode == 'Boek', ]
subset_Codeium <- samengevoegde_dataset[samengevoegde_dataset$methode == 'Codeium', ]

#totale man-vrouwverdeling
table(samengevoegde_dataset$Geslacht)

#man-vrouw verdeling Boek
table(subset_Boek$Geslacht)

#man-vrouwverdeling Codeium
table(subset_Codeium$Geslacht)

#pie chart man-vrouwverdeling Boek
categorieen_boek <- table(subset_Boek$Geslacht)# Tabel maken van frequenties
lbls <- c("Man", "Vrouw")
percentages_boek <- prop.table(categorieen_boek) * 100  # Percentage berekenen

# Kleuren voor de cirkeldiagramsectoren
kleuren <- c("lightblue", "lightpink")

# Maak het cirkeldiagram met percentages en legenda
pie(percentages_boek, labels = paste(lbls, " (", round(percentages_boek, 1), "%)"), 
    col = kleuren, main = "Man-vrouwverdeling categorie Boek")


#pie chart man-vrouwverdeling Codeium
categorieen_codeium <- table(subset_Codeium$Geslacht)# Tabel maken van frequenties
lbls <- c("Man", "Vrouw")
percentages_codeium <- prop.table(categorieen_codeium) * 100  # Percentage berekenen

# Kleuren voor de cirkeldiagramsectoren
kleuren <- c("lightblue", "lightpink")

# Maak het cirkeldiagram met percentages en legenda
pie(percentages_codeium, labels = paste(lbls, " (", round(percentages_codeium, 1), "%)"), 
    col = kleuren, main = "Man-vrouwverdeling categorie Codeium")

#gemiddelde leeftijd per conditie en totaal
mean(samengevoegde_dataset$Leeftijd)
mean(subset_Boek$Leeftijd)
mean(subset_Codeium$Leeftijd)

#staafdiagram leeftijdsverdeling 
leeftijd <- table(samengevoegde_dataset$Leeftijd)
barplot(leeftijd, main="leeftijdsverdeling totaal",
        xlab="Leeftijd", ylab="Aantal", col='lightblue')

#staafdiagram leeftijdsverdeling Boek
leeftijd_boek <- table(subset_Boek$Leeftijd)
barplot(leeftijd_boek, main="leeftijdsverdeling categorie Boek",
        xlab="Leeftijd", ylab="Aantal", col='lightblue')

#staafdiagram leeftijdsverdeling Codeium
leeftijd_codeium <- table(subset_Codeium$Leeftijd)
barplot(leeftijd_codeium, main="leeftijdsverdeling categorie Codeium",
        xlab="Leeftijd", ylab="Aantal", col='lightblue')

#gemiddelde niveauscore per conditie en totaal
mean(samengevoegde_dataset$Niveauscore)
mean(subset_Boek$Niveauscore)
mean(subset_Codeium$Niveauscore)

#verdeling tweede derde jaars per conditie en totaal
table(samengevoegde_dataset$Studiejaar)
(table(samengevoegde_dataset$Studiejaar) / 
    sum(table(samengevoegde_dataset$Studiejaar))) * 100

table(subset_Boek$Studiejaar)
(table(subset_Boek$Studiejaar) / 
    sum(table(subset_Boek$Studiejaar))) * 100

table(subset_Codeium$Studiejaar)
(table(subset_Codeium$Studiejaar) / 
    sum(table(subset_Codeium$Studiejaar))) * 100


#staafdiagram studiejaar Boek
studiejaar_boek <- table(subset_Boek$Studiejaar)
barplot(studiejaar_boek, main="Studiejaarverdeling categorie Boek",
        xlab="Studiejaar", ylab='Aantal', col='lightblue')

#staafdiagram studiejaar Codeium
studiejaar_codeium <- table(subset_Codeium$Studiejaar)
barplot(studiejaar_codeium, main="Studiejaarverdeling categorie Codeium",
        xlab="Studiejaar", ylab='Aantal',col='lightblue')


#Niveauverdeling Boek
niveau_boek <- table(subset_Boek$Niveau)
barplot(niveau_boek, main="Niveauverdeling categorie Boek",
        xlab="Niveau", ylab='Aantal',col='lightblue')

#Niveauverdeling Boek
niveau_codeium <- table(subset_Codeium$Niveau)
barplot(niveau_codeium, main="Niveauverdeling categorie Codeium",
        xlab="Niveau", ylab='Aantal',col='lightblue')

