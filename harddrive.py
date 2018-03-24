'''
    Copies files from n source directories into a destination ignoring files with equal names and file sizes (unmodified)
'''

import shutil
import os
import settings as settings

REPORT_FILE_DOES_NOT_EXIST = "File {} does not exist - copying to destination"
REPORT_FILE_SIZE_NOT_EQUAL = "File {} exists and but files sizes are not equal - copying to destination"
REPORT_FILE_SIZE_EQUAL = "File {} exists and files sizes are equal - not copying"

# list of source directories to copy files from
sources = settings.SOURCES

# location to place files
destination_directory = settings.DESTINATION

''' local scope methods '''

def are_file_sizes_equal(source_file, destination_file):
    
    # get source file size
    source_file_size = os.path.getsize(source_file)

    # get destination file size
    destination_file_size = os.path.getsize(destination_file)

    return source_file_size == destination_file_size

def copy_file(source_file, destination_file, destination_location):

    # if file exists in destination
    if os.path.isfile(destination_file):

        # are file sizes equals
        file_sizes_are_equal = are_file_sizes_equal(source_file, destination_file)

        # if our source file size is equal to our destination file size - do nothing - continue to the next file
        if file_sizes_are_equal:

            # log
            print REPORT_FILE_SIZE_EQUAL.format(destination_file)

            # skip to next source file
            return

        # if our source size is not equal to our destination size update the file
        else:

            # log
            print REPORT_FILE_SIZE_NOT_EQUAL.format(destination_file)

            # copy file
            shutil.copy(source_file, destination_directory)
    
    # the file does not exist so copy it
    else:

        # log
        print REPORT_FILE_DOES_NOT_EXIST.format(destination_file)

        # copy
        shutil.copy(source_file, destination_directory)

def copy_files_from_source_to_dest(source_directory, destination_directory):
    
    # get all files from this directory ['...', '...', ...]
    files = os.listdir(source_directory)
    
    # for every file
    for file in files:

        # our source file
        source_file = source_directory + "\\" + file

        # our destination file
        destination_file = destination_directory + "\\" + file

        # ensure this is a file - otherwise skip it
        if os.path.isfile(source_file):
            # copy file
            copy_file(source_file, destination_file, destination_directory)


# for each source directory we want to copy files from
for source_directory in sources:
    copy_files_from_source_to_dest(source_directory, destination_directory)
