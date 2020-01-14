library(nnet)
library(mlogit)
library(car)
library(ResourceSelection)
library(nnet)
library(epiDisplay)
library(caret)


df = read.csv("Scripts/logit_pm2_df_22.csv")
head(df)

round(cor(df),3)

write.csv(round(cor(df),3), "cor_exp.csv")

data = mlogit.data(df, shape = "long", choice ="Go", alt.levels = c("diver", "guru", "shop", "night", "cul"))

head(data,13)

# fit = glm(Go ~ diver+GURU.m2+shop.m2+night_amuse.m2+culture.m2+distance2, data=data, family=binomial)
# vif(fit)
# hoslem.test(fit$y, fitted(fit))
# summary(fit)

# logistic.display(fit, simplified=TRUE)

fit = glm(Go ~ diver+GURU.m2+culture.m2+distance2, data=data, family=binomial)
vif(fit)
write.csv(vif(fit), "vif_exp.csv")
hoslem.test(fit$y, fitted(fit))
write.csv(hoslem.test(fit$y, fitted(fit)), "ht_exp.csv")
summary(fit)
write.csv(summary(fit)$coefficient, "coe_exp.csv")

trainIndex <- createDataPartition(data, p = .67,
                                  list = FALSE,
                                  times = 1)

Train <- data[ trainIndex,]
Test  <- data[-trainIndex,]

Test$model_prob <- predict(model, Test, type = "response")

write.csv(fitted(fit), "fit.csv")

or = logistic.display(fit, simplified=TRUE)
# write.csv(or, "or_exp.csv")
sum(fit$y-data$Go)