# tmdb-cloner
A python tool to make a local clone of tmdb using mongodb.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes.

### Prerequisites

Requirements for the software
- [mongodb](https://www.mongodb.com/)
- [TMDB Api Key](https://www.themoviedb.org/documentation/api)

### Installing

First we start by installling mongodb and then proceed to setup our environment, and we finish up by running the cloner.

Step 1 - Mongodb installation

    Follow instructions for your operating system here: https://docs.mongodb.com/guides/server/install

    Add the mongodb url  this line to the bottom of your ~/.bashrc file
    
    export MONGODB_URL='mongodb://localhost:27017'

Step 2 - Add api key to local environment

    export MONGODB_URL='mongodb://localhost:27017'
    pip install --user pipenv
    pipenv install -r requirements.txt
    
    

Step 2 - Environment setup
    pip install --user pipenv
    pipenv install -r requirements.txt
 
Step 3 - Run tmdb-cloner
    pipenv run main.py

Step 4 - Wait for the cloner to finish doing its thing, if you encounter problems just restart the program

## Deployment

Add additional notes to deploy this on a live system

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Javier Beca** - *Main Developer* -
    [PurpleBooth](https://github.com/jcuervo-dev)

See also the list of
[contributors](https://github.com/jcuervo-dev/tmdb-cloner/contributors)
who participated in this project.

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE.md)
GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for
details