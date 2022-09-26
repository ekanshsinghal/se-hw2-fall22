def getHelp(key):
    out = {
    'help': "CSV : summarized csv file\n(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\nUSAGE: lua seen.lua [OPTIONS]\nOPTIONS:\n -e  --eg        start-up example                      = nothing\n -d  --dump      on test failure, exit with stack dump = false\n -f  --file      file with csv data                    = ../data/auto93.csv\n -h  --help      show help                             = false\n -n  --nums      number of nums to keep                = 512\n -s  --seed      random number seed                    = 10019\n -S  --Seperator feild seperator                       = ,\n"
}
    return out[key]