# Our filesystem, where keys are directories and values are lists containing subdirectory dict, dir size, and file names respectively
fs = {"/":[{}, 0]}
# Our current working directory, with the length representing the depth and each element excluding root is a string of each level's dir
wd = []

"""Recursively updates a given filesystem with files and directories

Parameters
----------
dirs : list
    The current directory being checked
fsPart : dict
    The portion of the filesystem being checked
size: int, optional
    The size of the file to add (default is 0)
file: str, optional
    The name of the file to add (default is None)

Returns
-------
fileUndiscovered
    Whether or not the file had not already been added to the working directory
"""
def recurseFileSystem(dirs: list, fsPart: dict, size: int = 0, file: str = None):
    fileUndiscovered = False
    # Our base case is when we run out of directories to traverse
    # This will also immediately return if the root directory is given
    if not len(dirs):
        return fileUndiscovered
    # If the directory doesn't exist, add it and default it to empty with no files
    if dirs[0] not in fsPart:
        fsPart[dirs[0]] = [{}, 0]
    # Recurse to next level, removing the first directory in the list and providing the subdirectory
    fileUndiscovered = recurseFileSystem(dirs[1:], fsPart[dirs[0]][0], size, file)
    # If there's a file to add and we haven't added it already
    if file and not fsPart[dirs[0]].count(file):
        # Making sure to only add the file to the directory it belongs in
        if len(dirs) == 1:
            fsPart[dirs[0]].append(file)
            # Mark the file as undiscovered
            fileUndiscovered = True
        # Add the file size to the file's directory and all parent directories
        fsPart[dirs[0]][1] += size
    return fileUndiscovered

"""Recursively determines the total size of good candidate directories to delete, as well as collect the directories with at least as much size as needed

Parameters
----------
fsPart : dict
    The portion of the filesystem being checked
candidates: dict
    A dictionary of best candidate directories and their sizes
spaceNeeded: int
    How large a directory needs to be to be added to candidates

Returns
-------
size
    The total size of good candidate directories
"""
def totalCandidateSize(fsPart: dict, candidates: dict, spaceNeeded: int):
    # Local directory size
    size = 0
    for dir, contents in fsPart.items():
        # If the directory is at most 100000, it's a good candidate, add to the size counter
        if contents[1] <= 100000:
            size += contents[1]
        # If the directory is at least the size needed, add it and its size to the best candidates
        if contents[1] >= spaceNeeded:
            candidates[contents[1]] = dir
        # Recursively add the size of the subdirectory
        size += totalCandidateSize(contents[0], candidates, spaceNeeded)
    return size

with open("input.txt") as f:
    while True:
        line = f.readline().strip()
        # Read until EOF
        if not line:
            break
        # Break lines into each word
        result = line.split(" ")
        # Commands start with $
        if line.startswith("$"):
            # We only care about cd, we can ignore ls
            if result[1] == "cd":
                # If it's the root folder, empty the working directory
                if result[2] == "/":
                    wd = []
                # If we're backing out a directory, remove the last directory from the working directory
                elif result[2] == "..":
                    wd.pop()
                # Otherwise, add subdirectory to the working directory
                else:
                    wd.append(result[2])
                # Recursively update our filesystem to include any newly discovered directories
                recurseFileSystem(wd, fs["/"][0])
        # If the line starts with dir then we need to update the filesystem in case it's undiscovered
        elif result[0] == "dir":
            recurseFileSystem([*wd, result[1]], fs["/"][0])
        # Otherwise we attempt to add a file to the current working directory
        else:
            # If we're in the root directory and this file wasn't already added, we need to add it here
            if not len(wd) and not fs["/"].count(result[1]):
                fs["/"].append(result[1])
            # Due to our recursion function base case, we need to add the file size here
            # But we need to make sure that the file wasn't already added before
            if recurseFileSystem(wd, fs["/"][0], int(result[0]), result[1]):
                fs["/"][1] += int(result[0])


candidates = {}
# The minimum size we need to free up is the minimum size needed minus the total device size minus the root directory size
spaceNeeded = 30000000 - (70000000 - fs["/"][1])
print(f"Total directory candidate size: {totalCandidateSize(fs, candidates, spaceNeeded)}")
# Use min() to find the smallest qualifying directory in candidates to get the best directory
print(f"Best candidate directory: {candidates[min(candidates.keys())]} at size {min(candidates.keys())}")
