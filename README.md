# Handbag "Store"

This is a site that serves as a listing of different handmade products. 

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Getting Started

The project is a website made with django. It is something between an e-commerce site and a gallery - not exactly just simple pictures with not much else, but not a store either, as implementing the payment system and login options were not required.
There is functionality to add, update and delete items, provided you have admin privileges, and also views them. Pretty much a simple CRUD app made mostly with generic views. 

## Prerequisites

Latest version of python and django are required. 

AWS S3 buckets are used to store static files, so you would need to configur those and set environment variables accordingly. 
The app could also be configured to not use aws services and save the files in your static folder instead. This can be achieved with a relatively few lines of code in settings.py.

## Installation

Step-by-step guide on how to install and set up the project.
WIP

## Acknowledgements

I used Dennis Ivy's Photo Album App tutorial as inspiration and a starting point. You can find the tutorial [here](https://youtu.be/sSquD2u5Ie0?si=uucjXbFBIYh6mLOW).
