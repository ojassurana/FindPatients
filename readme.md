*WEBSITE AND BOT IS NOW DEFUNCT* 

Website: https://www.findpatients.in * 
Telegram bot URL: https://www.t.me/FindPatientsBot. 



## Contents

* Introduction 
* Telegram bot
* Auto correct system
* Webhook 
* Lambda function 
* MongoDB 
* Flask app 
* Elastic Beanstalk
* Dynamic tables

## Introduction

India went through a huge spike in Covid-19 cases in the form of a second wave.Making resources even more scarce then it already was Unfortunately, due to just an overall lack in resources, the Indian people were driven into desperate measures to obtain resources to keep themselves and their loved ones alive.
Indian social media, which was the only platform people could turn to, was filled with cries for help.
Donation requests for necessities such as oxygen tanks and hospital beds accompanied with contact details were a common sight on every social media platform.  
We came to realise that this way of communication between donees and donors has its inadequacies. 
It presents a difficulty for a connection between donors and donees to be formed. 
Let’s say you are a donor who can only provide remedisvir in your city(delhi), won’t it be more efficient if you can just get a list of donees who require remedisvir in Delhi specifically instead of being constantly bombarded with irrelevant posts.


## Telegram bot

Telegram bot runs on a Python <a href='https://github.com/ojassurana/Immigrant-Technologies/blob/main/Telegram%20Bot/lambda_function.py'>script</a> and is hosted on AWS Lambda where it retrieves the data from the user. As such, this script **WILL NOT WORK IF YOU JUST RUN IT ON ANY PLACE OTHER THAN AWS LAMBDA**.
After which, we linked it to AWS API Gateway and set up a Telegram Webhook.

## Auto correct system

We used the levenshtein distance algorithm for the prediction of the city word incase someone misspells their city. For example, if someone types "Deli" instead of "Delhi", the code will know which is correct word to use as city :) 

## Webhook

Faster and more bandwidth efficient than pinging the server multiple times. Uses the AWS api gateway to connect the services together in a seamless way 

## MongoDB

MongoDB is used to store data and is hosted on AWS in a mumbai server for min ping.

## Elastic Beanstalk

Fast and efficient scaling of computing resources in the cloud 

## Dynamic tables

Usage of dynamic tables to portray the data in a conveyed in a concise manner for the donor to view
