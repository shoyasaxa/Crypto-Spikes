# Examining the Relationship between Bitcoin Price and Google Trends Using Granger Causality and Deep Learning 

### Overview 

* This repository contains all the work I did for the McDonough Summer Research Fellowship, in which I explored the quantitative relationship  between bitcoin prices and Google Trends. You can read the academic paper and the one-page summary on my linkedin profile [here] (https://www.linkedin.com/in/shoya-yoshida/) 

Below is the abstract from my paper
* This research analyzes the relationship between Google Trends and bitcoin price with 
hourly data. The exploratory data analysis showed that Google Trends and bitcoin price 
correlate, and Google Trends sometimes seems like a leading indicator of price. To add statistical 
significance to this observation, I tested for Granger Causality and graphed impulse response 
functions between the two time series using Structural Vector Autoregression (SVAR). Results 
for some of the keywords showed that, theoretically, Google Trends cause price and can be used 
to predict price. To examine if this theoretical causal relationship is practical, I built a specific 
kind of Recurrent Neural Network (RNN) called the Long Short-Term Memory (LSTM) to 
model hourly price movements. Unfortunately, this model was not able to show that Google 
Trends can add significant predictive power in forecasting price movements.  

In this project, I 
  * used Pytrends to get hourly Google Trends
    * [get_data.py] (https://github.com/shoyasaxa/Crypto-Spikes/blob/master/get_data.py) 
  * preprocessed data and performed exploratory analysis  
    * [analyze_data.ipynb] (https://github.com/shoyasaxa/Crypto-Spikes/blob/master/analyze_data.ipynb)
      * innovatively scaled Google Trends (Google Trends scale data in a very unhelpful way. For more information, please look into my paper).
  * Ran Structural Vector Autoregression to test for Granger Causality and graph impulse response functions between bitcoin prices and Google Trends 
    * bottom of analyze_data.ipynb and [Granger Causality Tests] (https://github.com/shoyasaxa/Crypto-Spikes/blob/master/More%20Granger%20Causality%20Tests.ipynb) 
  * Built LSTM using Keras to predict price movement 
    * [Price Spike Classification with Keras and LSTM v3.ipynb] (https://github.com/shoyasaxa/Crypto-Spikes/blob/master/Price%20Spike%20Classification%20with%20Keras%20and%20LSTM%20v3.ipynb)
    
    
