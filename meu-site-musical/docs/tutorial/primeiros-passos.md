## 📖 Tutorial de Uso

Clone o repositório localmente em sua maquina. 

[Repositório git](https://github.com/pcliquet/aps_logcomp)


### Criação da música




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
- `piano`: nome do instrumento. Para saber o nome do insrumento acesse [Instrumentos](https://github.com/pcliquet/aps_logcomp/blob/main/arquivo_com_nome_dos_instrumentos.txt). O compilador não trata os nomes compostos dos instrumentos, funciona apenas para nomes como viola.
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

Acesse os codigos de exemplo no link abaixo:

[Acesse a pasta de código](https://github.com/pcliquet/aps_logcomp/tree/main/arquivos_testes)


Para testar o codigo gerado pelo compilador utilize o site e arraste o arquivo .mid para ouvir:
[Pianotify](https://pianotify.com/import-midi-file)

Para executar:
```
python3 main.py seu_arquivo.music
```

