library(nnet)
library(mlogit)
# library(car)
# vif(fit)

df = read.csv("Scripts/logit_pm2_df_arr_original.csv")
head(df)

data = mlogit.data(df, shape = "wide", choice ="KEY_CODE")

head(data,13)
write.csv(data, "Scripts/mlogit_data.csv")
result = mlogit(KEY_CODE~0|diver+GURU.m2+shop.m2+distance2|0, data)

result = mlogit(KEY_CODE~0|diver+X+X.1+X.2|0,method = "nr", data)
# result = nnet::multinom(KEY_CODE ~ diver+X+X.1+X.2, data=data)
summary(result)
# , method = "bfgs"
# write.csv(result$coefficient, "result_coe_exp.csv")
# write.csv(result$fitted.values, "result_fit_exp.csv")
# write.csv(result$probabilities, "result_pro_exp.csv")