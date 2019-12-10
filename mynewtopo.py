from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def create_topo():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    #s5 = net.addSwitch('s5')

    info( '*** Creating links\n')
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s2, s4)
    net.addLink(s4, s3)
    #net.addLink(s5, s1)
    info( '*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)


if __name__ == '__main__':
    setLogLevel('info')
    create_topo()
