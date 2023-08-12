# Install and load the required libraries if not already installed
if (!requireNamespace("plotly", quietly = TRUE)) {
  install.packages("plotly")
}
library(plotly)

# Load your data (replace 'data.csv' with your actual file path)
data <- read.csv("test/test.txt", sep = "\t", header = TRUE)

# Create a directory to save the plots
if (!dir.exists("plots")) {
  dir.create("plots")
}

# Create a list to store trace objects for each column
traces <- list()

# Iterate through each column and create a trace for the combined plot
for (col in colnames(data)) {
  if (!all(is.na(data[[col]]))) {  # Skip columns with all NA values
    trace <- list(
      type = 'scatter',
      mode = 'lines',
      name = col,
      x = seq_along(data[[col]]),
      y = data[[col]]
    )
    traces[[col]] <- trace
  }
}

# Create the combined plot
combined_plot <- plot_ly()

# Add traces to the combined plot
for (trace in traces) {
  combined_plot <- add_trace(combined_plot, type = trace$type, mode = trace$mode, name = trace$name, x = trace$x, y = trace$y)
}

# Save the interactive HTML plot for the combined plot
html_file <- "combined_plot.html"
saveWidget(combined_plot, file = html_file)
cat("Saved combined plot:", html_file, "\n")
