data <- read.csv("/app/output/motif_counts_local.csv")

# יצירת גרף ושמירתו כקובץ PNG
png("/app/output/r_motif_plot.png")
barplot(data$Count, names.arg=data$Sequence, col="red", 
        main="R Container Analysis", ylab="Motif Count")
dev.off()
print("R Plot generated successfully.")
