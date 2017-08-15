########################################
# CS/CNS/EE 155 2017
# Problem Set 5
#
# Author:       Avishek Dutta
# Description:  Set 5
########################################

class Utility:
    '''
    Utility for the problem files.
    '''

    def __init__():
        pass

    @staticmethod
    def load_poem():
            '''
            Loads the file 'shake_words.txt'.

            Returns:
                states:      Sequnces of states, i.e. a list of lists.
                            Each sequence represents half a year of data.
                states_map:   A hash map that maps each state to an integer.
                observations:     Sequences of observations, i.e. a list of lists.
                            Each sequence represents half a year of data.
                observation_map:  A hash map that maps each observation to an integer.
            '''
            states = []
            states_map = {}
            observations = []
            observation_map = {}
            state_counter = 0
            observation_counter = 0

            with open("shake_words.txt") as f:
                state_seq = []
                observation_seq = []

                while True:
                    line = f.readline().strip()

                    if line == '' or line == '-':
                        # A line has been read. Add the current sequence to
                        # the list of sequences.
                        states.append(state_seq)
                        observations.append(observation_seq)
                        # Start new sequences.
                        state_seq = []
                        observation_seq = []

                    # end of file
                    if line == '':
                        break
                    # onto next line
                    elif line == '-':
                        continue

                    st, obs = line.split()

                    # Add new states to the st state hash map.
                    if st not in states_map:
                        states_map[st] = state_counter
                        state_counter += 1

                    state_seq.append(states_map[st])

                    # Add new observations to the obs observation hash map.
                    if obs not in observation_map:
                        observation_map[obs] = observation_counter
                        observation_counter += 1

                    # Convert the obs into an integer.
                    observation_seq.append(observation_map[obs])

            return states, states_map, observations, observation_map

    @staticmethod
    def load_poem_hidden():
        '''
        Loads the file 'shake_words.txt' and hides the states.

        Returns:
            genres:     The observations.
            genre_map:  A hash map that maps each observation to an integer.
        '''
        states, states_map, observations, observation_map = Utility.load_poem()
        return observations, observation_map
