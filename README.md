# Everything Remote

一个用来解决PC和Mac之间的远程搜索的小脚本.

## 安装

### PC端

在*PC*端安装*Everything*, 并在*Everything*上开启*HTTP*服务, *HTTP*服务可以提供认证方式. 同时在PC上运行Server端的*everything\_server.py*.

其中*everything\_server.py*中的ip地址需要修改自己的内网IP地址. 端口号也可以修改为自己想要的端口号. 只要保证同*Mac*端的一致即可.

### Mac端

在*Mac*端安装*Afred*, 使用*workflow*.

其中*everything_query.py*中的ip地址修改为PC的IP地址, 端口号修改为*Everything*提供*HTTP*服务的端口号, user/pwd都修改为*Everything*开启的用户名和密码

*everything_remote_open.py*中的ip地址修改PC的IP地址, 端口号保持同 *PC* 端的*everything_server.py*一致即可.

## 操作说明

*Mac*端使用*Afred*关键字*er*进行*PC*端的文件搜索, 搜索后, 选中文件将在*PC*端打开该文件.

