#!/usr/bin/env bash
halcmd -s show pin | grep '==' > pin.out
python hal_sigs_graphviz.py > laser.dot
dot -Tsvg laser.dot > laser.svg
