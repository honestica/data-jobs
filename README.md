# Lifen Data Challenge

 Looking for a job? Check out our [open positions](https://www.welcometothejungle.co/companies/lifen/jobs).

## Guidelines

- clone this repo (do **not** fork it)
- solve the levels in ascending order
- commit your code at the end of each level

You can have a look at the higher levels, but please do the **simplest thing** that could work for the level you're currently solving.

Each level uses the previous one, you can re-use your old code.

Don't hesitate to write [shameless code](http://red-badger.com/blog/2014/08/20/i-spent-3-days-with-sandi-metz-heres-what-i-learned/) at first, and then refactor it in the next levels.

For higher levels we are interested in seeing code that is:
- maintainable
- clean
- robust
- reliable

We are waiting for python (3.9) code.
Write your program in the corresponding level directory.
Do not modify given programs.


## Level 1

Run the `communication_file_generator.py` program in order to generate communication logs into folder `./communications/communications-{id}.json`. Each file represent one communication and it will look like this:

`id=0a0bd4d3-05cf-4912-b6ee-40d79a4f9901|telecom=mail|created_at=2019-07-26 18:30:07|sender={'name': 'Herve Delatour', 'profession': 'liberal'}`

The goal is to read all these files and transform them into json files in `./processed/communication-{id}.json` like this: 

```
{
   'id':'0a0bd4d3-05cf-4912-b6ee-40d79a4f9901',
   'telecom':'mail',
   'created_at':'2019-07-26 18:30:07',
   'sender':{
      'name':'Herve Delatour',
      'category':'liberal'
   }
}
```

## Level 2

As in previous level, instead of writing logs, we would like to insert them into a Mysql database.

You can use a table as follow:

```
CREATE TABLE communication(
   id varchar(100),
   telecom varchar(10),
   created_at timestamp,
   sender_name varchar(50),
   sender_category varchar(20)
)
```

## SQL level

Based on the table previously created we would like to answer these questions:
- Demateralization rate (= number of papered communication / total number of communication) for each `liberal` doctors
- Doctors list that have sent at least 5 communications during the 7 days following their first communication.

You can write your queries in the file `level_sql/queries.sql`.

### Data details

**communication:**

- `id`: communication ID
- `telecom`: medium used to sent the communication
- `created_at`: sending timestamp of the communication
- `sender_name`: name of the person who send the communication
- `sender_category`: job type of the person who send the communication

If you haven't made technical level 2, you can use data stored in `./sample/communications_sample.csv`.
No obligation of setting up a database, we'll only focus on the sql code.

Have fun
