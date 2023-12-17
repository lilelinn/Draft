# t-test voor tijd
library("gmodels")
library("car")
library("ggplot2")
library("qqplotr")
library("dplyr")


#Assumptie 2:
ggplot(samengevoegde_dataset, aes(x = methode, y = tijd, fill = methode)) +
  stat_boxplot(geom = "errorbar", width = 0.5) +
  geom_boxplot() +  
  stat_summary(fun.y = mean, geom = "point", shape = 10, size = 3.5, color = "black") + 
  ggtitle("Boxplots van tijd voor de methodes Boek en Codeium") + 
  theme_bw() + theme(legend.position = "none")

# Assumptie 3:
samengevoegde_dataset %>%
  group_by(methode) %>%
  summarise(`W Statistic` = shapiro.test(tijd)$statistic,
            `p-value` = shapiro.test(tijd)$p.value)

#qqplot voor Boek
qqnorm(subset_Boek$tijd)
qqline(subset_Boek$tijd)
mtext("QQ Plot - Methode Boek voor tijd", side = 3, line = 0.5)

#qqplot voor Codeium
qqnorm(subset_Codeium$tijd)
qqline(subset_Codeium$tijd)
mtext("QQ Plot - Methode Codeium voor tijd", side = 3, line = 0.5)

# Assumptie 4:
lev1<-leveneTest(tijd ~ methode, data=samengevoegde_dataset, center="mean")
lev2<-leveneTest(tijd ~ methode, data=samengevoegde_dataset, center="median")
print(lev1)
print(lev2)

# t-test

t.test(tijd ~ methode, data=samengevoegde_dataset, var.equal=TRUE, na.rm=TRUE, alternative="greater")

