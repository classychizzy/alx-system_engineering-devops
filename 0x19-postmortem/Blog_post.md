# **Misspelt Endpoint incidence report**
-----------------------------------------

![postmortem](https://user-images.githubusercontent.com/45069751/200926552-be6d29f7-cc29-452c-a227-83caff169373.jpg)
## **Issue Summary**
--------------------
On Thursday 3rd of November, from 12:00 am to Friday  6:00 am, some of our users experienced an outage when trying to access a particular page on our website. The root cause was a misspelt endpoint in the API.

## **Timeline**
---------------
- 12:00 am: a new webpage was added to our website and consequently the API was updated from the backend
- 12:10am: the junior DevOps engineer tried to access the page and got the error message “400 redirect URI mismatch “ 
- 12:13am: the junior DevOps started debugging the web server and noticed the issue was peculiar to a particular page on the website
- 12:20 am: after checking all the files in the var/www/html and confirming that the html for the particular page was present.
- 12:25 am: the junior Devops engineer contacts the backend team to check for things on their end
- 12:30 am: the backend engineer debugs the Django application using the debug toolbar. He finds out that the requested URL was not present and checks the mysites/urls.py and finds out that the endpoint was misspelt. He then updates it.
-12:35am: the backend engineer tested the server with curl 127.0.0.1 and the problem was solved

## **Root cause and resolution**
--------------------------------
The problem was that the backend engineer misspelt an endpoint in the url.py file, and extra “s” was added to the “/bags” so the name was changed to “/bagss”. He failed to test the app after creating the endpoint. Therefore, when it was time to test consume the API, the system failed.
To solve this problem, it is recommended that for every update; the engineer tests the app on the development server. All endpoints must be thoroughly checked before changes are pushed.

## **Corrective and preventive measures**
---------------------------------------
 To prevent this kind of issue from happening, it is recommended that a senior engineer tests all work by the junior engineers on the team and junior engineers are sensitised to not skip tests after changing files.
To address this kind of issues the following steps can be followed:
- Check the server is up and send a request to it e.g curl 127.0.0.1
- Check all processes involved, e.g MySQL, nginx, etc.
- Debug the web server process when a request arrives. E.g. Postman can check if endpoints are working properly.
- Read each message displayed 
- Solve the problem

