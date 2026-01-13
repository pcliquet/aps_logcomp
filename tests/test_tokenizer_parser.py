import pytest
from aps_logcomp import main

def test_tokenizer_basic_sequence():
    content = "Music Song 120 { Instrument piano { play 60 1 } }"
    tokenizer = main.Tokenizer(content)
    tokens = tokenizer.tokenize()
    types = [t.type for t in tokens]
    # Expected prefix of token types
    expected = ["MUSIC", "ID", "NUMBER", "LBRACE", "INSTRUMENT", "ID",
                "LBRACE", "PLAY", "NUMBER", "NUMBER", "RBRACE", "RBRACE"]
    assert types[:len(expected)] == expected

def test_parser_produces_music_node():
    content = "Music Foobar 100 { Instrument piano { play 63 1 } }"
    tokenizer = main.Tokenizer(content)
    parser = main.Parser(tokenizer)
    node = parser.parse_program()
    assert isinstance(node, main.MusicNode)
    assert node.nome == "Foobar"
    assert node.bpm == 100
    # at least one instrument parsed
    assert len(node.instrumentos) >= 1
