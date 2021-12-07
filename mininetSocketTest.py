from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI

def main():
    lg.setLogLevel('info')
    # net网络
    net = Mininet(SingleSwitchTopo(k=2))
    net.start()

    # 打开服务器myServer.py,绑定ip 端口
    h1 = net.get('h1')
    p1 = h1.popen('python myServer.py -i %s &' % h1.IP())

    # 运行客户端myClient.py,向指定ip 端口发送数据
    h2 = net.get('h2')
    h2.cmd('python myClient.py -i %s -m "hello world"' % h1.IP())

    # 打开mininet终端
    CLI( net )
    p1.terminate()
    net.stop()

if __name__ == '__main__':
    main()