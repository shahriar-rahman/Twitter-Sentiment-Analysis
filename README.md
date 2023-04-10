# **Twitter-Sentiment-Analysis**
An automated windows application, capable of sifting through user's tweets to analyze the overall sentiment.


## **Abstract**
Nowadays, the social media sites such as Twitter have become popular for people sharing their opinions and feelings. However, words can be structured in a complex method which would make it near impossible to detect the true sentiment value behind a tweet. Moreover, there is a myriad of slangs and trendy phrases that are being used to further make the effort of sentiment analysis more complicated. The primary incentive of this application is to construct an automated AI system capable of sifting through large chunks of tweets and, using tokenization and text polarity detection systems, be able to detect a user's sentiment over a single tweet. Additionally, the system is being calibrated to also detect every single tweet and visualize the overall results as well as create a psychological profile that would be beneficial in many sectors such as mental therapy, automated crime detection, and a plethora of other medical professions.


## Background and Significance
The applications that use this Sentiment Analysis tool ranges from ecommerce, marketing, crime detection, to politics and any other research. Firstly, it is used in Ecommerce and marketing where it analyzes web and social media mentions about a product, a service, a marketing campaign or a brand. This is how companies can discover consumer attitudes towards them, their products, services, or marketing campaigns on discussion forums, review sites, Twitter, Instagram, Facebook and other publicly available sources. Many companies also use this system to collect and analyze customer feedback. Some time ago, UBER used social media monitoring and sentiment analysis tool to discover if users like the new version of their app. Sentiment analysis is also used in politics. In 2012, the Obama administration used sentiment analysis tools to analyze the reception of policy announcement during 2012 presidential election. During the last presidential election in the US, some organizations analyzed, for example, how many negative mentions about particular candidates appeared in the media and news reports. However, there are some challenges and difficulties to expect while analyzing tweets or any posts. Sometimes there may be words that are contradictory for example “The weather is bad, but the hike is good”, as this sentence contains both a positive and a negative reaction. Sometimes it is hard to conclude whether a word is actually a word or a name of a brand or movie. For example “Python”.  It is very difficult to assume the appropriate context, such as predicting whether it is a snake or a language.


## Motivation
With the increase in technology, there is so much potential to make the world a better place using technology. Artificial Intelligence (AI) has proved time and time again that it is required as its importance grows larger by the minute. There are changes in our lives because this technology is covering a wide range of sectors that affects our daily life. 


## Methods and Models
LoginCheck: It verifies and confirms usernames and passwords.
OpenTwitterWeb: This method allows the user to open the Twitter website when the twitter icon is clicked.
MainMenu: Opens the Menu UI.
AnalyzeSentenceAction: Begins analysis of a single sentence.
AnalysisViewTwitterHistory: This shows up all the posts or tweets made on twitter.
AnalyzeTwitterPosts: At first, this method fetches all the required information from the site. Then, perform tokenization, integrates all the values, and displays visual representations of the obtained results.
TwitterSearchMenu: The purpose of this method is to search user input and then it finds the related relevant information (tweets). It then shows all the information and plots a graph showing input data results.

![alt text](https://github.com/shahriar-rahman/Twitter-Sentiment-Analysis/blob/main/Block%20Diagram.PNG)

![alt text](https://github.com/shahriar-rahman/Twitter-Sentiment-Analysis/blob/main/Block%20Diagram.PNG)

## Conclusions
In this project, the primary focus is on the development of a system that is able to calculate the magnitude of human sentiment. Firstly, a clear and visually appealing UI is designed to ensure user convenience. Then all of the user’s tweets are then sifted. Afterward, the data is extracted from the Twitter site using a Twitter API which helps in constructing a system capable of processing every single tweet and analyzing the polarity value by performing syntactic word calculation. Lastly, it will show the overall sentiment of all the tweets and display it in a graphical representation.
