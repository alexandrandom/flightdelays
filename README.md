# Flight Data Analysis Project
Ever waited on a delayed plane? Wondered when to travel to minimize the delay or flight cancelation risk?
I gathered flight data to build an algorithm that can give some insight into what flight routes and which days are the best to travel (more on-time departures and touchdowns) and which ones may be a somewhat less-safe-choice.

How does this work?
1. Flight data, as well as delay info, is scraped from a flight schedule website (not automated yet)
2. Airport and country data is requested from API
3. HTML parser goes through the data
4. Data is stored in dataframe, cleaned and merged with relevant ISO codes, country and city names
5. Data is aggregated accordingly
6. Plots relevant to the flight route chosen by the user are being generated

To be continued
