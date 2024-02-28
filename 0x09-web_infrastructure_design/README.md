This is a Repository for 0x09-web_infrastructure_design

Each task is explained below:

Task 0: Simple_web_stack
Explanation:

Server: The server is a physical or virtual machine that hosts and serves your web application to users over the internet.

Domain Name: The domain name provides a memorable and human-readable address for your website. It's used to identify and locate resources on the internet. The "www" prefix is a conventional way to denote the web server for a domain.

www DNS Record: The "www" record is typically a CNAME record that points to the domain's root DNS record. It's used to specify that the domain's web content is hosted on a particular server.

Web Server: The web server (Nginx) handles incoming HTTP requests from clients, serves static files, and forwards dynamic requests to the application server. It manages connections, handles SSL/TLS termination, and can perform load balancing to distribute traffic.

Application Server: The application server executes the business logic of your web application, generating dynamic content based on user requests. It communicates with the web server to process incoming requests and return responses.

Database: The database (MySQL) stores and manages structured data for your application. It provides a reliable way to store and retrieve information necessary for your application's functionality.

Communication with User's Computer: The server communicates with the user's computer using the HTTP protocol over the internet. When a user requests a webpage, their browser sends an HTTP request to the server, and the server responds with the requested content.
Issues with the Infrastructure:

Single Point of Failure (SPOF): Since there's only one server, if it goes down, the entire website becomes inaccessible. This could be mitigated by implementing redundancy, such as having multiple servers or utilizing cloud services with built-in redundancy.
Downtime during Maintenance: When maintenance is needed, such as deploying new code that requires restarting the web server, the website will experience downtime. This can disrupt user access and lead to a negative user experience. Implementing strategies like rolling updates or using a load balancer with multiple instances can help minimize downtime during maintenance.

Scalability Issues: If the website experiences a sudden increase in traffic, the single server may struggle to handle the load effectively. This can lead to slow performance or even crashes. Implementing scalability solutions like load balancers, auto-scaling, and distributed databases can help handle increased traffic more effectively.


Task 1`distributed_web_infrastructure Explanation:
Web Servers (Nginx, App, DB): Each server hosts Nginx for web serving, application logic, and a database. Distributing components across servers ensures redundancy and fault tolerance.

Load Balancer: Balances incoming traffic across web servers for scalability and reliability. Terminates SSL to encrypt traffic and offload decryption from the web servers.
Firewalls: Added for network security to control incoming and outgoing traffic. They protect servers from unauthorized access, malware, and other threats.

SSL Certificate (HTTPS): Encrypts data transmitted between the web server and clients, ensuring confidentiality and integrity. It's essential for securing sensitive information like passwords and payment details.

Monitoring Clients: Collect data on server performance, availability, and security. Essential for identifying and addressing issues proactively.
Specifics:

Firewalls: Control access to the servers, preventing unauthorized access and protecting against network attacks.
HTTPS: Encrypts data transmitted over the network, preventing eavesdropping and tampering.

Monitoring: Used to track server health, performance metrics, and security incidents. Sumo Logic collects data from servers and analyzes it to provide insights and alerts.

Monitoring QPS: To monitor web server QPS, you can track the number of incoming requests per second using monitoring tools. Set up alerts for unusual spikes or drops in QPS.
Issues:

SSL Termination at Load Balancer: While terminating SSL at the load balancer improves performance, it introduces a potential security risk as decrypted traffic traverses the internal network.

Single MySQL Server for Writes: Having only one MySQL server capable of accepting writes creates a single point of failure. If the server fails, write operations become unavailable, impacting application functionality.

Identical Servers: Using servers with the same components increases vulnerability to widespread failures. If a critical component fails across all servers simultaneously (e.g., Nginx), the entire infrastructure may become unavailable. It's advisable to diversify components to minimize this risk.
