import random


# Hareket listesi
movesB = ['left', 'no-op', 'right']
movesA = ['no-op', 'right']
movesC = ['left', 'no-op']

def main(p1, p2, p3):
    Agent_A_score = 0
    Agent_B_score = 0

    A = 'D'
    B = 'D'
    C = 'D'
    position = 'B'



    with open('a.txt', 'w') as Agent_A, open('b.txt', 'w') as Agent_B:
        for time_step in range(1000):
            Agent_A.write(f'{position}, {A}, {B}, {C}\n')
            Agent_B.write(f'{position}, {A}, {B}, {C}\n')

            if position == 'B':
                if  B == 'D':
                    action = 'suck'
                else:
                    action = random.choice(movesB)
                if action == 'suck':
                    B = 'C'
                elif action == 'left':
                    position = 'A'
                    Agent_B_score -= 0.5
                elif action == 'right':
                    position = 'C'
                    Agent_B_score -= 0.5

            elif position == 'A':
                if A == 'D':
                    action = 'suck'
                else:
                    action = random.choice(movesA)
                if action == 'suck':
                    A = 'C'
                elif action == 'right':
                    position = 'B'
                    Agent_B_score -= 0.5
            else:
                if  C == 'D':
                    action = 'suck'
                else:
                    action = random.choice(movesC)
                if action == 'suck':
                    C = 'C'
                elif action == 'left':
                    position = 'B'
                    Agent_B_score -= 0.5

            # Puan güncellemeleri
            def update_scores(agent_a_score, agent_b_score, room_states):
                for room_state in room_states:
                    if room_state == 'C':
                        agent_a_score += 1
                        agent_b_score += 1
                return agent_a_score, agent_b_score

            Agent_A_score, Agent_B_score = update_scores(Agent_A_score, Agent_B_score, [A, B, C])

            # İşlem ve durumları dosyaya yazma
            def write_to_file(agent_file, action, position, A, B, C, agent_score):
                agent_file.write(action + '\n')
                agent_file.write(f'{position}, {A}, {B}, {C}\n')
                agent_file.write(str(agent_score) + '\n')

            write_to_file(Agent_A, action, position, A, B, C, Agent_A_score)
            write_to_file(Agent_B, action, position, A, B, C, Agent_B_score)

            # Odaların durum güncellemeleri
            def update_room_states(room_state, probability):
                if room_state == 'C' and random.random() <= probability:
                    return 'D'
                return room_state

            # Odaların durum güncellemeleri
            A = update_room_states(A, p1)
            B = update_room_states(B, p2)
            C = update_room_states(C, p3)


if __name__ == '__main__':
    pA = float(input("Enter the probability of contamination of room A (0-1): "))
    pB = float(input("Enter the probability of contamination of room B (0-1): "))
    pC = float(input("Enter the probability of contamination of room C (0-1): "))
    main(pA, pB, pC)
