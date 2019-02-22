library(shiny)

CSVtitle<-read_csv("path/to/file/Ames.csv")
# Define UI for app that draws a histogram ----
ui <- fluidPage(
  
  # App title ----
  titlePanel("ComboBox With Data!"),
  sidebarLayout(
    sidebarPanel (
      selectInput("variable", "Variable:",
                  c("Cylinders" = "Neighborhood",
                    "Transmission" = "Condition",
                    "Gears" = "BldgType"),multiple = TRUE),
      tableOutput("data")
      ,width = 8),
    mainPanel ()
  )
)

# Define server logic required to draw a histogram ----

server = function(input, output) {
  output$data <- renderTable({

    CSVtitle[, c("LotArea", input$variable), drop = FALSE]
  }, rownames = TRUE)
}

# Create Shiny app ----
shinyApp(ui = ui, server = server)