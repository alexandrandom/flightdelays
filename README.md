# Flight Data Analysis Project
Ever waited on a delayed plane? Wondered when to travel to minimize the delay or flight cancelation risk?
I gathered PLL LOT flight data to build an algorithm that can give some insight into what flight routes and which days are the best to travel (more on-time departures and touchdowns) and which ones may be a somewhat less-safe-choice.

All the files have yet to be tidied up to properly work in here, but overall...
How does this work?
1. Flight data, as well as delay info, is scraped from a flight schedule website (not automated yet - hard to do so, because the site from which the data is being scraped is throwing 500, even with proper params in request - browser etc.). This step could be obviously omitted if I had full API access, but that's not easy being a student!
2. Airport and country data is requested from API (for this step basic access is enough)
3. HTML parser goes through the scraped data
4. Scraped data is stored in dataframe, cleaned and merged with relevant ISO codes, country and city names (API data)
5. Data is aggregated accordingly, saved to .csv - the two output files are here: https://drive.google.com/drive/folders/1qnlN3zR0M8SolQV4hasTwRMgCzTs7Kfn?usp=sharing  (I'll think about putting it in parquet file instead)
6. Plots relevant to the flight route chosen by the user are being generated (skrypcik.py)

One of the files also shows differences between the search popularity and factual count of domestic and international flights in the flight schedule.
