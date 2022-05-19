install.packages("arules")
library("arules") # Used for building association rules i.e. apriori algorithm

# Importing the dataset
Retail <- read.csv(file.choose())
View(Retail)

retail <- Retail[complete.cases(Retail), ] # Cleans the non missing values
str(retail)

summary(retail)

# making rules using apriori algorithm 
# Keep changing support and confidence values to obtain different rules

# Building rules using apriori algorithm
rules <- apriori(retail, parameter = list(support = 0.002, confidence = 0.5, minlen = 5))
rules

# Viewing rules based on lift value
inspect(head(sort(rules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(rules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(rules)

plot(rules,method="two-key plot") # Two-key Plot
plot(rules, method = "grouped")
plot(rules[1:40], method = "graph") # for good visualization try plotting only few rules

write(rules, file = "Retail_rules.csv", sep = ",")

getwd()

