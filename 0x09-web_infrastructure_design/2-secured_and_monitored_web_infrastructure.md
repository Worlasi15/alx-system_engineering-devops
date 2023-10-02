Server 1: Web Server (Nginx)
- Purpose: This server handles incoming web requests and serves static content.
- Components: Nginx web server.
- Specifics: Nginx is chosen for its efficiency in handling web traffic
and serving static content securely.

Server 2: Application Server
- Purpose: This server runs the application code.
- Components: Node.js, Ruby, or Python (depending on your application stack).
- Specifics: The application server executes dynamic code, handles business logic,
and generates dynamic web pages.

Server 3: Load Balancer (HAproxy)
- Purpose: This server distributes incoming traffic between web and application servers.
- Components: HAproxy load balancer.
- Specifics: HAproxy ensures load balancing and high availability for the website.

Firewalls (3)
- Purpose: Firewalls are added for security.
- Components: Firewall software or hardware.
- Specifics: Firewalls protect the infrastructure from unauthorized access and malicious traffic.

SSL Certificate
- Purpose: To secure traffic to www.foobar.com.
- Components: SSL/TLS certificate.
- Specifics: SSL ensures that data transmitted between clients and servers is encrypted and secure.

Monitoring Clients (3)
- Purpose: To monitor the infrastructure for performance and security.
- Components: Monitoring clients (e.g., Sumo Logic agents).
- Specifics: These clients collect data about server performance, errors, and security incidents for analysis.

Explanation of Specifics:
- Firewalls: Firewalls are added for security to control incoming and outgoing traffic,
preventing unauthorized access and protecting against cyber threats.
- HTTPS: Traffic is served over HTTPS to encrypt data in transit, ensuring confidentiality and integrity.
- Monitoring: Monitoring is used to track server performance, detect issues,
and ensure the availability and security of the infrastructure.
- Data Collection: Monitoring tools collect data by installing agents
or agents collect data directly, which is then sent to a central monitoring server for analysis.
- Web Server QPS (Queries Per Second): To monitor web server QPS,
you can collect data on incoming requests and analyze it to assess server load and performance.

Issues with the Infrastructure:
1. Terminating SSL at the Load Balancer Level:
   - Issue: Terminating SSL at the load balancer means that SSL decryption happens there,
potentially exposing unencrypted traffic on the internal network.
2. Only One MySQL Server Accepting Writes:
   - Issue: A single MySQL server accepting writes creates a single point of failure.
If it fails, write operations to the database will be disrupted.
3. Servers with the Same Components:
   - Issue: Having identical components (database, web server, and application server)
 across all servers may not provide sufficient redundancy or scalability.

To address these issues:
- Use end-to-end encryption (TLS) to secure traffic between
 clients and the application server, not just at the load balancer.
- Implement database replication or clustering to ensure database high availability and failover.
- Consider a more diverse server configuration, including different roles and redundancy,
to improve scalability and fault tolerance.

This revised infrastructure design addresses security, encryption,
and monitoring while mitigating the identified issues for www.foobar.com
