# STB: Authentication App

[![Project Status](https://img.shields.io/static/v1?label=project%20status&message=in%20development&color=yellow&style=flat-square)](#)

Application responsible for providing security for the APIs of the STB project.

![resources](assets/images/resources.png)

Features:
- sign up
- login
- logout


## Requirements

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


## Installation

(IN PROGRESS)

```bash
$ docker-compose up --build
```


## Run Locally
```bash
$ sam local start-api
$ curl http://localhost:3000/
```


## Usage

(IN PROGRESS)

```bash
# sign up
$ curl -X POST http://localhost/signup

# sign up
$ curl -X POST http://localhost/login
```


## Running Tests

(IN PROGRESS)

```bash
$ pytest --cov=app tests/
```


## Tech Stack

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)


## Reference
- https://aws.amazon.com/blogs/compute/using-github-actions-to-deploy-serverless-applications/
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html


## Feedback

If you have any feedback, please contact me at raphaeldias.ti@gmail.com

[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/raphaelbh)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raphaelbh/)