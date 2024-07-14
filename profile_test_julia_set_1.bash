python -m timeit -n 5 -r 1 -s "from julia_set import calculate_set_1" \
"set_1.calc_pure_python(desired_width=1000, max_iterations=300)"