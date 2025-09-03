


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
