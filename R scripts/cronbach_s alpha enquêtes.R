#cronbach's alpha enquêtes
# selecteert de kolommen met likert schaal antwoorden
selected_columns <- c("begrip.voor","begrip.na", 
                      "Hoe.goed.denk.je.dat.je.in.programmeren.bent.")
subset_data <- samengevoegde_dataset[, selected_columns]

# Berekent Cronbach's Alpha
psych::alpha(subset_data)

