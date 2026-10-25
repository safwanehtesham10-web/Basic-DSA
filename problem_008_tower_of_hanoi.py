def solve_hanoi(count, src, aux, target):
    if count == 0:
        return
    solve_hanoi(count - 1, src, target, aux)
    print(f"Move disk {count} from {src} to {target}")
    solve_hanoi(count - 1, aux, src, target)

solve_hanoi(3, 'A', 'B', 'C')
