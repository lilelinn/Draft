install.packages("gmodels")
install.packages("car")
install.packages("ggplot2")
install.packages("qqplotr")
install.packages("dplyr")

library("gmodels")
library("car")
library("ggplot2")
library("qqplotr")
library("dplyr")



# Assumptie 2:
ggplot(samengevoegde_dataset, aes(x = methode, y = beoordeling.begrip, fill = methode)) +
  stat_boxplot(geom ="errorbar", width = 0.5) +
  geom_boxplot() + 
  stat_summary(fun.y=mean, geom="point", shape=10, size=3.5, color="black") + 
  ggtitle("Boxplots van begrip voor de methodes Boek en Codeium") + 
  theme_bw() + theme(legend.position="none")

# Assumptie 3:
samengevoegde_dataset %>%
  group_by(methode) %>%
  summarise(`W Statistic` = shapiro.test(beoordeling.begrip)$statistic,
            `p-value` = shapiro.test(beoordeling.begrip)$p.value)

#qqplot voor Boek
qqnorm(subset_Boek$beoordeling.begrip)
qqline(subset_Boek$beoordeling.begrip)
mtext("QQ Plot - Methode Boek voor begrip", side = 3, line = 0.5)


#qqplot voor Codeium
qqnorm(subset_Codeium$beoordeling.begrip)
qqline(subset_Codeium$beoordeling.begrip)
mtext("QQ Plot - Methode Codeium voor begrip", side = 3, line = 0.5)

# Assumptie 4:
lev1<-leveneTest(beoordeling.begrip ~ methode, data=samengevoegde_dataset, center="mean")
lev2<-leveneTest(beoordeling.begrip ~ methode, data=samengevoegde_dataset, center="median")
print(lev1)
print(lev2)

# t-test

t.test(beoordeling.begrip ~ methode, data=samengevoegde_dataset, var.equal=TRUE, na.rm=TRUE, alternative = 'less')

