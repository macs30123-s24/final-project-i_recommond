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

### Methods: 

The data pipeline initiates by retrieving user data from a PostgreSQL database provided by Encore. I designed a Lambda function to extract attributes such as "uid," "userName," "category," "sub_category," "product," "listing_amount," "counts," and "total_bid_amount" from the database. Utilizing AWS Lambda's serverless architecture allows the data extracted from PostgreSQL to be processed and transformed into CSV format, then stored in an Amazon S3 bucket. This bucket serves as an intermediary before the data is accessed by an Amazon EMR cluster to run sophisticated PySpark jobs for my recommendation model. Finally, the analyzed data is saved back into the S3 bucket as JSON files, which are linked with pre-signed URLs to provide secure, temporary access for sharing results with stakeholders or integrating into other applications.

* Notice: Currently, we have only about 1,000 users and not many data points to train the model. I used the Python Faker library to generate additional data, uploading another CSV to S3 to simulate analysis with 100,000 data points. This step won't be necessary once we have sufficient real data. I implemented this to demonstrate that my code can scale to analyze 100K data points effectively.  

Overview of the pipline: 
  ![pipleline](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/pipeline.jpg)  

This diagram illustrates a robust data pipeline optimized for handling over 100,000 daily users by leveraging various AWS services and technologies.  

The pipeline operates as follows:

- [Setup](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/Setup.ipynb):
  - This file will set up lambda function, s3 bucket, EMR cluster and access S3 to generate the presigned URLS. (All BOTO3 related Stuff)
- [lambda function](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/lambda_function/lambda_deployment.py):
  - my lambda function can connect to PostgreSQL database and get all the data I need. Then, it can convert all data into csv format and save it into my S3 bucket for later access
  - to access PostgreSQL, I need to use psycopg2, which need to be additionally downloaded to the lambda function zip. I made the lambda function folder first and then used bash commond "pip install aws-psycopg2" in that folder. Then I zipped all files into [lambda_function.zip](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/lambda_function.zip)
- [mock data](https://github.com/macs30123-s24/final-project-i_recommond/tree/main/Mock_data):
  - as I explained earier, in order to prove that my pipeline can be applied to a large dataset, I have to boostrape some data at this point.
  - by using [bootstrapping](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/Mock_data/bootstrapping.ipynb), I created the [100k large dataset](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/Mock_data/fake_user_interaction.csv) and used that for further analysis:
- [pySpark Model](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/Recommendation_models.ipynb)
  - After creating the EMR Spark cluster, I SSHed into JupyterHub and wrote my PySpark code there. This PySpark script primarily focuses on several key tasks:
    - Cleaning the data.
    - Building the heuristic popularity model and the collaborative filtering model (ALS). The heuristic model is based on popularity (using the highest number of bids for each category) for users who don't have any data on the platform but have indicated their interests through a short questionnaire at the beginning, and Collaborative filtering is for users who have bidding history.
    - Evaluating the ALS model to find the best parameters.
    - Combining the popularity and collaborative filtering models to mitigate the cold start problem.
  - Finally, I generated recommendations for all users and saved them into JSON files in S3.
- [result](https://github.com/macs30123-s24/final-project-i_recommond/blob/main/part-00001-f50433a4-652e-40d9-8878-c6317443e011-c000%20.json)
  - This is one of the 25 JSON files I created using PySpark. For this json file, keys are userNames and values are tuples (product, predicted_bids). To create a file like this, you can refer back to my setup file and run the last section of code, which generates pre-signed S3 URLs for temporary public access. By clicking on these URLs, a JSON file like this will automatically be downloaded for you.
    
### Purpose and Impact:  

This pipeline is designed not only to handle the high volume of data efficiently but also to enhance the user experience on the Encore platform by providing timely and relevant product recommendations. By automating data processing and leveraging cloud services, the pipeline supports Encore's rapid growth and adaptability to market changes.

## Next Step: 

I have initiated a recommendation model using PySpark, which currently generates JSON files stored in S3, accessible via pre-signed URLs for easy download. This setup is part of an ongoing project with Encore, aimed at enhancing user experience by accurately targeting younger demographics with personalized product recommendations. As an initial phase, I've employed heuristic popularity models and collaborative filtering methods. Over the upcoming summer and academic year, I plan to expand this by experimenting with more sophisticated techniques like item-item filtering, deep learning, and two-tower models to optimize performance. The current strategy of saving recommendations in JSON format is based on my assumption that the team can utilize the results effectively. However, I will need to evaluate and possibly adjust this approach to ensure it aligns with the requirements of the project and stakeholders.
