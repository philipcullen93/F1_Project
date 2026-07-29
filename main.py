from api.jolpica import get_current_drivers
import json

def main():
    print("Connecting to Jolpica API")
    
    data = get_current_drivers()

    print("Successfull Connection\n")
    
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()