class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initialState = None
        self.finalStates = set()

    def addTransition(self, state, symbol, nextState):
        self.states.add(state)
        self.states.add(nextState)
        self.alphabet.add(symbol)
        if state not in self.transitions:
            self.transitions[state] = {}
        self.transitions[state][symbol] = nextState

    def setInitialState(self, state):
        self.initialState = state

    def addFinalState(self, state):
        self.finalStates.add(state)

    def getStates(self):
        return self.states

    def getAlphabet(self):
        return self.alphabet

    def getTransitions(self):
        return self.transitions

    def getInitialState(self):
        return self.initialState

    def getFinalStates(self):
        return self.finalStates
