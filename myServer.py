import socket, optparse

# 解析命令行
parser = optparse.OptionParser()
parser.add_option('-i', dest='ip', default='')
parser.add_option('-p', dest='port', type='int', default=12345)
(options, args) = parser.parse_args()

# sokect绑定ip 端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (options.ip, options.port) )

# 传来的数据写入文件中
f = open('foo.txt','w')
while True:
  data, addr = s.recvfrom(512)  # 接受数据
  f.write("%s: %s\n" % (addr, data))
  f.flush()