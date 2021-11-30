getwd()

dbtxt <- read.table("http://www.sthda.com/upload/boxplot_format.txt");

dbtxt.2 <- read.table("/home/lekillergallet/Downloads/BASETXT.txt", sep = ","); dbtxt.2

View(dbtxt.2);

library("readr")

dbcsv <- read_csv("/home/lekillergallet/Downloads/TOTALSACSV.csv");

View(dbcsv)

library("readxl")

dbxl<- read_excel("/home/lekillergallet/Downloads/TOTALSA.xls"); dbxl

View(dbxl)

library(foreign)

ceosal1 <- read.dta("http://fmwww.bc.edu/ec-p/data/wooldridge/ceosal1.dta")
dim(ceosal1)
View(ceosal1)

mean(ceosal1$salary)     
median(ceosal1$salary)   
var(ceosal1$salary)      
sd(ceosal1$salary)       
