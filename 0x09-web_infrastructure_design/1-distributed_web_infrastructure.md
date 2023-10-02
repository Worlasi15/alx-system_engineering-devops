Load Balancer (HAProxy):
Load Balancer Configuration: Round Robin
The HAProxy load balancer is set up to use a basic round-robin algorithm
for distributing incoming traffic evenly between the two web servers.

Active-Active Setup:
Both web servers are active concurrently, handling incoming requests simultaneously.
This setup guarantees both high availability and effective load distribution.

Web Servers (Nginx):
These servers manage incoming HTTP requests, deliver static content,
and function as a reverse proxy to forward dynamic requests to the application server.
Nginx offers improved performance, security, and scalability.

Application Server:
This server receives dynamic requests from Nginx and executes the codebase for the website.
The separation of the application layer from the web server layer facilitates enhanced scalability
and easier maintenance.

Database Cluster (MySQL):
Primary-Replica (Master-Slave) Configuration:
The primary node (Master) handles write operations and replicates data to the replica node (Slave).

Distinguishing Primary and Replica:
The Primary node is responsible for write operations, ensuring data consistency,
while the Replica node replicates data from the Primary and serves read-only requests.
This configuration enhances data availability, reliability, and read scalability.

Challenges with the Infrastructure:

Single Point of Failure (SPOF):
The load balancer itself could be a single point of failure. It is advisable to consider
implementing a redundant load balancer configuration to mitigate this risk.

Lack of Redundancy in Other Components:
Redundancy is absent in other components such as web servers, the application server, and the database,
making them susceptible to single points of failure as well.

Security Concerns:
Absence of a Firewall:
The infrastructure lacks a firewall to control incoming and outgoing traffic, which would enhance security significantly.

Absence of HTTPS:
Implementing HTTPS is essential to encrypt data during transit, ensuring secure communication
 between clients and the web servers.

Monitoring:
The infrastructure lacks monitoring tools, making it challenging to detect and respond to issues in real-time.
It is crucial to implement monitoring solutions to monitor server health, performance, and security incidents effectively
