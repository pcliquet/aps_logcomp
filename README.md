# aps_logcomp
## Aluno: Pedro Cliquet do Amaral


(* Programa *)
programa = { declaracao | comando } ;

(* Declarações *)
declaracao = "var" identificador ":" tipo "=" expressao ";" ;

tipo = "int" | "float" | "nota" | "instrumento" ;

(* Comandos *)
comando = tocar_nota
         | tocar_acorde
         | mudar_instrumento
         | if_statement
         | while_loop
         | atribuir_variavel
         | exportar_midi ;

tocar_nota = "play" expressao "dur" expressao ";" ;
tocar_acorde = "chord" "[" lista_de_notas "]" "dur" expressao ";" ;
mudar_instrumento = "instrument" expressao ";" ;
exportar_midi = "export" string_lit ";" ;

if_statement = "if" "(" expressao ")" "{" { comando } "}" [ "else" "{" { comando } "}" ] ;

while_loop = "while" "(" expressao ")" "{" { comando } "}" ;

atribuir_variavel = identificador "=" expressao ";" ;

(* Expressões *)
expressao = termo { operador termo } ;

termo = numero
      | identificador
      | nota_lit
      | string_lit ;

operador = "+" | "-" | "*" | "/" | "==" | "!=" | "<" | ">" | "<=" | ">=" ;

(* Listas *)
lista_de_notas = nota_lit { "," nota_lit } ;

(* Literais *)
nota_lit = "C" | "D" | "E" | "F" | "G" | "A" | "B"
         | "C#" | "D#" | "F#" | "G#" | "A#"
         | "Db" | "Eb" | "Gb" | "Ab" | "Bb" ;

string_lit = '"' { caractere } '"' ;

numero = [ "-" ] ( digit { digit } ) [ "." digit { digit } ] ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

identificador = letra { letra | digit | "_" } ;

letra = "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" ;

caractere = ? qualquer caractere válido exceto " ? ;

