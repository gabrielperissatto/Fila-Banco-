from __future__ import annotations
from typing import Any
from dataclasses import dataclass

@dataclass
class Pessoa:
    indice: int
    idade: int
    passagem: int = 0  

@dataclass
class No:
    elemento: Pessoa
    anterior: No | None = None
    proximo: No | None = None

class Fila:
    def __init__(self) -> None:
        '''
        Cria uma fila vazia.
        '''
        self.__inicio = None
        self.__fim = None

    def vazia(self) -> bool:
        '''
        Informa se há elementos na fila, isto é, devolve True se a fila está vazia e False caso contrário.
        
        Exemplos:
        >>> fila = Fila()
        >>> fila.vazia()
        True
        >>> fila.enfileira(Pessoa(1,31,0))
        >>> fila.vazia()
        False
        >>> fila.desenfileira()
        >>> fila.vazia()
        True
        '''
        return self.__inicio is None

    def numero_elementos(self) -> int:
        '''
        Devolve a quantidade de elementos que estão na fila.
        Exemplos:
        >>> fila = Fila()
        >>> fila.numero_elementos()
        0
        >>> fila.enfileira(Pessoa(1,31,0))
        >>> fila.enfileira(Pessoa(2,52,0))
        >>> fila.numero_elementos()
        2
        >>> fila.desenfileira()
        >>> fila.numero_elementos()
        1
        '''
        count = 0
        current = self.__inicio
        while current:
            count += 1
            current = current.proximo
        return count


    def enfileira(self, pessoa: Pessoa) -> None:
        '''
        
        Examples:
        >>> fila = Fila()
        >>> fila.enfileira(Pessoa(1, 65)) 
        >>> fila.enfileira(Pessoa(2, 25)) 
        >>> fila.enfileira(Pessoa(3, 72)) 
        >>> fila.enfileira(Pessoa(4, 31)) 
        >>> fila.enfileira(Pessoa(5, 80))
        >>> fila.enfileira(Pessoa(6, 18)) 
        >>> print(fila) 
        [Pessoa(indice=1, idade=65, passagem=0), Pessoa(indice=3, idade=72, passagem=0), Pessoa(indice=5, idade=80, passagem=0), Pessoa(indice=2, idade=25, passagem=0), Pessoa(indice=4, idade=31, passagem=0), Pessoa(indice=6, idade=18, passagem=0)]


        >>> fila2 = Fila()
        >>> fila2.enfileira(Pessoa(1, 25))
        >>> fila2.enfileira(Pessoa(2, 75))
        >>> fila2.enfileira(Pessoa(3, 62))
        >>> fila2.enfileira(Pessoa(4, 18))
        >>> fila2.enfileira(Pessoa(5, 19))
        >>> fila2.enfileira(Pessoa(6, 20))

        >>> print(fila2)
        [Pessoa(indice=2, idade=75, passagem=0), Pessoa(indice=3, idade=62, passagem=0), Pessoa(indice=1, idade=25, passagem=0), Pessoa(indice=4, idade=18, passagem=0), Pessoa(indice=5, idade=19, passagem=0), Pessoa(indice=6, idade=20, passagem=0)]

        >>> fila3 = Fila()  
        >>> fila3.enfileira(Pessoa(1, 20))
        >>> fila3.enfileira(Pessoa(2, 30))
        >>> fila3.enfileira(Pessoa(3, 40))
        >>> print(fila3)
        [Pessoa(indice=1, idade=20, passagem=0), Pessoa(indice=2, idade=30, passagem=0), Pessoa(indice=3, idade=40, passagem=0)]
        '''

        
        novo_no = No(pessoa)
        if self.vazia():
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            if pessoa.idade >= 60:  
                atual = self.__inicio
                anterior__ = None
                while atual:
                    if atual.elemento.idade < 60 and atual.elemento.passagem < 2:
                        
                        break
                    anterior__ = atual
                    atual = atual.proximo

                if anterior__ is None: 
                    novo_no.proximo = self.__inicio
                    self.__inicio.anterior = novo_no
                    self.__inicio = novo_no
                elif atual is None: 
                    novo_no.anterior = self.__fim
                    self.__fim.proximo = novo_no
                    self.__fim = novo_no
                else: 
                    novo_no.proximo = atual
                    novo_no.anterior = anterior__
                    anterior__.proximo = novo_no
                    atual.anterior = novo_no
                    if anterior__.elemento.idade < 60:
                        anterior__.elemento.passagem += 1
            else:  
                novo_no.anterior = self.__fim
                self.__fim.proximo = novo_no
                self.__fim = novo_no
                
    
    
    
    def desenfileira(self) -> None:
        '''
        Remove o elemento do início da fila. Se não for possível aparece um erro.
        
        Exemplos:
        >>> fila = Fila()
        >>> fila.enfileira(Pessoa(1,31))
        >>> fila.enfileira(Pessoa(2,32))
        >>> fila.enfileira(Pessoa(3,44))
        >>> fila.desenfileira()
        >>> print(fila)
        [Pessoa(indice=2, idade=32, passagem=0), Pessoa(indice=3, idade=44, passagem=0)]
        >>> fila.desenfileira()
        >>> print(fila)
        [Pessoa(indice=3, idade=44, passagem=0)]
        >>> fila.desenfileira()
        >>> print(fila)
        []
        >>> fila.desenfileira()
        Traceback (most recent call last):
            ...
        ValueError: fila vazia
        '''
        if self.vazia():
            raise ValueError('fila vazia')
        if self.__inicio == self.__fim:
            self.__inicio = None
            self.__fim = None
        else:
            self.__inicio = self.__inicio.proximo
            self.__inicio.anterior = None

    def primeiro(self):
        '''
        Devolve o elemento que está no início da fila 

        Exemplos:
        >>> fila = Fila()
        >>> fila.enfileira(Pessoa(1,50))
        >>> fila.enfileira(Pessoa(2,33))
        >>> fila.enfileira(Pessoa(3,41))
        >>> fila.primeiro()
        Pessoa(indice=1, idade=50, passagem=0)
        >>> fila.desenfileira()
        >>> fila.primeiro()
        Pessoa(indice=2, idade=33, passagem=0)
        >>> fila.desenfileira()
        >>> fila.primeiro()
        Pessoa(indice=3, idade=41, passagem=0)
        >>> fila.desenfileira()
        >>> fila.primeiro()
        Traceback (most recent call last):
            ...
        ValueError: fila vazia
        '''
        if self.vazia():
            raise ValueError('fila vazia')
        return self.__inicio.elemento

    def __str__(self) -> str:
        '''
        Exibe todos os elementos que estão na fila.
        '''
        if self.vazia():
            return '[]'
        it = self.__inicio
        repr = f'[{it.elemento}'
        while it != self.__fim:
            repr += ', '
            it = it.proximo
            repr += f'{it.elemento}'
        repr += ']'
        return repr
    
