import cv2
import os
import shutil
# main
def main():

    data_file = open('./excel.csv', 'rt', encoding="utf-8")
    user_data = file_read(data_file)
    excel_write = ''
    dog_number = 1


    for i in range(len(user_data)):
        cv2_image = cv2.imread("./images/" + str(i) + ".jpg",cv2.IMREAD_UNCHANGED) 
        cv2_image2 = cv2.resize(cv2_image, (360, 480))
        cv2.imshow("unnamed",cv2_image2)
        x = cv2.waitKey(0)
        if x == 48:
            break
        if x == 49:
            excel_write += str(dog_number) + "," 
            for j in range(11):
                excel_write += str(user_data[i][j]) + ","
            excel_write += str(user_data[i][11]) + "\n"
            image = "./images/" + str(i) + ".jpg"
            image_newname = "./images_check/" + str(dog_number) + ".jpg"
            os.rename(image,image_newname)
            dog_number += 1

    data_file2 = open('./result.csv', 'wt', encoding="utf-8")
    data_file2.write(excel_write)


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

