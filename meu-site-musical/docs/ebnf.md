
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