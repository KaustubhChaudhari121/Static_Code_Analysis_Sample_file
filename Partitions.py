import os
print('''
press e : Increase size of partition
press d : Decrease size of partition
press c : create partition
press v : display  vg
press p : display pv
press l : display lv
''')
choice = input("Enter your choice : ")
hd1 = input("Name of Hard disk 1(eg : /dev/sdc) : ")
hd2 = input("Name of Hard disk 2(eg : /dev/sdd) : ")
vg_name = input("Enter the virtual group name : ")
lv_name = input("Enter LVM Partition name : ")

if choice=='c':
        size = input("Enter size of partition(K,M,G): ")
        dir_name= input("Enter directory name to mount partition : ")
        os.system('pvcreate {}'.format(hd1))
        os.system('pvcreate {}'.format(hd2))
        os.system('vgcreate {} {} {}'.format(vg_name , hd1 , hd2))
        os.system('lvcreate --size {} --name {} {}'.format(size , lv_name , vg_name))
        os.system('mkfs.ext4 /dev/{}/{}'.format(vg_name , lv_name))
        os.system('mkdir /{}'.format(dir_name))
        os.system('mount /dev/{}/{} /{}'.format(vg_name , lv_name , dir_name))
elif choice=='e':
        s = input("Enter size to be increased(K,M,G) : ")
        os.system('lvextend --size +{} /dev/{}/{}'.format(s , vg_name , lv_name))
        os.system('resize2fs /dev/{}/{}'.format(vg_name , lv_name))
elif choice=='v':
        os.system('vgdisplay {}'.format(vg_name))
elif choice=='p':
        name = input("Enter name of pv : ")
        os.system('pvdisplay {}'.format(name))
elif choice=='l':
        os.system('lvdisplay {}'.format(lv_name))
elif choice=='d':
        s = input("Enter size to be reduced(K,M,G) : ")
        os.system('umount /data')
Pull the Github repo.....
