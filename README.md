# Jake Gadaleta | Programing with a Network in Mind

## Introduction

This paper will be taking a Python 3 (3.8.6) point of for all examples unless expressly stated otherwise

In this paper we will look at a network with 2 separate and unique view points. 
The first viewpoint will be that of an end user, someone who wants to take information from the internet and use code to be able to preform some task based on that data that has been downloaded.
The second person is that of a content creator / server manager / basically someone who wants to host their own content.
I have decided to take an in-depth look into both viewpoints independently at first to build up the basics and then combine the 2 together in a final section and an overview of how to build a full product. 

I would like to take a quick note and say that the code that I use in the following examples may not be the absolute best ways to solve a given problem instead using the simplest code that I can in order to achieve the explanations.

If you have questions while reading this please feel free to reach out to me and I will do my best to explain [jg9902@desales.edu](mailto:jg9902@desales.edu) and I will try to get back to you in as timely as a manner as I can.

## The End User

This is for the person who wishes to load `.csv` files directly into an analysis tool, or those who want to look through a set of quizlets relating to class in order to get a study sheet for the entire semester, or you want to cycle through wikipedia pages to pull brief definitions on a number of topics. We can even take this as far as to generate our own pseudo-apis to automate the flow of data. 

The TL;DR of this is that its called Web Scraping and involves making http connections to download files to be analyzed through code.

### Requests

The main package that we use to connect to a site and pull down its contents is called 