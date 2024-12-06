import seaborn as sns

# Importing the necessary module to interact w/ Snowflake data
from snowflake.snowpark.context import get_active_session

session = get_active_session()

# The active session is required to query data from Snowflake. 
# Snowpark is the SNowflake framework for working iwth data
# and get_active_session() retrieves a session object that can be used to 
# run SQL queries against Snowflake tables, returning the results as 
# a pandas DataFrame.

# Query to group movies by decade
result = session.sql("""
select
    floor(releaseyear / 10) * 10 as decade,
from
    notebook_lab_db.public.imdb
""").to_pandas()

# Use Seaborn's countplot to create a bar chart
# The x='DECADE' parameter groups bars by the decade column from the result DataFrame
sns.set_theme(style="whitegrid") # Set the style of the chart
ax = sns.countplot(x='DECADE', data=result) # Create the bar chart

# Set the title and axis_labels
ax.set(
    title='Number of Movies by Decade',
    xlabel='Decade',
    ylabel='Number of Movies'
)

# Get the current tick positions on the x-axis
x_ticks = ax.get_xticks() # Numerical posititons of the ticks
x_tick_labels = ax.get_xticklabels() # Labels of the ticks

# Update the tick labels to remove the decimal point
# We use float(label.get_text()) to convert the tick label to a float then convert it to an integer
ax.set_xticks(x_ticks) # Set the tick positions explicitly to avoid issues w/ dynamic tick positions
ax.set_xticklabels([str(int(float(label.get_text()))) for label in x_tick_labels]) # Update the tick labels

# Get the current tick positions on the y-axis
y_ticks = ax.get_yticks() # Numerical positions of the ticks
y_tick_labels = ax.get_yticklabels() # Labels of the ticks

# Set the fixed y-axis tick positions and labels
ax.set_yticks(y_ticks) # Set the tick positions explicitly to avoid issues w/ dynamic tick positions
ax.set_yticklabels(y_tick_labels) # Update the tick labels

