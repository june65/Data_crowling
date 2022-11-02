import ssl
import urllib.request

# main
def main():

    data_file = open('./excel.csv', 'r')
    user_data = file_read(data_file)
    for i in range(len(user_data)):
        image = user_data[i][9]
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(image, "./images/" + str(i) + ".jpg")

# file_read  
def file_read(file):
    print("start file_read")

    user_info_list=[]
    line = file.read().split('\n')
    for i in range(0, len(line) - 1):

        #user_info = [user_id, user_name, dog_name, dog_gender, dog_weight, dog_date, dog_link, dog_chest, dog_neck, dog_back, dog_leg, dog_age]
        user_info = line[i].split(',')
        user_info.insert(0, i)
        user_info_list.append(user_info)

    print("successfully file_read")

    return user_info_list  

if __name__ == '__main__':
    main()

