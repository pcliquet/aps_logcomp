import os
from aps_logcomp import main

def test_integration_generate_midi(tmp_path):
    # Minimal music: one instrument, one play
    content = "Music X 100 { Instrument piano { play 60 1 } }"
    tokenizer = main.Tokenizer(content)
    parser = main.Parser(tokenizer)
    music_node = parser.parse_program()

    # Build context by evaluating nodes (this populates context["instrumentos"])
    context = {}
    music_node.evaluate(context)

    # instrument map: piano -> GM program 0
    instrument_map = {"piano": 0}

    out_base = tmp_path / "out_test"
    # criar_midi_com_duracoes writes {nome}.mid, so pass a path-like name
    out_name = str(out_base)

    # call the function under test
    main.criar_midi_com_duracoes(context, music_node.bpm, out_name, music_node.instrumentos, instrument_map)

    out_file = out_base.with_suffix(".mid")
    assert out_file.exists(), "MIDI file was not created"
    assert out_file.stat().st_size > 0, "MIDI file size is zero"
