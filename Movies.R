install.packages("arules")
library("arules") # Used for building association rules i.e. apriori algorithm

# Importing the dataset
Movies <- read.csv(file.choose())
View(Movies)

summary(Movies)

# making rules using apriori algorithm 
# Keep changing support and confidence values to obtain different rules

# Building rules using apriori algorithm
rules <- apriori(as.matrix(Movies[,6:15],parameter=list(support=0.02, confidence = 0.5,minlen=5)))
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
plot(rules[1:10], method = "graph") # for good visualization try plotting only few rules

write(rules, file = "Movies_rules.csv", sep = ",")

getwd()

