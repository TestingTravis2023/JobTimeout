import time
# #loop for more than 10 mins
# # Set the duration to run the script
# DURATION = 11 * 60  # 11 minutes in seconds

# # Set the interval to print remaining time
# # Donot print anything until or > than 10 mins
# INTERVAL = 11 * 60  # 5 minutes in seconds

# # Get the start time
# start_time = time.time()

# # Run the script
# while (time.time() - start_time) < DURATION:
#     # Calculate the remaining time
#     remaining = DURATION - (time.time() - start_time)

#     # Check if it's time to print the remaining time
#     if (time.time() - start_time) >= INTERVAL:
#         print(f"Remaining time: {int(remaining/60)} minutes")
#         INTERVAL += (5*60)  # Update the interval

#     # Sleep for 1 minute
#     time.sleep(60)

# print("Script has finished running for 11 mins without printing anything.")



# #loop for more than 50 mins
# # Set the duration to run the script
# DURATION = 51 * 60  # 50 minutes in seconds

# # Set the interval to print remaining time
# # Donot print anything until or > than 10 mins
# INTERVAL = 5 * 60  # 5 minutes in seconds

# # Get the start time
# start_time = time.time()

# # Run the script
# while (time.time() - start_time) < DURATION:
#     # Calculate the remaining time
#     remaining = DURATION - (time.time() - start_time)

#     # Check if it's time to print the remaining time
#     if (time.time() - start_time) >= INTERVAL:
#         print(f"Remaining time: {int(remaining/60)} minutes")
#         INTERVAL += (5*60)  # Update the interval

#     # Sleep for 1 minute
#     time.sleep(60)

# print("Script has finished running for 51 mins by printing every 5 mins anything.")


#loop for more than 225 mins
# Set the duration to run the script
DURATION = 225 * 60  # 225 minutes in seconds

# Set the interval to print remaining time
# Donot print anything until or > than 10 mins
INTERVAL = 5 * 60  # 5 minutes in seconds

# Get the start time
start_time = time.time()

# Run the script
while (time.time() - start_time) < DURATION:
    # Calculate the remaining time
    remaining = DURATION - (time.time() - start_time)

    # Check if it's time to print the remaining time
    if (time.time() - start_time) >= INTERVAL:
        print(f"Remaining time: {int(remaining/60)} minutes")
        INTERVAL += (5*60)  # Update the interval

    # Sleep for 1 minute
    time.sleep(60)

print("Script has finished running for 225 mins by printing every 5 mins")

