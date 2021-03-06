# Politico

A platform which both the politicians and citizens can use. Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.

## Project Links
https://muirurikin.github.io/Politico/UI/

https://politico-alexona.herokuapp.com/api/v1/

## Technologies used.
* Python 3
* flask

## [Pivotal Tacker Board](https://www.pivotaltracker.com/n/projects/2241669)

## Current endpoints

| Method  | Endpoint  | Usage  |
|---|---|---|     
|GET| /api/v1/parties| Get all parties|
|POST | /api/v1/parties  | Create a new party  |
|GET| /api/v1/offices/  | Get all offices|
|POST|	/api/v1/offices/  |	Create a new office  |
|GET| /api/v1/parties/ (party_id) | Get a specific party|
|GET| /api/v1/offices/ (office_id) | Get a specific office|
|PUT|	/api/v1/parties/(party_id) |	Update a specific partys details.|
|DELETE	| /api/v1/parties/(party_id)	| Delete a specific party.|

## Installation guide and usage

#### **Clone the repo.**
  ```
$git clone https://github.com/muirurikin/Politico.git
  ```

#### **Cd Into Project, Create virtual environment & Activate.**
  ```
$ cd Politico
$ git checkout develop
$ virtualenv [envname]
$ source [envname]/bin/activate
   ```
#### **Install Dependancies.**
  ```
(envname)$pip install -r requirements.txt
  ```

#### **Run the app**
On Linux set the enviroment variables for the project
```
(envname)$ export FLASK_APP=run.py
(envname)$ export FLASK_DEBUG=True
(envname)$ export FLASK_ENV=development
(envname)$ flask run
```
On Windows set the enviroment variables for the project
```
(envname)$ set FLASK_APP=run.py
(envname)$ set FLASK_DEBUG=True
(envname)$ set FLASK_ENV=development
(envname)$ flask run
```

#### **Run Tests**

  ```
(envname)$ pytest
  ```
