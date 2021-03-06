# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
    songplay_id serial primary key,
    start_time timestamp,
    user_id int,
    level varchar(50),
    song_id char(18),
    artist_id char(18),
    session_id char(18),
    location varchar(100),
    user_agent varchar(400)
);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
    user_id int,
    first_name varchar(100),
    last_name varchar(100),
    gender char(1),
    level varchar(50)
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
    song_id char(18),
    title varchar(200),
    artist_id char(18),
    year int,
    duration float
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
    artist_id char(18),
    name varchar(200),
    location varchar(200),
    latitude float,
    longitude float
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS times(
    start_time timestamp,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users(
    user_id,
    first_name,
    last_name,
    gender,
    level
) VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO songs(
    song_id,
    title,
    artist_id,
    year,
    duration
) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO artists (
    artist_id,
    name,
    location,
    latitude,
    longitude
) VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO times (
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
SELECT
    s.song_id AS songid,
    a.artist_id AS artistid
FROM songs s
    INNER JOIN artists a
        ON s.artist_id = a.artist_id
WHERE s.title = %s
    AND a.name = %s
    AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]