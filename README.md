# AWS Assisted Pipline for A Recommondation System

### Yunrui Bao

## Problem Description: 
The shift towards digital marketplaces has transformed consumer behavior, offering the convenience of shopping from the comfort of home. Yet, this transformation has also introduced a challenge: information overload. To mitigate this, recommender systems have emerged as crucial tools that filter through the abundance of choices to deliver personalized product suggestions aligned with individual preferences, enhancing user experience and potentially increasing company revenues. For instance, McKinsey reports highlight that up to 35% of Amazon purchases and 75% of content viewed on Netflix are driven by these recommendation algorithms.  

In collaboration with "Encore," a pioneering startup launching a novel second-hand marketplace tailored to the digital-native younger generation through short video auctions, I aim to design a recommendation system that best suits users on this platform. Unlike traditional platforms such as eBay, which predominantly attracts users aged between 35-64, Encore focuses on capturing the untapped market of young millennials and Gen Z. These demographics demonstrate a burgeoning interest in vintage fashion—a trend that promises a solid and less saturated market opportunity for innovative platforms like Encore.  

The core objective of this project is to develop a robust AWS pipeline capable of managing over 100,000 daily users while delivering appropriate recommendations. This pipeline will leverage AWS services for large-scale data processing, ensuring users receive timely and relevant product suggestions. Designed for scalability and efficiency, it aims to support the rapid growth of Encore and maintain the flexibility required to adapt to an evolving market. The ultimate goal of my recommendation system is to enhance the user experience on Encore and attract an increasing number of new users to the platform. Currently, the project's focus is on establishing an automated pipeline rather than refining the recommendation system itself, because our dataset is not yet large enough to train sophisticated models. Initially, I have implemented heuristic popularity models and collaborative filtering methods. As we collect more data, I plan to further develop and enhance the recommendation engine as part of my professional thesis next year.

## Social Science Implication: 
This project addresses the social science research problem of understanding consumer behavior in digital environments. By analyzing large datasets of user interactions and item information, the recommendation algorithm can reveal patterns and preferences that are not immediately apparent, providing insights into consumer decision-making processes. This aligns with computational social science by combining data science with behavioral analysis to better understand and predict user actions.

## Solution: 

- Overview of the pipline: 
- ![pipleline](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/pipeline.jpg)
Currently, we only have 1000 users and not a lot of datapoints to trian the I will continue to work with them through out the year and further develop it into my professional thesis. But for the sake of final project, 

extract “uid”,"userName",category, sub_category,
            product,
            listing_amount,
            counts,
           total_bid_amount



- conclusion:


## Next Step: 

 justification of the importance of using scalable computing methods to solve it, as well as a description of the large-scale computing methods you employ in the project.


Methodology: The project will utilize machine learning techniques, specifically collaborative filtering, to build the recommendation system. Collaborative filtering will be employed to predict user preferences based on interactions with similar users and items. The dataset will consist of extensive user data (e.g., past purchases, browsing history) and item data (e.g., category, price, reviews) from the e-commerce platform.
