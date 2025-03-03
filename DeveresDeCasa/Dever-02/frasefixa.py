def solicitar_frase():
    """Função para retornar uma frase fixa (substitui a entrada do usuário)."""
    return "Python é bem dificil"

def analisar_frase(frase):
    # Contagem de caracteres
    total_caracteres = len(frase)

    # Contagem de palavras
    palavras = frase.split()
    num_palavras = len(palavras)

    # Maior palavra
    maior_palavra = max(palavras, key=len)

    # Inversão da frase por caracteres
    frase_invertida_caracteres = frase[::-1]

    # Inversão da ordem das palavras
    frase_invertida_palavras = ' '.join(palavras[::-1])

    # Alteração de caixa
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()

    # Criando a tupla de palavras
    tupla_palavras = tuple(palavras)

    return total_caracteres, num_palavras, maior_palavra, frase_invertida_caracteres, frase_invertida_palavras, frase_maiuscula, frase_minuscula, tupla_palavras

def exibir_resultados(resultado):

    total_caracteres, num_palavras, maior_palavra, frase_invertida_caracteres, frase_invertida_palavras, frase_maiuscula, frase_minuscula, tupla_palavras = resultado
    
    print("\nResultados da Análise da Frase:")
    print(f"1. Número de caracteres da frase: {total_caracteres}")
    print(f"2. Número de palavras na frase: {num_palavras}")
    print(f"3. A palavra com maior comprimento: {maior_palavra}")
    print(f"4. Frase invertida por caracteres: {frase_invertida_caracteres}")
    print(f"5. Frase invertida pela ordem das palavras: {frase_invertida_palavras}")
    print(f"6. Frase em maiúsculas: {frase_maiuscula}")
    print(f"7. Frase em minúsculas: {frase_minuscula}")
    print(f"8. Tupla com as palavras da frase: {tupla_palavras}")

def main():
    
    frase = solicitar_frase()  # Solicita a frase ao usuário
    resultado = analisar_frase(frase)  # Realiza as operações de análise e formatação
    exibir_resultados(resultado)  # Exibe os resultados formatados

if __name__ == "__main__":
    main()
