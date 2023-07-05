# Tableau Story ~ [Flight Journey: Unveiling the 2001 Aviation Landscape in the US](https://public.tableau.com/shared/FXGM3DP2Z?:display_count=n&:origin=viz_share_link).

##### Description: Explore the dynamic world of aviation in 2001. Analyze flight patterns, cancellations, and the profound impact of 9/11. Uncover monthly trends, busy airports, and the evolving landscape of air travel in the US.

## Pages:

- #### 1st Page

  **Caption**: This page presents an overview of the airline data for the year 2001. It includes the total number of actual flights, providing a sense of the volume of air traffic during that period. The visualization also highlights the count of cancelled flights, shedding light on the impact of various factors on flight cancellations. Additionally, the average flights per month are showcased, allowing us to understand seasonal variations and trends in air travel while considering the impact of cancellations.


  - Total number of actual flights.
  - Total Cancelled Flights.
  - Average Flights per Month. The data is filtered on Cancelled and Date Month. The Cancelled filter includes values less than or equal to 0. The Date Month filter excludes September, October, November and December.
  - Average Flights per Month. The data is filtered on Cancelled and Date Month. The Cancelled filter includes values less than or equal to 0. The Date Month filter keeps September, October, November and December.
  - Table ~ Count of flightscleaned_data.cs broken down by Unique Carrier.
- #### 2nd Page

  **Caption**: The map visualization on this page depicts the geographic distribution of US airports, including Puerto Rico and the Virgin Islands. By using average longitude and latitude coordinates, it visualizes the concentration of airports across different regions, with color coding indicating the states where these airports are located. Another map visualization shows the same distribution but adds bubble sizes to represent the count of flights originating from each airport, giving us insights into busier airports and their relative importance in terms of air traffic.


  - Map based on average of Longitude and average of Latitude.  Color shows details about State. Shows each US airport including puerto rico and virgin islands. Based on Flight count.
  - Map based on average of Longitude and average of Latitude.  Color shows details about State.  Size of bubble shows count of flights.  Shows each US airport including puerto rico and virgin islands. Based on Flight count.
- #### 3rd Page

  **Caption**: This page features bar graphs that provide insights into the timing of flights. One graph shows the count of flights for each hour of arrival time, highlighting peak and off-peak hours. Another graph focuses on the count of flights for each hour of departure time, enabling us to understand departure patterns and identify the busiest hours of air travel.


  - Bar Graph ~ Count of flights for each Arrival Time Hour. The view is filtered on Arrival Time Hour, which excludes Null.
  - Bar Graph ~ Count of flights for each Departure Time Hour. The view is filtered on Departure Time Hour, which excludes Null.
- #### 4th Page

  **Caption**: The area chart on this page illustrates the count of flights for each month, allowing us to identify overall trends and patterns in air travel throughout the year. Another area chart adds color coding to represent cancelled flights, enabling us to analyze the impact of cancellations on the monthly count and identify potential correlations between cancellations and specific months.


  - Area Chart ~ Count of flights for each Date Month.
  - Area Chart ~ Count of flights for each Date Month.  Color shows details about Cancelled.
- #### 5th Page

  **Caption**: This page showcases line charts that capture the trend of flight counts for each month. One chart focuses on cancelled flights, providing insights into the impact of cancellations on overall air traffic patterns. The other chart examines actual flights that were not cancelled, giving us a deeper understanding of air travel demand and any variations compared to the cancelled flights.


  - Line Chart ~ The trend of count of flights for Date Month. The data is filtered on Cancelled, only includes cancelled flights.
  - Line Chart ~ The trend of count of flights for Date Month. The data is filtered on Cancelled, only includes actual flights.
- #### 6th Page

  **Caption**: The stacked bar chart displayed here presents the count of flights for each day of the week. The color coding distinguishes cancelled flights, enabling us to identify any significant variations and patterns in flight counts by day. It offers insights into weekly trends and provides an opportunity to observe the impact of cancellations on specific days. Additionally, this page discusses the profound effect of the 9/11 tragedy on air travel, highlighting the significant increase in flight cancellations.


  - Stacked Bar Chart ~ Count of flights for each Date Day.  Color shows details about Cancelled. The data is filtered on Date Month, which keeps September. Shows the effect 9/11 tragedy best.
