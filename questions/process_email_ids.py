# 28. Write a program to read email IDs of n number of students and store
# them in a tuple. Create two new tuples, one to store only the usernames
# from the email IDs and second to store domain names from the email IDs.
# Print all three tuples at the end of the program. Use the function split()


def process_email_ids(emails):
    usernames = tuple(email.split('@')[0] for email in emails)
    domains = tuple(email.split('@')[1] for email in emails)
    return usernames, domains


email_list = ["shivansh@gmail.com", "shiva@google.com", "shiv@yahoo.com"]
usernames_tuple, domains_tuple = process_email_ids(email_list)

print("Emails:", email_list)
print("Usernames:", usernames_tuple)
print("Domains:", domains_tuple)
