import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
# to save data into json files
#if the filepath does not exist save_data() creates a file

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
#to load data from json files in this case from filepath
#in load_data() if the filepath does not exist, it returns an empty dictionary
        
if(len(sys.argv)) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a Key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print('data saved to clipboard')
        
    elif command == "load":
        key = input("Enter a Key: ")
        if key in data:
            clipboard.copy(data[key])
            print('data copied from clipboard')
        else:
            print('key does not exist')
            
    elif command == "list":
        print(data)     
            
    else:
        print("Unknown Command")
else:
    print("Please pass a command")
    
    






# data = clipboard.paste()
# print(data) # paste the data in clipboard

# clipboard.copy("abc") : copy abc into clipboard

# print(sys.argv[1:]) # to check all the passed commands in the cli


#to delete data from the clipboard
    # elif command == 'delete':
    #     key = input("enter the key to be deleted")
    #     data = load_data(SAVED_DATA)
    #     if key in data:
    #         del(data[key])
    #         save_data(SAVED_DATA, data)
    #         print('dta deleted')
    #     else: 
    #         print('key dont exist')