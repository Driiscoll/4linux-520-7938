import os ,pprint

pprint.pprint(dict(os.environ))

requeriments_file = os.eviron.get("REQUIREMENTS_TXT")
print(requeriments_file)
processo = os.popen("date")
saida = list(processo)[0]
print(saida)
processo.close()

processo = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)

processo.wait()
print(processo.pid)
print(processo.returncode)

for(caminho, pastas, arquivos) in os.wait('.'):
    print(f'estamos em {caminho}')
    print(f'os arquivos são {arquivos}')
    print(f'as pastas são {pastas}')
    input('>')
