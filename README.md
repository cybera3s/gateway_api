<div>
    <h1 align="center">Gateway API Service</h1>

<p>
This is an example of an GRPC client that sends remote procedure calls to the server.
</p>
</div>

### Built With
 * [Django](https://www.djangoproject.com/)
 
### Prerequisites


* [Python](https://www.python.org/) 3.8
* PIP
* virtualenv 
  

### Usage (Docker)

Clone the GRPC Client repository

   ```sh

  git clone https://github.com/cybera3s/gateway_api.git

   ```

in the same directory Clone the GRPC server repository

   ```sh

  git clone https://github.com/cybera3s/user_management_service.git

   ```


move the <b>docker-compose</b> from user_management_service to current directory 

    mv user_management_service/docker-compose.yml .


<h2>Initial .env variables for Client</h2>

Add and Open .env file to add Required Configurations:
```sh
nano gateway_api/gateway_api/.env
   ```
Add these required Configurations to .env file for GRPC Client:
```sh
SECRET_KEY=<your secret key>

ALLOWED_HOSTS=<host1,host2,...> or '*'

GRPC_SERVER_PORT=<grpc server port default 50051>
   ```
Save Your changes with CTRL+X 


<h2>Initial .env for Server</h2>

Add and Open .env file to add Required Configurations:
```sh
nano user_management_service/user_manager/.env
   ```
Add these required Configurations to .env file for GRPC server:
```sh
SECRET_KEY=<your secret key>

POSTGRES_DBNAME=<database name>
POSTGRES_USER=<database username>
POSTGRES_PASSWORD=<database password>
POSTGRES_PORT=<database port>
   ```
Save Your changes with CTRL+X 
<hr>
Run and Build docker-compose file

    docker-compose --env-file ./user_management_service/user_manager/.env up --build 

if everything goes well visit site at: http://127.0.0.1:1234/swagger


## License

Distributed under the GPL License




<!-- CONTACT -->

## Contact

Sajad Safa - cybera.3s@gmail.com


<p align="right">(<a href="#top">back to top</a>)</p>