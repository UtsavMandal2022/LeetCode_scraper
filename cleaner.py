#this is to clean the yielded file of any extra links like solution

#Utsav Mandal

#this code filters out lines that contain a specific substring and creates a new list with the remaining lines
def filter_substring(location,substring):
# Read the contents of the file
    with open(location, 'r') as file:
        lines = file.readlines()

    # Filter out lines containing the substring
    filtered_lines = [line for line in lines if substring not in line]

    # Write the filtered lines to a new file
    with open('output_filtered.txt', 'w') as file:
        file.writelines(filtered_lines)


substring = '/solution'  # Links with substring to be removed
filter_substring('output_lc.txt',substring)