import csv
from datetime import datetime

def read_csv_record(n):
    try:
        with open('data.csv', 'r') as file:
            records = list(csv.reader(file))
            
            if n < 1 or n > len(records):
                return "Registro não encontrado"
                
            record = records[n-1]
            
            # Convert dates to Brazilian format
            birth_date = datetime.strptime(record[1], '%m-%d-%Y').strftime('%d/%m/%Y')
            register_date = datetime.strptime(record[2], '%Y-%m-%d').strftime('%d/%m/%Y')
            
            # Format the output
            return f"Nome: {record[0]} | Data de Nascimento: {birth_date} | Data de Cadastro: {register_date} | Hora: {record[3]}"
            
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Erro ao ler o arquivo: {str(e)}"

# Get user input
try:
    n = int(input("Digite o número do registro que deseja consultar: "))
    result = read_csv_record(n)
    print(result)
except ValueError:
    print("Por favor, digite um número válido")