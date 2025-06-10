# 🎼 Linguagem de Descrição Musical

Este projeto define uma linguagem simples para compor música estruturada em texto.

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

---

## 📂 Estrutura do Projeto

- `parser/`: contém o analisador da linguagem
- `examples/`: exemplos de composições
- `README.md`: este arquivo de documentação

---

## 🧠 Licença e Créditos

Criado por Pedro Cliquet do Amaral. Sinta-se livre para usar, modificar e compartilhar.