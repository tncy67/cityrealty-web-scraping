##  cityrealty web scraping and analysis of apartment rental market in NYC
 NYC rental price determinants by intrinsic factors - part 2
 
 ##### this is continuation of https://github.com/ted2020/determining-the-NYC-rental-prices...
 ##### part 1 was focused on extrinsic factors in determining the rental price.
 ##### part 2 is focused on intrinsic factors in determining the rental price.
 ##### part 3 will be focused on personal factors in determining the rental price.
 
 
 #### Hypothesis: 
 ####### Ho: number of bedrooms and bathrooms, square footage, doorman, furnished, etc. have no impact on rental prices in NYC.
 ####### Ha: number of bedrooms and bathrooms, square footage, doorman, furnished, etc. have an impact on rental prices in NY
 
 
 #### Data:
 ###### Scraped variables: price, square footage, building type, address, city, longitude and latitude, bedrooms, bathrooms, furnished, doorman, amenities, date.
 ###### Rental apartments data >> by Oct 25th 2019 >> 2500 observations
 ###### Apartments on sale data >> by Oct 25th 2019 >> 2500 observations
 ###### Apartments sold >> from Oct 2018 to Oct 2019 >> 15000 observations

 #### Literature:
 ###### Determining Apartment Rent: The Value of Amenities, Services, and External Factors by Sirmans, Stacy G., et al. 
 ###### “Determinants of Rental Value for Residential Properties: A Land Owner’s Perspective for Boarding Homes." by Nishan 
 ###### "Social Factors Affecting Landlords in the Determination of Rent." by Gilderbloom, John I. 


 #### OLS assumptions checked:
 ###### Homoskedasticity / Heteroskedasticity / Autocorrelation
 ###### Multicollinearity
 ###### Normality of residuals
 ###### Independent errors
 ###### Random sampling
 ###### linear in parameters
 
 
 #### extrinsic factors: 
 ###### Crime Rate
 ###### Median Income
 ###### Population
 ###### Employment
 ###### Poverty rate
 ###### Racial Diversity
 ###### Income Diversity
 ###### Rental Vacancy rate
 ###### Education
 ###### Closeness to a park 
 ###### Closeness to a subway station
 ###### New residential permits
 ###### Public & Subsidized Housing
 ###### Housing Units
 ###### College nearby
 ###### Tourist Attractions
 
 
 
 #### intrinsic factors: 
 ###### Age of building
 ###### Square footage
 ###### Number of bedrooms
 ###### Number of bathrooms
 ###### Kitchen size & quality
 ###### w/ or w/o a garage
 ###### Street parking permit
 ###### Frontyard / Backyard
 ###### Washer/Dryer
 ###### Pool
 ###### Fitness
 ###### Doorman
 ###### Furnished
 ###### Building Type


 #### personal  factors: 
 ###### Single/Married
 ###### Have kids
 ###### Education level
 ###### Age
 ###### Disabled
 ###### Smoke
 ###### Race
 ###### Personal Income
 ###### Own a pet
 ###### Where born

