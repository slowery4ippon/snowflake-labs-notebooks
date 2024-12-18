import seaborn as sns

# Importing the necessary module to interact with Snowflake data
from snowflake.snowpark.context import get_active_session
session = get_active_session()

# The active session is required to query data from Snowflake.
# Snowpark is the Snowflake framework for working with data, 
# and get_active_session() retrieves the current active session.
# This allows us to run SQL queries directly against Snowflake tables,
#returning the result as a Pandas DataFrame for further analysis.


# Query to group movies by decade
result = session.sql("""
    SELECT 
        FLOOR(releaseyear / 20) * 20 AS decade
    FROM notebook_lab_db.public.imdb
""").to_pandas()

# Use Seaborn's countplot to create the bar graph by decade
# The `x="DECADE"` argument ensures that the bars are grouped by the decade column
sns.set_theme(style="whitegrid") # Set the Seaborn theme for better aesthetics
ax = sns.countplot(
    data=result, # Data to plot (grouped by decade)
    x="DECADE", # x-axis corresponds to decades
)

# Set title and axis labels
ax.set(
    title="Number of Movies by Release Year Decade", # Title of the plot
    xlabel="Decade", # Label for the x-axis
    ylabel="Number of Movies" # Label for the y-axis
)

# Get the current tick positions on the x-axis (decade positions)
x_ticks = ax.get_xticks() # These are the numerical positions of the x ticks
x_tick_labels = ax.get_xticklabels() # These are the labels of the ticks (decades)

# Update tick labels to remove decimals
# We use `float(label.get_text())` to remove decimals, then convert it to an integer
# This ensures that the label is displayed without the ".0" decimal part
ax.set_xticks(x_ticks)  # Ensure the tick positions are fixed (helps avoid issues with dynamic ticks)
ax.set_xticklabels([str(int(float(label.get_text()))) for label in x_tick_labels]) # Remove decimals and set the labels

# Get the current y-axis tick positions and labels
y_ticks = ax.get_yticks()  # Get the positions of the y ticks
y_tick_labels = [f'{int(x):,}' for x in y_ticks]  # Format the tick labels by adding commas to large numbers

# Set the fixed y-axis ticks and labels
ax.set_yticks(y_ticks)  # Fix the positions
ax.set_yticklabels(y_tick_labels)  # Set the formatted labels


