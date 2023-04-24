import os
import re

# Set the directory to scan
directory = 'path/to/change/files'

# Define the regex pattern to match .live() events
#pattern = r'\$\(['\"](.+?)['\"]\)\.live\(\s*("[^"]*")\s*,\s*(\w+)\s*\);'
pattern = r"\$\(['\"](.+?)['\"]\)\.live\(\s*['\"](.+?)['\"]\s*,\s*(.*)"
#pattern = r"\$\(['\"](.+?)['\"]\)\.(?:live|bind)\(\s*['\"](.+?)['\"]\s*,\s*(\w+)\s*\)|\$\(['\"](.+?)['\"]\)\.on\(\s*['\"](.+?)['\"]\s*,\s*(\w+)\s*\)"

#pattern = r'\$\(("[^"]*")\)\.live\(\s*("[^"]*")\s*,\s*(\w+)\s*\);'
#pattern2 = r'\$\(("[^"]*")\)\.live\(\s*("[^"]*")\s*,\s*(\w+)\s*\(\)\s*\{'

#pattern2 = r'\$\(("[^"]*")\)\.live\(\s*("[^"]*")\s*,\s*(\w+)\s*\(\)\{'

# Define the replacement string with the selector parameter
replacement = r'$(document).on("\2", "\1", \3'
#replacement2 = r'$(document).on(\2, \1, \3{'


# Recursively scan the directory for .aspx and .js files
for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(subdir, file)
        if filepath.endswith('.aspx') or filepath.endswith('.js'):
            # Open the file and read its contents
            with open(filepath, 'r') as f:
                content = f.read()
                # Replace all instances of .live() with $(document).on() using the selector parameter
                new_content = re.sub(pattern, replacement, content)
                #new_content = re.sub(pattern, replacement2, content)
            # Write the new contents back to the file
            with open(filepath, 'w') as f:
                f.write(new_content)
