if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("ComplexHeatmap")
n
library(ComplexHeatmap)
set.seed(123)
nr1 = 4; nr2 = 8; nr3 = 6; nr = nr1 + nr2 + nr3
nc1 = 6; nc2 = 8; nc3 = 10; nc = nc1 + nc2 + nc3
mat = cbind(rbind(matrix(rnorm(nr1*nc1, mean = 1,   sd = 0.5), nr = nr1),
                  matrix(rnorm(nr2*nc1, mean = 0,   sd = 0.5), nr = nr2),
                  matrix(rnorm(nr3*nc1, mean = 0,   sd = 0.5), nr = nr3)),
            rbind(matrix(rnorm(nr1*nc2, mean = 0,   sd = 0.5), nr = nr1),
                  matrix(rnorm(nr2*nc2, mean = 1,   sd = 0.5), nr = nr2),
                  matrix(rnorm(nr3*nc2, mean = 0,   sd = 0.5), nr = nr3)),
            rbind(matrix(rnorm(nr1*nc3, mean = 0.5, sd = 0.5), nr = nr1),
                  matrix(rnorm(nr2*nc3, mean = 0.5, sd = 0.5), nr = nr2),
                  matrix(rnorm(nr3*nc3, mean = 1,   sd = 0.5), nr = nr3))
)
mat = mat[sample(nr, nr), sample(nc, nc)] # random shuffle rows and columns
rownames(mat) = paste0("row", seq_len(nr))
colnames(mat) = paste0("column", seq_len(nc))
mat
Heatmap(mat)
Heatmap(mat2)
mat
getwd()
setwd("C:/Users/shiva/Documents/Task/heatmap/")
mat1 <- read.csv("H-count_T0.csv",sep="\t",header = TRUE)
mat1
Heatmap(mat2)
mat2 <- mat1[,2:6]
mat2
rownames(mat2) <- paste0("S",seq(1,16))
rownames(mat2) <- c("AA","AB","AC","AD","AE","AF","AQ","AW","AZ","AS","AL","AAA","AAB","AKA","ALA","AIK")
rownames(mat2) <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
rownames(mat2) <- mat1[1]
rownames(mat2)
mat1[1]

mat3 <- read.csv("/Users/apple/Downloads/heatmap/H-count_T18-2.csv",sep="\t",header = TRUE)
mat4 <- mat3[,2:5]
mat4
Heatmap(mat4)
rownames(mat3)
