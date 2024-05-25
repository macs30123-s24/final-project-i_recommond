# AWS Assisted Pipline for A Recommondation System

### Yunrui Bao

## Problem Description: 
The shift towards digital marketplaces has transformed consumer behavior, offering the convenience of shopping from the comfort of home. Yet, this transformation has also introduced a challenge: information overload. To mitigate this, recommender systems have emerged as crucial tools that filter through the abundance of choices to deliver personalized product suggestions aligned with individual preferences, enhancing user experience and potentially increasing company revenues. For instance, McKinsey reports highlight that up to 35% of Amazon purchases and 75% of content viewed on Netflix are driven by these recommendation algorithms.  

In collaboration with "Encore," a pioneering startup launching a novel second-hand marketplace tailored to the digital-native younger generation through short video auctions, I aim to design a recommendation system that best suits users on this platform. Unlike traditional platforms such as eBay, which predominantly attracts users aged between 35-64, Encore focuses on capturing the untapped market of young millennials and Gen Z. These demographics demonstrate a burgeoning interest in vintage fashion—a trend that promises a solid and less saturated market opportunity for innovative platforms like Encore.  

The core objective of this project is to develop a robust AWS pipeline capable of managing over 100,000 daily users while delivering appropriate recommendations. This pipeline will leverage AWS services for large-scale data processing, ensuring users receive timely and relevant product suggestions. Designed for scalability and efficiency, it aims to support the rapid growth of Encore and maintain the flexibility required to adapt to an evolving market. The ultimate goal of my recommendation system is to enhance the user experience on Encore and attract an increasing number of new users to the platform. Currently, the project's focus is on establishing an automated pipeline rather than refining the recommendation system itself, because our dataset is not yet large enough to train sophisticated models. Initially, I have implemented heuristic popularity models and collaborative filtering methods. As we collect more data, I plan to further develop and enhance the recommendation engine as part of my professional thesis next year.

## Social Science Implication: 
This project addresses the social science research problem of understanding consumer behavior in digital environments. By analyzing large datasets of user interactions and item information, the recommendation algorithm can reveal patterns and preferences that are not immediately apparent, providing insights into consumer decision-making processes. This aligns with computational social science by combining data science with behavioral analysis to better understand and predict user actions.

## Solution: 

### Justification for Large-scale Computing: 
As our application scales beyond 10K or 100K users, running the recommendation model on local infrastructure becomes impractical due to the significant computational power required. Additionally, implementing collaborative filtering methods necessitates generating a large matrix, which is unfeasible for local computation when dealing with user data at scale. To address these challenges, I have designed a pipeline that eliminates the need for local analysis, allowing results to be directly accessed through a JSON file saved in a S3 bucket. By leveraging large-scale computing techniques, this system can efficiently conduct analyses for over 100,000 users within a minute, ensuring performance and scalability.  

### Overview of the pipline: 
  ![pipleline](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/pipeline.jpg)  

This diagram illustrates a robust data pipeline optimized for handling over 100,000 daily users by leveraging various AWS services and technologies.  


### Methods: 
The pipeline operates as follows:
- PostgreSQL Database: The process begins with a PostgreSQL database where user data is stored. The pipeline initiates by connecting to this database to retrieve the necessary data.

- AWS Lambda: Once the data is fetched, AWS Lambda functions are used to process and transform this data into a CSV format. Lambda provides a serverless architecture that helps scale data processing without the need to manage servers.

- Amazon S3: The processed CSV file is then stored in an S3 bucket, a scalable storage solution in AWS. This storage acts as an intermediary, holding the data before it's further processed by PySpark.

- Amazon EMR: The stored CSV data is accessed by an Amazon EMR (Elastic MapReduce) cluster, which runs PySpark jobs. PySpark allows for sophisticated data processing and analytics, suitable for the large-scale data inherent to this pipeline.

- URLs: The JSON files stored in S3 are associated with pre-signed URLs, which facilitate secure and temporary access to the data. These URLs can be used to share analysis results with stakeholders or to integrate results into other applications or platforms.





Currently, we only have 1000 users and not a lot of datapoints to trian the I will continue to work with them through out the year and further develop it into my professional thesis. But for the sake of final project, 

extract “uid”,"userName",category, sub_category,
            product,
            listing_amount,
            counts,
           total_bid_amount



### Purpose and Impact:  

This pipeline is designed not only to handle the high volume of data efficiently but also to enhance the user experience on the Encore platform by providing timely and relevant product recommendations. By automating data processing and leveraging cloud services, the pipeline supports Encore's rapid growth and adaptability to market changes.



## Next Step: 


