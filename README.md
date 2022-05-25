# This project is creating to collect and store song data and user activity of Sparkify's music streaming application.

# Database structures
This project use a database name Sparkify with a Fact table and 4 dimension tables.
## Fact table:
- **songplays**: to store data of user activity on application
    + songplay_id serial
    + start_time timestamp
    + user_id int
    + level varchar(50)
    + song_id char(18)
    + artist_id char(18)
    + session_id char(18)
    + location varchar(100)
    + user_agent varchar(400)

## Dimension tables
- **songs**: to store data of all songs
    + song_id char(18)
    + title varchar(200)
    + artist_id char(18)
    + year int
    + duration float

- **users**: to store data of all users who used the application
    + user_id int
    + first_name varchar(100)
    + last_name varchar(100)
    + gender char(1)
    + level varchar(50)

- **times**: to store timestamp information of all activities
    + start_time timestamp,
    + hour int
    + day int
    + week int
    + month int
    + year int
    + weekday int
    
- **artist**: to store artist data who create the song
    + artist_id char(18)
    + name varchar(200)
    + location varchar(200)
    + latitude float
    + longitude float

# To using this project, you need have at least 3 Python script files in your working directory:
- sql_queries.py: to store all of SQL queries for project
- create_tables.py: to create/reset all table structures of Sparkify database
- etl.py: to analyze and insert data to all tables

# How to run
- Step 1: put all 3 scripts into a single folder
- Step 2: run `python create_tables.py` to initialize the table structures
- Step 3: run `python etl.py` to insert song and user activity data