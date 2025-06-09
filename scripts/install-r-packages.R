packages <- c(
  "tidyverse", "gganimate", "ggraph", "leaflet", "janitor", "tidylog",
  "pdftools", "readxl", "tidytext", "httr", "glmnet", "reticulate",
  "rpart.plot", "GGally", "vip", "skimr", "widyr", "stringr",
  "rgdal", "rgeos", "htmlwidgets", "htmltools", "hunspell", "lubridate",
  "scales", "gridExtra", "keras", "igraph", "sunburstR"
)
install.packages(setdiff(packages, installed.packages()[,"Package"]), repos = "https://cloud.r-project.org")