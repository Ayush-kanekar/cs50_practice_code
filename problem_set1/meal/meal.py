def main():
    time_str = input("What time is it ? ")
    time = convert(time_str)
    if 7.0 <= time < 8.0:
        print("breakfast time")
    elif 12.0 <= time < 13.01:
        print("lunch time")
    elif 18.0 <= time < 19.0:
        print("dinner time")

def convert(time):
    hours ,minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = hours + minutes /60.0
    return  time
if __name__ == "__main__":
    main()
