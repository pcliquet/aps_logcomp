# aps_logcomp
## Aluno: Pedro Cliquet do Amaral



# 🎼 Linguagem de Descrição Musical

Este projeto define uma linguagem simples para compor música estruturada em texto.

## 🧠 Licença e Créditos

Criado por Pedro Cliquet do Amaral. Sinta-se livre para usar, modificar e compartilhar.


---

## 💡 Motivação

A principal motivação por trás do desenvolvimento desta linguagem foi **simplificar a criação de músicas programaticamente**, permitindo que músicos, desenvolvedores e entusiastas possam escrever composições musicais de forma **estruturada, legível e reutilizável**, sem depender de interfaces complexas ou softwares pesados.

Alguns dos objetivos foram:

- Criar uma **DSL (linguagem específica de domínio)** para composição musical;
- Permitir **composição textual** de músicas com controle preciso de notas e acordes;
- Facilitar o ensino de **lógica musical** e estruturas repetitivas usando uma linguagem próxima da programação;
- Oferecer uma ferramenta que **gera arquivos MIDI** de maneira rápida e controlada.

---

## ✨ Características da Linguagem

- Sintaxe **intuitiva** e fácil de aprender.
- Suporte a **variáveis musicais** (notas e acordes).
- Blocos bem definidos: `Music`, `Varials`, `Instrument`, `Loop`.
- Comandos simples: `Chord`, `play`.
- Reutilização de padrões por meio de `Loop`.
- Estrutura pensada para facilitar a **geração de músicas repetitivas** e com **estrutura clara**.
- Compatível com padrões **MIDI**, facilitando a integração com instrumentos e DAWs.

---

## 🎲 Curiosidades

- A ideia do bloco `Varials` veio da necessidade de **nomes simbólicos para acordes e notas**, como se fosse uma "tabela de acordes".
- Foi inspirada por linguagens como **ABC Notation**, mas com foco em **blocos e repetição**, como um "pseudocódigo musical".
- A linguagem não usa **ponto e vírgula** ou símbolos desnecessários: a ideia é manter a sintaxe o mais **musical e natural possível**.
- Pode ser expandida futuramente com **dinâmicas**, **instrumentos personalizados**, **mudança de andamento**, entre outros recursos.


## EBNF

program         = "Music", identifier, integer, "{",
                    varials_block,
                    instrument_block*,
                  "}" ;

varials_block   = "Varials", "{",
                    varial_decl*,
                  "}" ;

varial_decl     = identifier, "=", (note_list | integer) ;

note_list       = "[",
                    integer, { ",", integer },
                  "]" ;

instrument_block = "Instrument", identifier, integer, "{",
                     loop_block+,
                   "}" ;

loop_block       = "Loop", identifier, integer, "{",
                     music_command+,
                   "}" ;

music_command    = chord_command | play_command ;

chord_command    = "Chord", identifier, integer ;

play_command     = "play", identifier, integer ;

identifier       = letter, { letter | digit | "_" } ;

integer          = digit, { digit } ;

letter           = "A" .. "Z" | "a" .. "z" ;

digit            = "0" .. "9" ;



## 📖 Tutorial de Uso

### 🎵 Estrutura Inicial

Toda música começa com o bloco `Music`, que define o nome da música e o BPM (batidas por minuto):

```txt
Music Nome_da_Musica 128 {
    // blocos internos aqui
}
```

- `Music`: palavra-chave obrigatória que inicia o bloco principal.
- `Nome_da_Musica`: nome da música (usado como nome do arquivo final).
- `128`: BPM da música.

---

### 🎼 Bloco `Varials`

O bloco `Varials` define notas ou acordes reutilizáveis com nomes simbólicos:

```txt
Varials {
    do_maior = [60, 64, 67]
    fa = 77
}
```

- Valores entre colchetes (`[...]`) representam **acordes** (notas tocadas ao mesmo tempo).
- Valores inteiros simples representam **notas únicas**.

---

### 🎹 Bloco `Instrument`

Define um instrumento que será usado na composição:

```txt
Instrument piano 1 {
    // loops aqui
}
```

- `Instrument`: palavra-chave do bloco.
- `piano`: nome do instrumento.
- `1`: canal MIDI no qual o instrumento será executado.

---

### 🔁 Bloco `Loop`

Define um padrão repetido de execução musical:

```txt
Loop riff_principal 4 {
    Chord do_maior 2
    play fa 1
}
```

- `Loop`: palavra-chave do bloco.
- `riff_principal`: nome do loop.
- `4`: quantidade de vezes que esse bloco será repetido.

---

### 🎶 Comando `Chord`

Toca um conjunto de notas ao mesmo tempo (acorde):

```txt
Chord do_maior 2
```

- `do_maior`: nome de um acorde definido em `Varials`.
- `2`: tempo de duração do acorde.

---

### 🎵 Comando `play`

Toca uma única nota por um determinado tempo:

```txt
play fa 1
```

- `fa`: nome de uma nota definida em `Varials`.
- `1`: tempo de duração da nota.

---

## 📦 Exemplo Completo

```txt
Music MinhaMusica 120 {
    Varials {
        do_maior = [60, 64, 67]
        fa = 77
    }

    Instrument piano 1 {
        Loop base 2 {
            Chord do_maior 2
            play fa 1
        }
    }
}
```


Acesse os codigos de exemplo no link abaixo:

[Acesse a pasta de código](https://github.com/pcliquet/aps_logcomp/tree/main/arquivos_testes)


Para testar o codigo gerado pelo compilador utilize o site e arraste o arquivo .mid para ouvir:
[Pianotify](https://pianotify.com/import-midi-file)




