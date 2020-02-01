# am

df = read.csv("Scripts/contents_am.csv")
df_scale = scale(df)
data = df
data_scale	<-	data.frame(df_scale)

dim(df)
head(df_scale)

am<-lm(people_count.m2~guru_m2+shop.m2+day_amuse.m2+culture.m2+diver,data=data_scale)
summary(am)$coefficients
write.csv(summary(am)$coefficients, "lm_coe_am.csv")

# pm1

df = read.csv("Scripts/contents_pm1.csv")
df_scale = scale(df)
data = df
data_scale	<-	data.frame(df_scale)

dim(df)
head(df_scale)

pm1<-lm(people_count.m2~guru_m2+shop.m2+day_amuse.m2+culture.m2+diver,data=data_scale)
summary(pm1)$coefficients
write.csv(summary(pm1)$coefficients, "lm_coe_pm1.csv")


# pm2

df = read.csv("Scripts/contents_pm2.csv")
df_scale = scale(df)
data = df
data_scale	<-	data.frame(df_scale)

dim(df)
head(df_scale)

pm2<-lm(people_count.m2~guru_m2+shop.m2+night_amuse.m2+culture.m2+diver,data=data_scale)
summary(pm2)$coefficients
write.csv(summary(pm2)$coefficients, "lm_coe_pm2.csv")