import os
import re

if __name__ == "__main__":
    os.system("sudo docker image ls > img_list.txt")
    os.system("sudo docker ps --filter \"status=exited\" > container_list.txt")
    f_images = open("img_list.txt", "r")
    f_cont = open("container_list.txt", "r")
    cont_cmd = "sudo docker rm "
    img_cmd = "sudo docker rmi "
    img_set = set()
    idx = 0
    lines = f_images.readlines()
    for l in lines:
        if idx != 0:
            split = my_list = re.split("\s{2,}", l)
            if split[0] == "<none>" and split[1] == "<none>":
                img_set.add(split[2])
                img_cmd += split[2] + " "
        idx += 1
    idx = 0
    lines = f_cont.readlines()
    for l in lines:
        if idx != 0:
            split = my_list = re.split("\s{2,}", l)
            if split[1] in img_set:
                cont_cmd += split[0] + " "
        idx += 1
    os.system(cont_cmd)
    os.system(img_cmd)

    
    
    
    os.system("rm *.txt")
    
