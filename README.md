# OctopusLab
Code challenge Octopus labs

##How to run
Run the command "docker-compose up"
The Api will be accessible form your local machine via below url

127.0.0.1:8888

##Improvements and Assumptions

- Swagger can be configured for auto generated documentation.
- Salted Hash and Encryption can also be implemented in the DB (this is arguable and may vary case case to case)
- I have created an admin page. right now it does not require authentication. In production there should be user model via which authentication can be performed( JWT, OAuth, Secure cookies ) 
- THe public and private keys for encryption should be generated once and saved in DB for future use. Right now they are saved as global variable and chabge with each execution of program
- Ideally Front end should be seperate. Preferably in new JS tech like react or angular.
- NLTK is used to detect verbs and nouns. It can be furthur improved by providing more strict parameters.
- Wait_for_it ensures that web server starts after db is up and ready