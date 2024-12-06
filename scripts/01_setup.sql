-- scripts/01_setup.sql
-- Snowflake SQL for setting up Snowflake Labs

-- security admin owns roles & grants
use role securityadmin;
create role notebook_lab_role;

-- sysadmin creates account objects
use role sysadmin;

-- create a warehouse for the lab
create warehouse notebook_lab_wh
with WAREHOUSE_TYPE = standard
    WAREHOUSE_SIZE = XSMALL
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE
;

-- create a database for the lab
create database notebook_lab_db;

-- grant ownership of the warehouse and database to the lab role
use role securityadmin;

grant ownership on warehouse notebook_lab_wh to notebook_lab_role;
grant ownership on database notebook_lab_db to notebook_lab_role;
grant ownership on schema notebook_lab_db.public to notebook_lab_role;
grant create notebook on schema notebook_lab_db.public to notebook_lab_role;

-- grant the lab role to the user (replace YOUR_USER_HERE with your username)
grant role notebook_lab_role to user YOUR_USER_HERE;
