#src = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc2.txt", "r")


try:
    #src = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc.txt", "r")
    src = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc2.txt", "r")
    print('File is open!')
except Exception as E:
    print('File not found!')
    print(E)
finally:
    print('Thank you!')



#except FileNotFoundError or ZeroDivisionError:


except FileNotFoundError:
    
except ZeroDivisionError:

except:

    
