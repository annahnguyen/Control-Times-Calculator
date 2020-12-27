# Brevet Control time calculator service
---
Name: Anna Nguyen

Email: anguyen5@uoregon.edu

## Info 

* Front-end - AJAX, jQuery, CSS, PHP
* Back-end - Flask-based server, MongoDB (NoSQL) storage
* Basic HTTP/IP Protocol
* RESTful API implementation
* Docker deployment and Git version control

## ACP Time Calculator

The information for the ACP time calculator can be referenced from the following link: https://rusa.org/pages/acp-brevet-control-times-calculator.

The calculator operates following the rules found in the link provided above. It will take in the start time, distance of the brevet, and the last control distance inputed. The open and close times are then calculated based on which range the control distance falls into, (0, 200), (201, 300), (301, 400), (401, 600), or (601, 1000).

When the control distance is greater than the brevet distance, an overall time limit is established (details at rusa.org/pages/rulesForRiders, Article 9). The 0km starting point always closes 1 hour after the start time of the race. The maximum brevet distance should be 1000km due to higher distance races not being used for an ACP brevet (see under "Oddities" in the reference link).

## Usage

Build by typing: $ docker-compose up --build
Access the webpage to input data by typing this into the url: http://localhost:5010.

Select the brevet distance, and input a distance, either in miles or kilometers in the table. The open and close spaces will then be populated with appropriate times. Pressing "Submit" will put the data from the fields into a database. Pressing "Display" will load a page with the open and close times taken from the database.

Going to http://localhost:5001/[YourAPIhere>] will display subsequent information specified below. EX: http://localhost:5001/listAll/csv should display all open and close times in CSV format. NOTE: Query parameter to get top "k" does not work with listAll APIs or APIs without format specification.

The application supports the following APIs:

    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format
