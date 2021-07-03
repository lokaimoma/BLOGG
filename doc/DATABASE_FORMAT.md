![BLOGG logo](../assets/blog_logo.png)
## General database URL format
- - -
In this project the database operations are done
asynchronously. Therefore an asynchronous database
driver has to be installed for any database you for 
at the end of the day.   
That is why by default **aiosqlite** is installed for
for sqlite databases, and that dependency is added to 
the requirements by default.   
For each database I mention below, I will give the async
driver to be installed also.  
Below is the general URL format.
```
dialect+driver://username:password@host:port/database
```
## NOTE
- - -
The environmental variable for the database url must have
a key of **DATABASE_URL**.   
**PLEASE REMEMBER TO ACTIVATE THE VIRTUAL ENVIRONMENT 
BEFORE INSTALLTING ANY ASYNC DATABASE DRIVER**

## SQLITE
```
DATABASE_URL=sqlite+aiosqlite:///database_name.sqlite
```
**aiosqlite**: Async driver of sqlite (Installed already)

## MySQL
- - -
```
DATABASE_URL=mysql+aiomysql://username:password@host:port/database_name
```
**aiomysql**: Async driver for MySQL   
How to install  
**Assuming virtual environment is activated.**
```
pip install aiomysql
```

## PostgreSQL
- - -
```
DATABASE_URL=postgresql+asyncpg://username:password@host:port/database_name
```
**asyncpg**: Async Database driver for PostgreSQL   
How to install  
**Assuming virtual environment is activated.**
```
pip install asyncpg
```

## Oracle
- - -
```
DATABASE_URL=oracle+cx_Oracle_async://username:password@database_name
```
**cx_Oracle_async**: Async Databse driver for Oracle   
How to install  
**Assuming virtual environment is activated.**
```
pip install cx-Oracle-async
```
