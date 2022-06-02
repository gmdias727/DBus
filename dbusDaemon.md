# DBUS Daemon

dbus-daemon is the D-Bus message bus daemon.

dbus-daemon is an application that uses this library to implement a message bus daemon.

Multiple programs connect to the message bus daemon and can exchange messages with one another.

There are two standard message bus instances: the systemwide message bus and the per-user-login-session message bus

dbus-daemon is used for both of these instances, but with a different configuration file.

### CADA INSTÂNCIA POSSUI SEU ARQUIVO DE CONFIGURAÇÃO

The --session option is equivalent to "--config-file=/usr/local/share/dbus-1/session.conf"

the --system option is equivalent to "--config-file=/usr/local/share/dbus-1/system.conf"

### É POSSÍVEL CRIAR UMA INSTÂNCIA CUSTOMIZADA TAMBÉM

By creating additional configuration files and using the --config-file option, additional special-purpose message bus daemons could be created.

The systemwide daemon is normally launched by an init script, standardly called simply "messagebus".

The systemwide daemon is largely used for broadcasting system events, such as changes to the printer queue, or adding/removing devices.

The per-session daemon is used for various interprocess communication among desktop applications

# CONFIGURATION FILE
A message bus daemon has a configuration file that specializes it for a particular application.
For example, one configuration file might set up the message bus to be a systemwide message bus, while another might set it up to be a per-user-login-session bus.
The configuration file also establishes resource limits, security parameters, and so forth.

AMBOS ARQUIVOS DE CONFIGURAÇÃO NORMALMENTE LEÊM ARQUIVOS .XML

**EXPLICAR O ARQUIVO DE CONFIGURAÇÃO FEITO EM PYTHON AQUI**


**integração com serviço de sessão e sistema feito em python**



