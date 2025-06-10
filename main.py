from mido import Message, MidiFile, MidiTrack, MetaMessage
import sys

# Cria um novo arquivo MIDI
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

    
def set_bpm( bpm, time=0):
    """
    track = MidiTrack()
    set_bpm(track, bpm=100)

    """
    return int(60_000_000 / bpm)
    #track.append(MetaMessage('set_tempo', tempo=tempo, time=time))

###########################################################################################################################
#Busca instrumento
instrument_map = {
    "acoustic grand piano": 0,
    "bright acoustic piano": 1,
    "electric grand piano": 2,
    "honky-tonk piano": 3,
    "electric piano 1": 4,
    "electric piano 2": 5,
    "harpsichord": 6,
    "clavinet": 7,
    "celesta": 8,
    "glockenspiel": 9,
    "music box": 10,
    "vibraphone": 11,
    "marimba": 12,
    "xylophone": 13,
    "tubular bells": 14,
    "dulcimer": 15,
    "drawbar organ": 16,
    "percussive organ": 17,
    "rock organ": 18,
    "church organ": 19,
    "reed organ": 20,
    "accordion": 21,
    "harmonica": 22,
    "tango accordion": 23,
    "acoustic guitar (nylon)": 24,
    "acoustic guitar (steel)": 25,
    "electric guitar (jazz)": 26,
    "electric guitar (clean)": 27,
    "electric guitar (muted)": 28,
    "overdriven guitar": 29,
    "distortion guitar": 30,
    "guitar harmonics": 31,
    "acoustic bass": 32,
    "electric bass (finger)": 33,
    "electric bass (pick)": 34,
    "fretless bass": 35,
    "slap bass 1": 36,
    "slap bass 2": 37,
    "synth bass 1": 38,
    "synth bass 2": 39,
    "violin": 40,
    "viola": 41,
    "cello": 42,
    "contrabass": 43,
    "tremolo strings": 44,
    "pizzicato strings": 45,
    "orchestral harp": 46,
    "timpani": 47,
    "string ensemble 1": 48,
    "string ensemble 2": 49,
    "synth strings 1": 50,
    "synth strings 2": 51,
    "choir aahs": 52,
    "voice oohs": 53,
    "synth choir": 54,
    "orchestra hit": 55,
    "trumpet": 56,
    "trombone": 57,
    "tuba": 58,
    "muted trumpet": 59,
    "french horn": 60,
    "brass section": 61,
    "synth brass 1": 62,
    "synth brass 2": 63,
    "soprano sax": 64,
    "alto sax": 65,
    "tenor sax": 66,
    "baritone sax": 67,
    "oboe": 68,
    "english horn": 69,
    "bassoon": 70,
    "clarinet": 71,
    "piccolo": 72,
    "flute": 73,
    "recorder": 74,
    "pan flute": 75,
    "blown bottle": 76,
    "shakuhachi": 77,
    "whistle": 78,
    "ocarina": 79,
    "lead 1 (square)": 80,
    "lead 2 (sawtooth)": 81,
    "lead 3 (calliope)": 82,
    "lead 4 (chiff)": 83,
    "lead 5 (charang)": 84,
    "lead 6 (voice)": 85,
    "lead 7 (fifths)": 86,
    "lead 8 (bass + lead)": 87,
    "pad 1 (new age)": 88,
    "pad 2 (warm)": 89,
    "pad 3 (polysynth)": 90,
    "pad 4 (choir)": 91,
    "pad 5 (bowed)": 92,
    "pad 6 (metallic)": 93,
    "pad 7 (halo)": 94,
    "pad 8 (sweep)": 95,
    "fx 1 (rain)": 96,
    "fx 2 (soundtrack)": 97,
    "fx 3 (crystal)": 98,
    "fx 4 (atmosphere)": 99,
    "fx 5 (brightness)": 100,
    "fx 6 (goblins)": 101,
    "fx 7 (echoes)": 102,
    "fx 8 (sci-fi)": 103,
    "sitar": 104,
    "banjo": 105,
    "shamisen": 106,
    "koto": 107,
    "kalimba": 108,
    "bagpipe": 109,
    "fiddle": 110,
    "shanai": 111,
    "tinkle bell": 112,
    "agogo": 113,
    "steel drums": 114,
    "woodblock": 115,
    "taiko drum": 116,
    "melodic tom": 117,
    "synth drum": 118,
    "reverse cymbal": 119,
    "guitar fret noise": 120,
    "breath noise": 121,
    "seashore": 122,
    "bird tweet": 123,
    "telephone ring": 124,
    "helicopter": 125,
    "applause": 126,
    "gunshot": 127
}

def buscar_programa(nome, instrument_map):
    nome_normalizado = nome.strip().lower()
    if nome_normalizado in instrument_map:
        return instrument_map[nome_normalizado]
    raise ValueError(f"Nome do Instrumento '{nome}' nao encontrado.")


###########################################################################################################################
# PrePro (futuramente: remove comentários, normaliza espaços, etc.)
# Por enquanto, mantemos em branco



#########################################################################################################################

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def evaluate(self, st):
        return None

def beat_to_tick(beat, ticks_per_beat=480):
    return int(beat * ticks_per_beat)


def criar_midi_com_duracoes(musica, bpm, nome, instrumentos, instrument_map):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    tempo = int(60_000_000 / bpm)
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
    track.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))

    # Lista com todos os eventos (tempo absoluto)
    eventos = []

    #program = buscar_programa(instrumentos[], instrument_map)
    #print(program)

    # Instrumentos
    for nome_instr, dados in musica["instrumentos"].items():
        #print(nome_instr)
        canal = dados["canal"]
        program = buscar_programa(nome_instr, instrument_map)
        track.append(Message('program_change', program=program, channel=canal, time=0))

        tempo_atual = 0  # tempo em beats

        for bloco in dados["partitura"]:
            if "nota" in bloco or "note" in bloco:
                entradas = bloco["note"]
                if isinstance(entradas, tuple):
                    entradas = [entradas]

                for nota, duracao in entradas:
                    tick_on = beat_to_tick(tempo_atual)
                    tick_off = beat_to_tick(tempo_atual + duracao)

                    eventos.append({"tick": tick_on, "msg": Message('note_on' , note=nota, velocity=64, channel=canal)})
                    eventos.append({"tick": tick_off, "msg": Message('note_off', note=nota, velocity=64, channel=canal)})
                    tempo_atual += duracao

            elif "chord" in bloco:
                entradas = bloco["chord"]
                if isinstance(entradas, tuple):
                    entradas = [entradas]

                for notas, duracao in entradas:
                    tick_on = beat_to_tick(tempo_atual)
                    tick_off = beat_to_tick(tempo_atual + duracao)
                    for nota in notas:
                        eventos.append({"tick": tick_on, "msg": Message('note_on', note=nota, velocity=64, channel=canal)})
                        eventos.append({"tick": tick_off, "msg": Message('note_off', note=nota, velocity=64, channel=canal)})
                    tempo_atual += duracao


    # Ordenar eventos por tick
    eventos.sort(key=lambda e: e["tick"])

    # Converter para tempo relativo
    ultimo_tick = 0
    for evento in eventos:
        delta = evento["tick"] - ultimo_tick
        evento["msg"].time = delta
        track.append(evento["msg"])
        ultimo_tick = evento["tick"]

    mid.save(f'{nome}.mid')
    print(f"Arquivo '{nome}.mid' criado com sucesso.")





class MusicNode(Node):
    def __init__(self, nome, bpm, varials, instrumentos, loops, ifs, chords, plays):
        self.nome = nome
        self.bpm = bpm
        self.varials = varials
        self.instrumentos = instrumentos
        self.loops = loops
        self.ifs = ifs
        self.chords = chords
        self.plays = plays

    def evaluate(self, context=None):
        print(f"⏺ Criando música: {self.nome} | BPM: {self.bpm}")
        
        if context is None:
            context = {}
        if "instrumentos" not in context:
            context["instrumentos"] = {}
        
        # Criar dicionário varials no contexto, se ainda não existir
        if "varials" not in context:
            context["varials"] = {}

        # Avalia variáveis primeiro
        if self.varials:
            self.varials.evaluate(context)

        # Avalia instrumentos com acesso às variáveis
        for instrumento in self.instrumentos:
            instrumento.evaluate(context)



class VarialsNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value  # int ou list

    def evaluate(self, context):
        nome = self.name.value

        if isinstance(self.value, list):
            valor = [v.value for v in self.value]  # lista de inteiros
        else:
            valor = self.value.value  # um número só

        context["varials"][nome] = valor
        #print("VarialsNode")
        #print(context)

class VarialsBlockNode:
    def __init__(self, varials):
        self.varials = varials

    def evaluate(self, context):
        #print(f'contexto no vblock{context}')
        for varial in self.varials:
            varial.evaluate(context)


class InstrumentNode(Node):
    def __init__(self, nome, canal):
        self.nome = nome
        self.canal = canal
        self.partitura = []
        self._current_block_type = None
        self._current_block = None

    def add_event(self, tipo, node):
        if tipo != self._current_block_type:
            if self._current_block:
                self.partitura.append(self._current_block)
            self._current_block_type = tipo
            self._current_block = {tipo: []}
        self._current_block[tipo].append(node)


    def finalize(self):
        if self._current_block:
            self.partitura.append(self._current_block)
            #print(f'TEMOS UM JOGO: {self.partitura}')
            self._current_block = None
            self._current_block_type = None

    def evaluate(self, context):
        self.finalize()
        context["instrumentos"][self.nome] = {
            "canal": self.canal,
            "partitura": []
        }

        for bloco in self.partitura:
            for tipo, eventos in bloco.items():
                for node in eventos:
                    node.evaluate(context)

        print(f"[InstrumentNode.evaluate] Instrumento '{self.nome}' avaliado e salvo no contexto")



class PlayNode(Node):
    def __init__(self, nota, duracao, canal):
        self.nota = nota
        self.duracao = duracao
        self.canal = canal

    def evaluate(self, context):
        # Resolve nota
        if hasattr(self.nota, "evaluate"):
            nota_val = self.nota.evaluate(context)

        elif isinstance(self.nota, Token):
            nome_var = self.nota.value
            if nome_var in context["varials"]:
                nota_val = context["varials"][nome_var]
            else:
                raise Exception(f"Variável '{nome_var}' não definida")

        elif isinstance(self.nota, str):
            if self.nota in context["varials"]:
                nota_val = context["varials"][self.nota]
            else:
                raise Exception(f"Variável '{self.nota}' não definida")

        elif isinstance(self.nota, int):
            nota_val = self.nota

        else:
            raise Exception(f"Tipo inesperado em nota: {self.nota} ({type(self.nota)})")

        # Se for lista (ex: acorde), pega a primeira nota
        if isinstance(nota_val, list):
            nota_final = nota_val[0]
        else:
            nota_final = nota_val

        # Resolve duração
        duracao_final = self.duracao.evaluate(context) if hasattr(self.duracao, "evaluate") else self.duracao

        # Adiciona à partitura
        for nome, info in context["instrumentos"].items():
            if info["canal"] == self.canal:
                info["partitura"].append({"note": (int(nota_final), duracao_final)})
                break
        else:
            raise Exception(f"Nenhum instrumento com canal {self.canal}")

class ChordNode(Node):
    def __init__(self, notas, duracao, canal):
        self.notas = notas  # Lista de notas ou tokens
        self.duracao = duracao
        self.canal = canal

    def evaluate(self, context):
        duracao_val = self.duracao.evaluate(context) if hasattr(self.duracao, "evaluate") else self.duracao
        notas_com_duracao = []

        # Transforma tudo em lista, mesmo que venha só uma string ou token
        notas = self.notas if isinstance(self.notas, list) else [self.notas]

        #print(f'qq e isso: {self.notas}')

        for n in notas:
            # Caso seja um nó que implementa evaluate()
            if hasattr(n, "evaluate"):
                val = n.evaluate(context)

            # Caso seja um Token do tipo IDENTIFIER (ID)
            elif isinstance(n, Token):
                nome_var = n.value
                if nome_var in context["varials"]:
                    val = context["varials"][nome_var]
                else:
                    raise Exception(f"Variável '{nome_var}' não definida")

            # Caso seja uma string simples (como 'do_maior')
            elif isinstance(n, str):
                if n in context["varials"]:
                    val = context["varials"][n]
                else:
                    raise Exception(f"Variável '{n}' não definida")

            # Caso seja número direto
            elif isinstance(n, int):
                val = n

            else:
                raise Exception(f"Tipo inesperado em notas: {n} ({type(n)})")

            # Se a nota for um acorde (lista), adiciona todas
            if isinstance(val, list):
                notas_com_duracao.extend(val)
            else:
                notas_com_duracao.append(val)

        #print(notas_com_duracao)

        for nome, info in context["instrumentos"].items():
            if info["canal"] == self.canal:
                info["partitura"].append({"chord": (notas_com_duracao, duracao_val)})
                break
        else:
            raise Exception(f"Nenhum instrumento com canal {self.canal}")
            



class LoopNode(Node):
    def __init__(self, vezes, conteudo):
        self.vezes = vezes
        self.conteudo = conteudo

    def evaluate(self, context):
        for _ in range(self.vezes):
            for node in self.conteudo:
                node.evaluate(context)



#########################################################################################################################
# Token

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


#########################################################################################################################
# Tokenizer
class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.position = 0

    def get_next_char(self):
        if self.position >= len(self.text):
            return None
        char = self.text[self.position]
        self.position += 1
        return char

    def peek_char(self):
        if self.position >= len(self.text):
            return None
        return self.text[self.position]

    def tokenize(self):
        tokens = []

        keywords = {
            "play": "PLAY",
            "Chord": "CHORD",
            "Loop": "LOOP",
            "Instrument": "INSTRUMENT",
            "Music": "MUSIC",
            "Varials": "VARIALS",
            "if": "IF"
        }

        while True:
            char = self.get_next_char()
            if char is None:
                break
            elif char.isspace():
                continue
            elif char.isdigit():
                number = char
                while (peek := self.peek_char()) and peek.isdigit():
                    number += self.get_next_char()
                tokens.append(Token("NUMBER", int(number)))
            elif char == "+":
                if self.peek_char() == "=":
                    self.get_next_char()
                    tokens.append(Token("PLUS_ASSIGN", "+="))
                else:
                    tokens.append(Token("PLUS", "+"))
            elif char == "-":
                tokens.append(Token("MINUS", "-"))
            elif char == "*":
                tokens.append(Token("MULT", "*"))
            elif char == "/":
                tokens.append(Token("DIV", "/"))
            elif char == ">":
                if self.peek_char() == "=":
                    self.get_next_char()
                    tokens.append(Token("GTE", ">="))
                else:
                    tokens.append(Token("GT", ">"))
            elif char == "<":
                if self.peek_char() == "=":
                    self.get_next_char()
                    tokens.append(Token("LTE", "<="))
                else:
                    tokens.append(Token("LT", "<"))
            elif char == "=":
                if self.peek_char() == "=":
                    self.get_next_char()
                    tokens.append(Token("EQ", "=="))
                else:
                    tokens.append(Token("ASSIGN", "="))
            elif char == "{":
                tokens.append(Token("LBRACE", "{"))
            elif char == "}":
                tokens.append(Token("RBRACE", "}"))
            elif char == "[":
                tokens.append(Token("LBRACK", "["))
            elif char == "]":
                tokens.append(Token("RBRACK", "]"))
            elif char == ",":
                tokens.append(Token("COMMA", ","))
            elif char in "()":
                tokens.append(Token("PAREN", char))
            elif char.isalpha():
                ident = char
                while (peek := self.peek_char()) and (peek.isalnum() or peek == "_"):
                    ident += self.get_next_char()
                token_type = keywords.get(ident, "ID")
                tokens.append(Token(token_type, ident))
            else:
                raise ValueError(f"Caractere inválido: {char}")

        return tokens


#########################################################################################################################
# Parser
class Parser:
    def __init__(self, tokenizer):
        self.tokens = tokenizer.tokenize()
        self.pos = 0
        self.count = 0
        self.instrumento_atual = None
        self.varials = {}  # <- aqui!

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected_type):
        token = self.current_token()
        if token is None:
            raise Exception("Fim inesperado dos tokens")
        if token.type == expected_type:
            self.pos += 1
            return token
        raise Exception(f"Esperado {expected_type}, mas encontrou {token.type}")
    
    def parse_expression(self):
        expr = self.parse_term()
        while self.current_token() and self.current_token().type in ("PLUS", "MINUS"):
            op = self.eat(self.current_token().type)
            right = self.parse_term()
            expr = f"{expr} {op.value} {right}"
        return expr

    def parse_term(self):
        term = self.parse_factor()
        while self.current_token() and self.current_token().type in ("MULT", "DIV"):
            op = self.eat(self.current_token().type)
            right = self.parse_factor()
            term = f"{term} {op.value} {right}"
        return term

    def parse_factor(self):
        token = self.current_token()
        if token.type in ("NUMBER", "ID"):
            return self.eat(token.type).value
        elif token.type == "PAREN" and token.value == "(":
            self.eat("PAREN")  # come (
            expr = self.parse_expression()
            self.eat("PAREN")  # come )
            return f"({expr})"
        else:
            raise Exception(f"Fator inválido: {token}")

    def parse(self):
        self.parse_program()

    def parse_program(self):
        #print("novo bloco MUSIC \n################################################ ")
        
        self.eat("MUSIC")
        nome = self.current_token().value
        self.eat("ID")

        bpm = int(self.current_token().value)
        self.eat("NUMBER")

        self.eat("LBRACE")

        varials = []
        instrumentos = []
        loops = []
        ifs = []
        chords = []
        plays = []

        while self.current_token() and self.current_token().type != "RBRACE":
            token_type = self.current_token().type

            if token_type == "VARIALS":
                varials = self.parse_varials_block()
            elif token_type == "INSTRUMENT":
                instrumento = self.parse_instrument_block()  # captura o InstrumentNode criado
                instrumentos.append(instrumento)             # adiciona na lista
            elif token_type == "LOOP":
                loops.append(self.parse_loop_block())
            elif token_type == "IF":
                ifs.append(self.parse_if_block())
            elif token_type == "CHORD":
                chords.append(self.parse_chord())
            elif token_type == "PLAY":
                plays.append(self.parse_play_stmt())
            else:
                raise Exception(f"Token inesperado: {token_type}")

        self.eat("RBRACE")

        return MusicNode(nome, bpm, varials, instrumentos, loops, ifs, chords, plays)

    

    def parse_varials_block(self):
        #print("novo bloco VARIALS \n################################################ ")
        self.eat("VARIALS")
        self.eat("LBRACE")
        
        varials = []
        while self.current_token() and self.current_token().type == "ID":
            varial_node = self.parse_assignment()
            #print(f"valor no block: {varial_node.value}")
            #print(f"nome no block: {varial_node.name}")
            varials.append(varial_node)
        
        self.eat("RBRACE")
        return VarialsBlockNode(varials) 

    def parse_assignment(self):
        var_name = self.eat("ID")  # supondo que eat retorna o valor do token
        self.eat("ASSIGN")
        
        if self.current_token().type == "NUMBER":
            value = self.eat("NUMBER")
            #print(f"{var_name} = {value}")
        elif self.current_token().type == "LBRACK":
            self.eat("LBRACK")
            numbers = [self.eat("NUMBER")]
            while self.current_token().type == "COMMA":
                self.eat("COMMA")
                numbers.append(self.eat("NUMBER"))
            self.eat("RBRACK")
            #print(f"{var_name} = {numbers}")
            value = numbers
        else:
            raise Exception("Valor inválido em assignment")

        return VarialsNode(var_name, value)



    def parse_instrument_block(self):
        self.eat("INSTRUMENT")
        instrument_name = self.eat("ID").value
        canal = int(self.eat("NUMBER").value)
        
        self.instrumento_atual = InstrumentNode(instrument_name, canal)  # salva instrumento ativo

        self.eat("LBRACE")
        while self.current_token() and self.current_token().type != "RBRACE":
            token = self.current_token()
            if token.type == "PLAY":
                self.parse_play_stmt()
            elif token.type == "CHORD":
                self.parse_chord_stmt()
            elif token.type == "LOOP":
                self.parse_loop_block()
            elif token.type == "IF":
                self.parse_if_block()
            elif token.type == "ID" and self.peek().type == "PLUS_ASSIGN":
                self.parse_inc_stmt()
            else:
                raise Exception(f"Instrução inesperada: {token}")
        self.eat("RBRACE")

        # Finaliza e salva no contexto (ou em lista, dependendo do seu parser)
        self.instrumento_atual.finalize()
        self.count += 1
        return self.instrumento_atual
    

    def parse_play_stmt(self):
        self.eat("PLAY")
        nota = self.parse_expression()
        duracao = self.parse_expression()
        #print(f'esse é o canal: {self.instrumento_atual.canal}')
        node = PlayNode(nota, duracao, self.instrumento_atual.canal)
        self.instrumento_atual.add_event("note", node)

    def parse_chord_stmt(self):
        self.eat("CHORD")

        if self.current_token().type == "LBRACK":
            self.eat("LBRACK")
            notas = []
            while True:
                nota = self.parse_expression()
                notas.append(nota)
                if self.current_token().type == "COMMA":
                    self.eat("COMMA")
                elif self.current_token().type == "RBRACK":
                    self.eat("RBRACK")
                    break
                else:
                    raise Exception("Esperado vírgula ou colchete de fechamento")
        else:
            notas = self.eat("ID").value  # apenas o nome da variável

        duracao = self.parse_expression()
        #print(f'parse chord: {notas}')
        node = ChordNode(notas, duracao, canal=self.instrumento_atual.canal)
        self.instrumento_atual.add_event("chord", node)


    def parse_inc_stmt(self):
        var = self.eat("ID")
        self.eat("PLUS_ASSIGN")
        value = self.eat("NUMBER")
        #print(f"{var.value} += {value.value}")

    def parse_loop_block(self):
        #print("novo bloco LOOP \n################################################ ")
        self.eat("LOOP")

        loop_id = self.eat("ID").value
        repeat_count = int(self.eat("NUMBER").value)  # número de repetições

        self.eat("LBRACE")

        # Armazenar instruções dentro do loop
        loop_instructions = []
        while self.current_token() and self.current_token().type != "RBRACE":
            token = self.current_token()
            if token.type == "IF":
                loop_instructions.append(('if', self.current_token()))  # opcional, depende do seu uso
                self.parse_if_block()
            elif token.type == "PLAY":
                self.eat("PLAY")
                note = self.parse_expression()
                duration = self.parse_expression()
                loop_instructions.append(('play', note, duration))
            elif token.type == "CHORD":
                self.eat("CHORD")
                if self.current_token().type == "LBRACK":
                    self.eat("LBRACK")
                    notas = []
                    while True:
                        nota = self.parse_expression()
                        notas.append(nota)
                        if self.current_token().type == "COMMA":
                            self.eat("COMMA")
                        elif self.current_token().type == "RBRACK":
                            self.eat("RBRACK")
                            break
                        else:
                            raise Exception("Esperado vírgula ou colchete de fechamento")
                else:
                    notas = self.parse_expression()  # <-- ID passado direto!

                duracao = self.parse_expression()
                loop_instructions.append(('chord', notas, duracao))
                
        self.eat("RBRACE")

        # Agora executar o loop N vezes
        for _ in range(repeat_count):
            for instr in loop_instructions:
                tipo, *args = instr
                if tipo == 'play':
                    note, duracao = args    
                    #print(f"loop block play {note}")
                    #print(f'esse é o canal LOOP play: {self.instrumento_atual.canal}')
                    node = PlayNode(note, duracao, self.instrumento_atual.canal)
                    self.instrumento_atual.add_event("note", node)
                elif tipo == 'chord':
                    notas, duracao = args
                    #print(f"loop block chord{notas}")
                    #print(f'esse é o canal LOOP chord: {self.instrumento_atual.canal}')
                    node = ChordNode(notas, duracao, canal=self.instrumento_atual.canal)
                    self.instrumento_atual.add_event("chord", node)


    def parse_if_block(self):
        #print("novo bloco IF \n################################################ ")
        self.eat("IF")
        self.parse_condition()
        self.eat("LBRACE")
        while self.current_token() and self.current_token().type != "RBRACE":
            if self.current_token().type == "PLAY":
                self.parse_play_stmt()
        self.eat("RBRACE")

    def parse_condition(self):
        left = self.eat("ID").value
        op = self.eat(self.current_token().type).value
        right = self.parse_expression()
        #print(f"condição: {left} {op} {right}")

    def peek(self):
        return self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else Token("EOF", "")





#########################################################################################################################
# Main

def main():
    if len(sys.argv) != 2:
        print("Uso: python classes.py arquivo.music")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith('.music'):
        print("Erro: o arquivo deve ter extensão .music")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Erro: arquivo '{filename}' não encontrado.")
        sys.exit(1)

    tokenizer = Tokenizer(content)
    parser = Parser(tokenizer)

    music_node = parser.parse_program()  # agora retorna o nó Music

    context = {}  # contexto inicial vazio

    music_node.evaluate(context)  # chama Evaluate para gerar o .mid
    #build_midi_sequencial(context, bpm=music_node.bpm)
    print(context)
    criar_midi_com_duracoes(context, music_node.bpm, music_node.nome, music_node.instrumentos, instrument_map)

if __name__ == "__main__":
    main()
