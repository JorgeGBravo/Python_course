text = input("Escribe en la siguiente linea, el texto a analizar : \n")

text = text.lower()
text_letters = list(text)
text_words = text.split()

text_count = len(text_letters)
text_letter_start = text_letters[0]
text_letter_end = text_letters[-1]

text_words.reverse()
text_words = " ".join(text_words)

print("Ingresa tres letras: \n")
letter_A = input("Primera: ").lower()
letter_B = input("Segunda: ").lower()
letter_C = input("Tercera: ").lower()
letter_count_A = text.count(letter_A)
letter_count_B = text.count(letter_B)
letter_count_C = text.count(letter_C)


search = "python" in text_words
results_searchs = {True: "Python se encuentra en el texto", False: "Python no se encuentra en el texto"}


print(f"""El texto contine {text_count} letras.
La primera letra del texto es "{text_letter_start.upper()}" y la última "{text_letter_end}".
La letra "{letter_A}" está {letter_count_A} veces en el texto. 
La letra "{letter_B}" está {letter_count_B} veces en el texto.
La letra "{letter_C}" está {letter_count_C} veces en el texto.
El texto del reves se escribiría así:
{text_words}
El texto contiene {text_count} en total y la palabra {results_searchs[search]}.""")