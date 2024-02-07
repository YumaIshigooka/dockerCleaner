import os
import re

if __name__ == "__main__":
    # List all the Images and Exited Containers.
    os.system("sudo docker image ls > img_list.txt")
    os.system("sudo docker ps --filter \"status=exited\" > container_list.txt")
    f_images = open("img_list.txt", "r")
    f_cont = open("container_list.txt", "r")

    # The final commands
    cont_cmd = "sudo docker rm "
    img_cmd = "sudo docker rmi "

    # To only remove containers listed on the image list.
    img_set = set()
    idx = 0

    # Archive the images into the set, and build the rmi command
    lines = f_images.readlines()
    for l in lines:
        if idx != 0:
            split = my_list = re.split("\s{2,}", l)
            if split[0] == "<none>" and split[1] == "<none>":
                img_set.add(split[2])
                img_cmd += split[2] + " "
        idx += 1
    idx = 0

    # Build the rm command for the containers. 
    # If the image referenced by the container is listed in the to delete set, delete the container.
    lines = f_cont.readlines()
    for l in lines:
        if idx != 0:
            split = my_list = re.split("\s{2,}", l)
            if split[1] in img_set:
                cont_cmd += split[0] + " "
        idx += 1
    
    # Run the containers.
    os.system(cont_cmd)
    os.system(img_cmd)

    # Remove the files.    
    os.system("rm *.txt")
    
