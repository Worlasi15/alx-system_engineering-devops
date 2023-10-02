 Single Server: this is a computer-based system that hands out
services and resources to other computers that will be known as clients over internet.
In this infrastructure, we will use a single server that has been assigned the IP address of 8.8.8.8.8
to host the whole infrastructure (web application and database).
 Domain Name: this is an address that helps users to have access to websites.
In this infrastructure, foobar.com will be our domain name which will be configured
using the DNS record that will point out our IP address.
The point of the domain name is to make it readable to users rather than pointing out IP addresses to them
 which could be meaningless to them.
DNS Record: A Canonical Name record for "www.foobar.com" in the DNS configuration,
will then be created which will point out to "foobar.com."
and come to a consensus that both "www.foobar.com" and "foobar.com" resolve to the IP address 8.8.8.8.
 Web Server (Nginx): the Nginx will be used as a webserver in this infrastructure to take care of HTTP requests
and points them to the right resources on the single server. It will also establish a secure connection
by listening on port 80 which is the HTTP and port 443 which is the HTTPS.
Application Server: Application server is known to host applications,
install them and helps in the operation of the application as well as interacts with the database.
It will receive requests from the webserver and sends feedbacks after it processes it.
Application Files (Code Base): it contains the web application files and the entire source code that constitute in
bringing your website to action. This is kept on the single server introduced and then executed by
the application server depending on the user requests. The files normally comprise od CSS, HTML, JavaScript etc.
Database (MySQL): it plays the role of storing organized and structured data for the web application for easy retrieval,
management and access.
User Communication: A user will have access to the website,
when "www.foobar.com" in their web browser. The DNS system then resolves this domain name to our server's IP address which is 8.8.8.8.
The user's browser establishes an HTTP connection to our server over port 80 (or HTTPS over port 443 for secure connections).
Nginx receives the request, forward dynamic requests to the application server, and return the appropriate response to the user's browser.

ISSUES WITH THE INFRASTRUCTURE
Single Point of Failure: The infrastructure has a single server setup which means that if the server fails,
the entire website becomes inaccessible
Downtime During Maintenance: in this context, when maintenance needs to be done
like adding a new code it could requires restarting the web server or database that can cause downtime.
Scalability Limitations: This infrastructure will face challenges in handling high incoming traffic
since it is having just one server that provides all resources and services. It may slow down the server since traffic will be a lot for just a
single server.
