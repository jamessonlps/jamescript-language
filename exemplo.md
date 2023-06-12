```ts



def factorial(integer a) : integer {
  const factor : integer = 1
  const index : integer = 1

  while (index <= a) {
    factor = factor * index
    index = index + 1
  }

  return factor
}

const x : integer = factorial(5)

stdout("Fatorial de", 5, "é:", x)
// Fatorial de 5 é: 120



const x : integer
const y : integer

const a : string = "James"
const b : string = " Bond"

x = a == b
y = a != b

// Concatena, compara se igual, compara se diferente
stdout(a . b, x, y)
// James Bond 0 1



const arrow_function = (integer a, integer b) : integer => {
  
}

```