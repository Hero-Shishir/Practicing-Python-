def main():
    enter = input ("what time is it ? ")
    enter = convert(enter)
    if 7.0 <= enter <= 8.0 :
        print ("breakfast time")
    elif 12.0 <= enter <= 13.0 :
        print ("lunch time")
    elif 18.0 <= enter <= 19.0 :
        print ("dinner time")
    
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    hours = hours * 60
    value = hours + minutes 
    value = value / 60
    return value

main()