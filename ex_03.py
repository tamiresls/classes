
from classes import ContaCorrente

conta = ContaCorrente(1234, "Tamires")
print(f'O número da sua conta é: {conta.numero_conta}')
print(f'Nome: {conta.nome_correntista}')
print(f'Seu saldo é de: R${conta.saldo}')

depositar = float(input('Digite o valor que deseja depositar: '))
conta.deposito(depositar)
print(f'Seu saldo agora é de: R${conta.saldo}')

sacar = float(input('Digite o valor que deseja sacar: '))
conta.saque(sacar)
print(f'Seu saldo agora é de: R${conta.saldo}')

conta.alterar_nome("Tamires 02")
print(f'O nome da sua conta oi alterada para: {conta.nome_correntista}')