# This python script automatically replaces all the api tokens in this repo
import os

def err():
    print('Put the api key in the txt file pls')
    os._exit(1)

api_key = None
with open('api-key.txt', 'r') as f:
    try:
        key = f.readlines()[0].strip()
    except:
        err()
    
    if key == "DELETE THIS LINE AND REPLACE IT WITH YOUR API KEY":
        err()
    
    # Find all the .conf files and replace them
    files = [os.path.join(r, fn)
        for r, ds, fs in os.walk(".") 
        for fn in fs if fn.endswith(".conf")]

    for file in files:
        new_file = ""
        with open(file, 'r') as conf_file:
            for line in conf_file:
                line = line.strip('\n')
                if "Bearer" in line:
                    changes = f"    Authorization = \"Bearer {key}\""
                else:
                    changes = line
                new_file += changes + "\n"
        
        with open(file, "w+") as conf_file:
            conf_file.write(new_file)

        print(f'Successfully replaced api key in {file}')
        