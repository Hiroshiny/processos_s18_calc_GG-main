class Calculadora:
    @staticmethod
    def somar(num1, num2):
        return num1 + num2

    @staticmethod
    def maiorNumero(num1, num2):
        if num1 == num2:
            return 'Os dois números são iguais'
        if num1 > num2:
            return f'O maior número é {num1}'
        else:
            return f'O maior número é {num2}'

    @staticmethod
    def diferenca(numero1, numero2):
        return abs(numero1 - numero2)
