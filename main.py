import re
import os

def get_file_path():
    while True:
        path = input("Digite o caminho do arquivo do log que deseja analisar: ").strip()
        if os.path.isfile(path):
            return path
        print("Arquivo de log não encontrado, verifique o caminho do arquivo e tente novamente")

severity_patterns = {
    "ERROR": re.compile(r'\b(error|err|fatal|critical)\b', re.IGNORECASE),
    "WARNING": re.compile(r'\b(warn|warning)\b', re.IGNORECASE),
    "LOGIN": re.compile(r'\b(login|logon|signin|authenticat\w*)\b', re.IGNORECASE),
    "INFO": re.compile(r'\b(info|notice)\b', re.IGNORECASE),
}

ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

events = {key: 0 for key in severity_patterns}
ips = []
total_lines = 0

file_path = get_file_path()

with open(file_path, "r") as file:
    for line in file:

        total_lines += 1

        for event, pattern in severity_patterns.items():
            if pattern.search(line):
                events[event] += 1
        ips.extend(ip_pattern.findall(line))
       
unique_ips = sorted(set(ips))

print("Resumo da analise:")
print(f"\nNumero total de linhas presente no log: {total_lines}\n")

for event, count in events.items():
    print(f"{event}: {count}")

print("\nIps Encontrados:")
for ip in unique_ips:
    print(ip)
