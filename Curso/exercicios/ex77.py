palavras = ('aprender', 'programas', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')