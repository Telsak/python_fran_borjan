def grab_rconf(filename):
    with open(filename, 'r') as f:
        for rad in f:
            if 'hostname' in rad:
                host = rad[rad.find(' ')+1:].rstrip()
            elif 'Last configuration change at' in rad:
                change = rad[rad.find('at ')+3:].rstrip()
    return host, change

def grab_vers(filename):
    with open(filename, 'r') as f:
        for rad in f:
            if 'ROM: System' in rad:
                version = rad[rad.find('System'):].rstrip()
            elif 'uptime is' in rad:
                uptime = rad[rad.find('is ')+3:].rstrip()
    return version, uptime

def push_info(rconf, vers, host, change, rom, uptime):
    r_just = 'Senaste ändringen:'
    print(f'{"="*10} Info konfigurationsfiler {"="*10}')
    print(f'Läser: {rconf}\nLäser: {vers}')
    print(f'Sammanställning:\n{"-"*80}')
    print(r_just.rjust(len(r_just)+1), change)
    print('Hostname:'.rjust(len(r_just)+1), host)
    print('ROM-version:'.rjust(len(r_just)+1), rom)
    print('Uptime:'.rjust(len(r_just)+1), uptime)


rconf = 'router_configuration.txt'
vers = 'router_show_version.txt'
            
m_host, m_change = grab_rconf(rconf)
m_vers, m_uptime = grab_vers(vers)
push_info(rconf, vers, m_host, m_change, m_vers, m_uptime)
