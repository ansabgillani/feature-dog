> This is just a dummy run state. More detailed run me will be added by me soon.

## How to download it to local env?
Pre-requisites:
- I am developing using Mac, so Python is already installed. Incase you don't have it, please install and configure it on your machine.
- Download github and git if not already installed. Google for more instructions.
- Download Docker if not already installed. Google for more instructions.

1. `$ git clone https://github.com/ansabgillani/feature-dog.git`
2. `$ cd platform`
3. `$ docker-compose run web ./manage.py migrate`
4. `$ docker-compose build` or `docker-compose up -d`

## How to run?
`$ docker-compose up`
or 
`$ docker-compose up -d` to run in the background.

To work with django commands, use:
`$ sudo docker-compose run web ./manage.py migrate` etc.