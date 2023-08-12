# Install and load necessary packages
if (!requireNamespace("tidyverse", quietly = TRUE)) {
  install.packages("tidyverse")
}

if (!requireNamespace("plotly", quietly = TRUE)) {
  install.packages("plotly")
}

library(tidyverse)
library(plotly)

# Read data
data <- read.delim("/test/test.txt", sep = "\t", header = TRUE)

# Reshape data for plotting
data_long <- data %>%
  pivot_longer(cols = everything(), names_to = "Column", values_to = "Value")

# Create interactive combined plot
combined_plot <- plot_ly(data_long, x = ~Column, y = ~Value, 
                         color = ~Column, type = "box", boxpoints = "all",
                         hoverinfo = "x+y+text",
                         text = ~paste("Value:", Value)) %>%
  layout(title = "Interactive Combined Plot", xaxis = list(title = "Columns"), yaxis = list(title = "Value"))

# Export interactive HTML plot
if (!requireNamespace("htmlwidgets", quietly = TRUE)) {
  install.packages("htmlwidgets")
}

library(htmlwidgets)
saveWidget(combined_plot, "interactive_combined_plot.html")
