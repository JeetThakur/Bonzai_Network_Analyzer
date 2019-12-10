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
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')
    s8 = net.addSwitch('s8')
    s9 = net.addSwitch('s9')
    s12 = net.addSwitch('s12')
    s13 = net.addSwitch('s13')
    s14 = net.addSwitch('s14')
    s15 = net.addSwitch('s15')
    s16 = net.addSwitch('s16')
    s17 = net.addSwitch('s17')
    s18 = net.addSwitch('s18')
    s19 = net.addSwitch('s19')

    info( '*** Creating links\n')
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)
    net.addLink(s1, s5)
    net.addLink(s1, s6)
    net.addLink(s1, s7)
    net.addLink(s1, s8)
    net.addLink(s1, s9)
    net.addLink(s2, s12)
    net.addLink(s2, s13)
    net.addLink(s3, s12)
    net.addLink(s3, s13)
    net.addLink(s4, s14)
    net.addLink(s4, s15)
    net.addLink(s5, s14)
    net.addLink(s5, s15)
    net.addLink(s6, s16)
    net.addLink(s6, s17)
    net.addLink(s7, s16)
    net.addLink(s7, s17)
    net.addLink(s8, s18)
    net.addLink(s8, s19)
    net.addLink(s9, s18)
    net.addLink(s9, s19)
    info( '*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)


if __name__ == '__main__':
    setLogLevel('info')
    create_topo()

