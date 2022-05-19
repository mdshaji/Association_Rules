install.packages("arules")
library("arules") # Used for building association rules i.e. apriori algorithm

# Importing the dataset
Phone <- read.csv(file.choose())
View(Phone)

summary(Phone)

# making rules using apriori algorithm 
# Keep changing support and confidence values to obtain different rules

# Building rules using apriori algorithm
rules <- apriori(as.matrix(Phone[,4:9],parameter=list(support=0.002, confidence = 0.75,minlen=2)))
rules

# Viewing rules based on lift value
inspect(head(sort(rules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(rules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules

plot(rules,method="two-key plot") # Two-key Plot

plot(rules[1:1], method = "graph") # for good visualization try plotting only few rules

write(rules, file = "Phone_rules.csv", sep = ",")

getwd()

