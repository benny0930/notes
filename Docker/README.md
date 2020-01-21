
docker-compose stop;docker-compose rm;docker-compose up -d;

docker exec -it dr-web /bin/bash
docker exec -it dockerdata_webpack-dev-front /bin/bash
docker exec -it myVue sh


docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
docker images


//创建虚拟机
docker-machine create [OPTIONS] [arg...]

//移除虚拟机
docker-machine rm [OPTIONS] [arg...]

//登录虚拟机
docker-machine ssh [arg...]

//docker客户端配置环境变量
docker-machine env [OPTIONS] [arg...]

//检查机子信息
docker-machine inspect

//查看虚拟机列表
docker-machine ls [OPTIONS] [arg...]

//查看虚拟机状态
docker-machine status [arg...]  //一个虚拟机名称

//启动虚拟机
docker-machine start [arg...]  //一个或多个虚拟机名称

//停止虚拟机
docker-machine stop [arg...]  //一个或多个虚拟机名称

//重启虚拟机
docker-machine restart [arg...]  //一个或多个虚拟机名称


------刪除 Docker Image
Docker 提供了 rmi 參數, 可以用作刪除 images, 但在執行前, 我們需要知道 image id, 先用以下指令找出 image id:

# docker image ls
找到要刪除的 image 的 image id 後, 便可以執行以下指令刪除:

# docker rmi image_id


------查看本地所有的镜像
$ docker images

------查看正在运行的容器
$ docker ps

------查看虚拟机列表
$ docker-machine ls

------停止所有容器
➜  ~ docker ps -a | grep "Exited" | awk '{print $1 }'|xargs docker stop

------删除所有容器
➜  ~ docker ps -a | grep "Exited" | awk '{print $1 }'|xargs docker rm

------删除所有none容器
➜  ~ docker images|grep none|awk '{print $3 }'|xargs docker rmi


------MySQL
从 Dockerhub拉取 MySQL 镜像：

$ docker pull mysql
实例容器,启动数据库

$ docker run -p 3306:3306 --name mysql -v ~/www/mysql/:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d --privileged=true mysql

### 命令说明：
-p 3306:3306：将容器的3306端口映射到主机的3306端口
-v ~/www/mysql/:/var/lib/mysql：将主机当前用户目录下的mysql文件夹挂载到容器的/var/lib/mysql 下，在mysql容器中产生的数据就会保存在本机mysql目录下
-e MYSQL_ROOT_PASSWORD=123456：初始化root用户的密码
-d 后台运行容器
--name 给容器指定别名
--privileged=true  可能会碰到权限问题，需要加参数


------Nginx
从 Dockerhub拉取 Nginx 镜像：


$ docker pull nginx
实例容器,启动Nginx

$ docker run --name nginx -p 80:80 -d nginx


运行成功后，终端会返回容器的ID号，上面的命令中，

run：创建一个新的容器
--name：指定容器的名称（如果留空，docker会自动分配一个名称）
-p：导出容器端口到本地服务器，格式：-p <local-port>:<container-port>。在本例中，我们映射容器的80端口到本地服务器的80端口。
nginx：是 Dockerhub 上下载nginx镜像名称（如果本地没有可用的镜像，Docker会自动下载一个）
-d：后台启动。


关闭指定的虚拟机
$ docker-machine stop default

开启指定的虚拟机
$ docker-machine start default