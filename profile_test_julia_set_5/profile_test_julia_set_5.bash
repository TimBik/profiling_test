python -m cProfile -o profile.stats ../julia_set/calculate_set_1.py
sleep 2
python stats_reader.py