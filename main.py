from api.jolpica import get_current_drivers

def main():
    print("Connecting to Jolpica API")
    
    data = get_current_drivers()

    print("Successfull Connection")
    print(data)

if __name__ == "__main__":
    main()