```ts
def function_name(integer a, integer b):integer {
  const x:integer = 1
  const y:integer = 9

  while (x < y) {
    x = x + 1

    if (x < y) {
      stdout("X é menor que y")
    } else {
      stdout("X é maior ou igual a y")
    }
  }

  const string1:string = "James"
  const string2:string = "Leandro"

  const soma = string1 + string2

  return soma
}

const somador:integer = function_name(m, n)


// Função que verifica se duas strings são iguais
def factorial(integer a) : integer {
  const factor : integer = 1
  const index : integer = 1

  while (index < a) {
    factor = factor * a
    index = index + 1

    if (index == a) {
      stdout("Fatorial atingido. Resposta: ")
      stdout(factor)
    }
  }

  return factor
}


```