# become_qa
This is the framework designed in order to perform tests for Github using UI and API approaches.

## Framework structure
Contains two main folders - 'src' and 'tests'. Purpose of first one is to store source code of test framework, second one is to store automated tests itself. 

### SRC
#### Config module
Config is responsible to storing framework's and env's configuration. Parameters in config module will be used in whole framework - like setting file for whole project.

Adding new content: add new method in 'config.py' file.

#### Applications module
Applications folder contains all required methods for UI and API tests for testing specific application, which are NOT test cases.

Adding new tests: create folder with application name (example: 'github'). Create subfolders with : 'api' and 'ui'. Store test cases in respective subfolders. Create .py file with convention 'ApplicationName_TestType' (example: 'github_api.py').

#### Helpers
Additional helping functions with purpose to reusing in whole framework. 

Adding new content: add new function in 'helpers.py' file.

### TESTS
#### tests
Test module should contain all created test cases for specific application.

Adding new tests: create folder with application name (example: 'github'). Create subfolders with : 'api' and 'ui'. Store test cases in respective subfolders. Remember to use 'test_' prefix in naming. 
