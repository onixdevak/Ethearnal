import os
# temporaly disable until find solution for windows
# import miniupnpc


def kwargs(**kwa):
    return kwa


def _mkdir(newdir):
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("The same name file as the desired "
                      "directory, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            _mkdir(head)

        if tail:
            os.mkdir(newdir)


def mkdir(newdir):
    _mkdir(newdir)


def mkd(newdir):
    abspath = os.path.abspath(newdir)
    _mkdir(abspath)
    return abspath


def upnp_map_port(local_port, nat_router_port, proto):
    # todo failed to install on windows
    import miniupnpc
    protos = ('TCP', 'UDP')
    if proto not in protos:
        raise ValueError('Protocol should be one %s or %s' % protos)
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 10
    upnp.discover()
    upnp.selectigd()
    description = 'Ethearnal protocol upnp map %s %d -> %d' % (proto, nat_router_port, local_port)
    print(description)
    upnp.addportmapping(nat_router_port, proto, upnp.lanaddr, local_port, description, '')


def on_hook(target, target_args, target_kwargs):
    def wrap(func):
        def f(*args, **kwargs):
            target(*target_args, **target_kwargs)
            return func(*args, **kwargs)
        return f
    return wrap
