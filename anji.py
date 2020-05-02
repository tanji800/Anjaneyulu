
import os
os.system('clear')

print('''
-------------------------------------------------------------------------------
 #######   ########  ########  ########   ##   ##      IIEC RISE Project Docker           
 ##   ##      ##        ##        ##      ##  ##                 - anji
 ##   ##      ##        ##        ##      ## ##
 #######      ##        ##        ##      ####
 ##   ##      ##        ##        ##      ## ##
 ##    ##     ##        ##        ##      ##  ## 
 ##     ## ########     ##     ########   ##   ##
-------------------------------------------------------------------------------''') 
def about():
       print(''' anji
                 #IIEC RISE community #Righteducation #Vimaldaga
                 if you want you can learn Docker tool @youtube search in youtube IIEC_Connect 
                 Engineering college bikaner
                 if you are facing any issu in this program then mail me
                 E- mail :- t.anji800@gmail.com''')
       final()
def titlebar():
        print('-'*79)
        print('\t\t\t Make your life easy \n\t\t\t\t\t\t -anji' )
        print('-'*79)
        print('1.Docker   2.Docker Images   3.Docker Container   4.Docker volume    5.Web server   6.About')
def exit1() :
        exit()
def images_docker() :
        os.system('docker  images')
        final()
def running_container() :
        os.system('docker container ps')
        final()
def all_docker_id() :
        os.system('docker container ps -a ')
        final()
def os_new_start() :
        image = input('which os you want to start : ')
        name = input('give a name to your os : ')
        os.system('docker container run -dit --name {0} {1}'.format(name,image))
        final()
def attach_container() :
        image = input('which os you want to attach : ')
        os.system('docker container attach {0} '.format(image))
        final()
def start_container() :
        image = input('which container you want to  start  : ')
        os.system('docker container start {0} '.format(image))
        final()
def remove_container():
        name = input('which container you want to remove : ')
        conf = input('Aren you sure[yes/no] : ')
        conf=conf.lower()
        if conf == 'yes':
            os.system('docker container rm {}'.format(name))
        final()
def confi_docker_yum() :
        os.system(""" echo '''
[docker-cccccccccccc]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
[docker-ce]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/Packages/
gpgcheck=0'''  >>  /etc/yum.repos.d/hello_created_by_python.repo""" )
        final()
def install_docker() :
        os.system('yum  install docker-ce --nobest')
        final()
def info_docker() :
        os.system('docker info')
        final()
def create_image() :
        name = input("Which container's image you want to create : ")
        image = input(" Give a name to your new image : ")
        imageVer = input('Enter version : ')
        os.system('docker commit {0} {1}:{2} '.format(name,image,imageVer))
        final()
def detail_container() :
        name = input('which container details you want : ')
        os.system('docker container inspect {0} ' .format(name))
        final()
def ip_container(name) :
        if name == '':
             name = input(' Which container IPadress you want : ')
        else:
             value = '"{{.NetworkSettings.IPAddress}}"'
             os.system('echo {0} IPAddress : ` docker container inspect --format {1} {0}` '.format(name,value))
        final()
def cmd_run() :
        name = input('Choose your Container : ')
        while True :
            cmd = input('Enter 0 to exit or enter command : ')
            if cmd == '0' :
                break
            else :
                os.system('docker container exec {0} {1}'.format(name,cmd))
        final()
def stop_container() :
        name = input('Which container you want to stop : ')
        os.system('docker container stop {} '.format(name))
        final()
def detail_vol() :
        volume_inspect = input('Enter your volume name : ')
        os.system('docker volume inspect {0}'.format(volume_inspect))
        final()
def create_vol() :
        vol_name = input('Give a name to volume : ')
        os.system('docker volume create {0}'.format(vol_name))
        final()
def del_vol() :
        vol= input('Which volume you want to delete : ')
        confirm = input("This action can't be reversed really want to delete [y/n] : ")
        if confirm == 'y' :
            os.system('docker volume rm {0}'.format(vol))
            final()
        else :
            print('Operation cancelled ' )
            final()
def list_vol() :
        os.system('docker volume ls')
        final()
def wordpress():
    os.system('yum install mysql')
    os.system('docker pull mysql:5.7')
    os.system('docker pull wordpress:5.1.1.-php7.3-apache')
    os.system('docker run -dit -e MYSQL_ROOT_PASSWORD=anji -e MYSQL_USER=anji -e MYSQL_PASSWORD=anji -e MYSQL_DATABASE=my_database mysql:5.7')
    os.system(''' echo """

version: '3'
services:
        data_base_os:
                image: mysql:5.7
                volumes:
                        - mysql_storage:/var/lib/mysql
                restart: always
                environment:
                        MYSQL_ROOT_PASSWORD: anji
                        MYSQL_USER: anji
                        MYSQL_PASSWORD: anji
                        MYSQL_DATABASE: my_database



        wordpress_OS:
                image: wordpress:5.1.1-php7.3-apache
                restart: always
                depends_on:
                        - data_base_os

                ports:
                        -  8081:80
                environment:
                        WORDPRESS_DB_HOST: data_base_os
                        WORDPRESS_DB_USER: anji
                        WORDPRESS_DB_PASSWORD: anji
                        WORDPRESS_DB_NAME: my_database
                volumes:
                        - wp_storage:/var/www/html

volumes:
          wp_storage:
          mysql_storage:   """  > docker-compose.yml ''')
    x=os.system('docker-compose up')
    if x != 0:
       compose_install()
       os.system('docker-compose up')
def invalid_option()  :
        print('error : option not supported ')
        final()
def copy(x):
    if x== 1:
       container = input('Container id or name : ')
       print('ex :- /root/webpage/webpage.html ') 
       path = input('path of your webpage file : ')
       os.system('docker cp {0} {1}:/var/www/html/'.format(path,container))
    else :
        path = input('Enter file path : ')
        container = input('Enter container id or name  ; ')
        path2 = input('File destination in container (default /root/) : ')
        if path2 == '':
            path2 = '/root/'
        os.system('docker cp {0} {1}:{2}'.format(path,container,path2))
        print('file succesfully copied in @{0}:{1}'.format(container,path2))
def final() :
    input('Press Enter to continue ..........')
    os.system('clear')
    titlebar()
def httpd():
    y1=0
    os.system('docker images')
    image = input('In which os you want  to configure Webserver : ')
    name =  input('Give a name to your  webserver os : ')
    os.system('netstat -nptl')
    port =eval(input('select a port which is not usable by host : '))
    service = input('enter your service port default:80  : ')
    if service == '':
        service = 80
    os.system('docker volume ls')
    vol = input('Volume name  : ')
    check = os.system('docker volume inspect {0} >> cachfile'.format(vol))
    if check != 0:
         os.system('docker volume create {0}'.format(vol))
    x= os.system('docker container run  -dit --name {0} -p {3}:{4} -v {1}:/var/www/html {2}'.format(name,vol,image,port,service))
    httpdcheck = os.system('docker container exec {} rpm -q httpd'.format(name))
    if httpdcheck !=0 :
        y1=os.system('docker container exec {0} yum install httpd -y'.format(name))
    if x == 0 and y1 == 0 :
        os.system('docker container exec {0} /usr/sbin/httpd '.format(name))
        print('congratulation ! webserver configured successfully')
    else :
        print('Webserver not configured')
    final()
def download_image():
    image = input('Which os you want to download : ')
    os.system('docker pull {0}'.format(image))
def disable_firewall():
    os.system('systemctl disable firewalld ')
    os.system('systemctl stop firewalld')
    print('firewall  has been disabled')
def image_create(name,img):
    x=1
    if img == '':
        img = input('Which image you want to use : ')
        x=0
    if name =='':
        name  = input('Give a name : ')
    os.system('docker container run -dit --name {0} {1} '.format(name,img))
    os.system('docker container exec {0} yum install httpd -y'.format(name))
    os.system('docker container stop {0}'.format(name))
    os.system('docker commit {0} {0}'.format(name))
    os.system('docker images')
    if x == 1:
        os.system('docker container rm -f {0}'.format(name))
def httpd_configure_always():
    os.system('docker images')
    image= input('Enter a os name :  ')
    name = input('Give a name to this container : ')
    os.system('docker container run  -dit --name  anji707054   {0}'.format(image))
    check_httpd_installed_or_not=os.system('docker container exec anji707054 rpm -q httpd')
    os.system('docker container rm -f anji707054')
    if check_httpd_installed_or_not != 0 :
        image_create(name,image)
        image = name
    os.system('docker volume ls ')
    vol = input('Enter volume name which you want attach this file : ')
    print('If your choice is docker than you can access your site only to this operating system ')
    choice = input('Which IP you want use as a server webserver adress[base/docker] : ')
    x=3
    if choice == 'base':
    	os.system('netstat -nptl')
    	port1 = input('Enter a port no which is free : ')
    	x=os.system('docker container run -dit --name {0} -v {1}:/var/www/html/  -p {2}:80 {3}'.format(name,vol,port1,image))
    	os.system('wait $!')
    elif choice == 'docker':
        x=os.system('docker container run -dit --name {0} -v {1}:/var/www/html/   {2}'.format(name,vol,image))
        os.system('wait $!')
    else :
       print('option not valid')
    if x == 0:
        os.system('''echo """
import os
os.system( 'echo rm -r -f /var/run/httpd/* >> /root/.bashrc')
os.system( 'echo /usr/sbin/httpd  >> /root/.bashrc')
        """ > prem123.py ''')
        os.system('echo docker container start {0} >> /root/.bashrc'.format(name))
        os.system('wait $!')
        python_check=os.system('docker exec {0} rpm -q python36'.format(name))
        if python_check != 0:
              os.system('docker exec {0} dnf install python3 -y'.format(name))
        os.system('wait $!')
        os.system('docker cp anji123.py {}:/root/anji123.py '.format(name))
        os.system('wait $!')
        os.system('docker exec {0} /usr/sbin/httpd'.format(name))
        os.system('wait $!')
        os.system('docker exec {0} python /root/anji123.py'.format(name))
        os.system('wait $!')
        if choice == 'docker':
            ip_container(name)
        else:
            print('If you trying to access this site from phone than your laptop and phone is connected to same network')
            os.system('echo """Enter this IP in your browse with port no : {0} `ifconfig enp0s3 | grep "inet 192."`"""'.format(port1))
    final()
def compose_install():
	os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
	os.system('chmod +x /usr/local/bin/docker-compose')
	os.system('docker-compose version')
	final()
def removeallcontainer():
	print('Not recommanded ')
	con=input('Are you sure you want to delete all container[y/n] : ') 
	if con == 'y':
		os.system('docker container rm -f $(docker container ps -a -q)')
		os.system('docker container ps -a ; echo done')
	else:
		print('Operation cancelled ')
	final()
def tar():
	image=input('Which image you want to save as a tar file : ')
	name=input('Give a name to your file : ')
	print('please wait .........')
	os.system('docker save  {0}  -o /root/{1}.tar'.format(image,name))
	print('your file is saved @/root/ ')
	final()
def delete_image():
        os.system('docker images ')
        image=input('Which image you want to delete : ')
        con= input('Are you sure ? you want to delete[y/n] : ')
        if con == 'y':
           os.system('docker rmi {0}.'.format(image))
           os.system('docker images ')
        else :
           print('Operation is cancelled ')
        final()
def load():
	imgsrc=input("tar file location : ")
	print('Please wait ...........')
	os.system("docker load -a {}".format(imgsrc))
	final()
def upload():
        print('If you don have a account on docker hub then first create')
        select=input('Select Which image you want to upload in docker hub : ')
        if '/' not in select :
          print('you need to rename your image like :  anji/webserver:v1')
          upload = input('New name : ')
        os.system('docker login ')
        os.system('docker push {0}'.format(upload))
start = 0
while True:
    if start == 0 :
       titlebar()   
    menu = input('Chose your menu : ')
    if menu == '1' :
        final()
        while True :
            print('''
            Press 0  : Main menu                
            Press 1  : Configure yum/dnf to download docker
            Press 2  : Install Docker Tool in your PC
            Press 3  : about Docker''') 
            ch = input('Enter your option : ')
            if ch == '0' :
                os.system('clear')
                break
            elif ch == '1' :
                confi_docker_yum()
            elif ch == '2' :
                install_docker()
            elif ch == '3' :
                info_docker()
            else:
                invalid_option()
    elif menu == '2':
        final()
        while True :      #images menu create_image() 
            print('''
            Press 0  : Main menu
            Press 1  : Show all Docker  Images
            Press 2  : Create  Docker images from container
            Press 3  : Download Docker images
            Press 4  : Save image in tar file
            Press 5  : Delete Docker image
            Press 6  : Load docker image locally
            Press 7  : Upload image on docker hub ''')
            ch = input('Enter your option : ')
            if ch == '0' :
                os.system('clear')
                break
            elif ch == '1' :
                images_docker() 
            elif ch == '2' :
                create_image() 
            elif ch == '3':
                download_image()
            elif ch == '4':
                tar()
            elif ch == '5':
                delete_image()
            elif ch == '6':
                load()
            elif ch == '7':
               upload()
            else:
                invalid_option()
    elif menu == '3' :
        final()
        while True :#container menu
            print('''
            Press 0  : Main menu
            Press 1  : Show how much  Docker container are running currently
            Press 2  : Show all Docker containers (Stopped and Running)
            Press 3  : Start a new container
            Press 4  : Start a existing Container
            Press 5  : Attach os to terminal 
            Press 6  : Run commands in container
            Press 7  : Check IPadress of container
            Press 8  : Stop Container
            Press 9  : Remove containers
            Press 10 : Copy somthing in container from base
            Press 11 : Delete all container
                ''') 
            ch = input('Enter your option : ')
            if ch == '0' :
                break
                os.system('clear')
            elif ch == '9' :
                remove_container()
            elif ch == '1' :
                running_container()
            elif ch == '2':
                all_docker_id()
            elif ch == '3' :
                os_new_start()
            elif ch == '5':
                attach_container()
            elif ch=='4':
                start_container()
            elif ch == '6':
                cmd_run()   
            elif ch == '7' :
                ip_container('')
            elif ch == '8' :
                stop_container()
            elif ch == '10':
                copy(4)
            elif ch == '11':
                removeallcontainer()
            else:
                invalid_option()
    elif menu == '4' :
        final()
        while True :#volume menu
            print('''
            Press 0  : Main menu
            Press 1 : List of docker volumes
            Press 2 : Check docker volume detail
            Press 3 : Create Docker Volume 
            Press 4 : Delete a volume
        ''')
            ch = input('Enter your option : ')
            if ch == '0' :
                os.system('clear')
                break
            elif ch == '2' :
                detail_vol() 
            elif ch == '3' :
                create_vol() 
            elif ch == '4' :
                del_vol()
            elif ch == '1' :
                list_vol()
            else:
                invalid_option()

    elif menu == '5':
        final()
        while True:
            print('''
            \t Use only redhat or centos images otherwise might be possibe failure\n 
        Press 0: Main  menu
        Press 1: Configure Appache web server for temporary
        Press 2: Configure Wordpress web server
        Press 3: Install Docker-compose 
        Press 4: create a image of your weserver os
        Press 5: Setup your webpage in container
        Press 6: Configure a appache webserver which always run on startup
        Press 7: Some port you cant select like 1234 to select these type of port disable Selinux security for this press 8 ''')
            ch = input("Enter your option : ")
            if ch == '0':
                 os.system('clear')
                 break 
            elif ch == '1':
                 disable_firewall()
                 httpd()
            elif ch == '2':
                 disable_firewall()
                 wordpress()
            elif ch == '3':
                 compose_install()
            elif ch =='4':
                 create_image()
            elif  ch == '5':
                 copy(1)
            elif ch =='6':
                 httpd_configure_always()
                 disable_firewall()
            elif ch == '7':
                 os.system('setenforce 0')          
            else:
                invalid_option()
    elif menu == '0':
        exit1()
    elif menu == '6':
         os.system('clear')
         titlebar()
         about()
         os.system('clear')
    else :
        invalid_option()
