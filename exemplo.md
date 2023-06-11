```ts
def function_name(param a, param b):integer {
  const x:integer = 1
  const y:integer = 9

  while (x < y) {
    x = x + 1;

    if (x < y) {
      stdout("X é menor que y")
    }
    else {
      stdout("X é maior ou igual a y")
    }
  }

  const string1:string = "James"
  const string2:string = "Leandro"

  const soma = string1 + string2

  return soma
}

const somador:integer = function_name(m, n)

```