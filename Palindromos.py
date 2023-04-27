# No es la forma más optima de obtener un palindromo.
# Aunque queria destacarlo porque hice un razonamiento interesante para
# obtener el resultado deseado.



def es_palindromo(texto):
    if " " in texto:
        texto = texto.replace(" ", "")
    
    resultado = 0
    for _ in texto:
        resultado += 1
    
    half = resultado % 2
    if half == 0:
        result = int(resultado / 2)
        result_corr = result
    else:
        result = int((resultado - 1) / 2)
        result_corr = int(result + 1)

    part1 = texto.lower()[:result]
    part2 = texto.lower()[result_corr:]
    part2_reversed = part2[::-1]
    
    if part1 == part2_reversed:
         print("es palíndromo")
    else:
        print("no es palíndromo")
    
es_palindromo("reco nocer")