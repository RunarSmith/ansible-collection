import sys
import xml.etree.ElementTree as ET

def parse_nmap_xml(filename):
    """Parses an Nmap XML output file and returns a list of dictionaries, each representing a service."""

    services = []
    tree = ET.parse(filename)

# <!DOCTYPE nmaprun>
# 'nmaprun' object is the root
    root = tree.getroot()

# <nmaprun scanner="nmap" args="nmap -T4 -sCSV -oA target 10.10.10.10" start="1234567890" startstr="Fri Oct 10 10:10:10 2000" version="xxxx" xmloutputversion="1.05">
# 'nmaprun' is the root object
    print( f"\nCommand: `{root.get('args')}`\n")

    for host in root.findall('host'):

# <hostnames>
#   <hostname name="hostname.lan" type="PTR"/>
# </hostnames>
        for hname in host.findall('hostnames'):
            print( "- Hostname: `" + hname.find('hostname').get('name') + "`" )

# <address addr="10.10.10.10" addrtype="ipv4"/>
        print( "- Address: `" + host.find('address').get('addr') + "`" )
        print( "" )

# <ports>
#   <port protocol="tcp" portid="135">
#       <state state="open" reason="syn-ack" reason_ttl="64"/>
#       <service name="msrpc" product="Microsoft Windows RPC" ostype="Windows" method="probed" conf="10">
#           <cpe>cpe:/o:microsoft:windows</cpe>
#       </service>
#   </port>
#   <port>
#       ...
#   </port>
# </ports>
        for port in host.find('ports').findall('port'):
            state = port.find('state').get('state')
            service = port.find('service')
            if service is not None:
                name = service.get('name')
                product = service.get('product')
                version = service.get('version')
                port_proto = port.get('protocol')
                port_number = port.get('portid')

                services.append({'name': name, 
                                 'product': product, 
                                 'version': version, 
                                 'proto': port_proto, 
                                 'port': port_number,
                                 'state': state})
    return services

def generate_markdown_table(services):
    """Generates a Markdown table from a list of service dictionaries."""

    table_header = "| Software | Version | Vuln. ID       | Service name | Exposed on | Comments |\n| -------- | ------- | ------- | ------- | ---------- | -------- |\n"
    table_rows = []
    for service in services:

        port_state = ""
        if service['state'] != None and service['state'] != 'open':
            port_state = f"({service['state']}) "
        
        product = service['product']
        if product == None:
            product = ""

        version = service['version']
        if version == None:
            version = ""

        table_rows.append(f"| {product} | {version} |  | {service['name']} | {service['proto'].upper()}/{service['port']} {port_state}|  |\n")
    return table_header + ''.join(table_rows)

if __name__ == '__main__':
    nmap_output_file = sys.argv[1]
    print( "Input File: {}".format( nmap_output_file ) )
    services = parse_nmap_xml(nmap_output_file)
    markdown_table = generate_markdown_table(services)
    print(markdown_table)
