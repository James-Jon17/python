nomeCompleto = str(input('Digite seu nome completo')).strip()
nomeSeparado = nomeCompleto.split()
print('Seu nome comple é {}'.format(nomeCompleto.title()))
print('Seu primeiro nome é {}'.format(nomeSeparado[0].capitalize()))
print('Seu ultimo nome é {}'.format(nomeSeparado[-1].capitalize()))