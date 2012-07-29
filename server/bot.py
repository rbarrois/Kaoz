#!/usr/bin/python
# -*- coding: utf-8 -*-

#This file is a part of Kaoz, a free irc notifier
#Copyright © Binet Réseau, see the licence file for more informations
from twisted.internet.protocol import ServerFactory, ReconnectingClientFactory
from twisted.application.internet import TCPServer, SSLServer, TCPClient, SSLClient
from twisted.application.service import Application
from twisted.internet.ssl import ClientContextFactory, DefaultOpenSSLContextFactory

from publishbot import Listener, Publisher
import config

application = Application("Kaoz Irc-Notifier")

sf = ServerFactory()
sf.protocol = Listener

cf = ReconnectingClientFactory()
cf.protocol = Publisher
cf.queued = []
cf.connection = None

sf.publisher = cf

if config.LISTENER_SSL:
    SSLServer(config.LISTENER_PORT, sf, DefaultOpenSSLContextFactory(config.LISTENER_PEM, config.LISTENER_PEM)).setServiceParent(application)
else:
    TCPServer(config.LISTENER_PORT, sf).setServiceParent(application)
if config.SSL_IRC:
    ircservice = SSLClient(config.IRC_SERVER, config.IRC_PORT, cf,
                           ClientContextFactory())
else:
    ircservice = TCPClient(config.IRC_SERVER, config.IRC_PORT, cf)

ircservice.setServiceParent(application)
