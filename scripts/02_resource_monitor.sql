-- scripts/02_resource_monitor.sql
-- Snowflake SQL for setting up a resource monitor

use role accountadmin;

-- create a resource monitor for the lab
CREATE OR REPLACE RESOURCE MONITOR limiter
  WITH CREDIT_QUOTA = 100
       NOTIFY_USERS = (YOUR_USER_HERE, )
  TRIGGERS ON 75 PERCENT DO NOTIFY
           ON 100 PERCENT DO SUSPEND
           ON 110 PERCENT DO SUSPEND_IMMEDIATE;