class GrammarAnalyzer:
    def __init__(self, non_terminals, terminals, start_symbol, productions):
        self.nt = non_terminals
        self.t = terminals
        self.start = start_symbol
        self.prods = productions
        self.first = {X: set() for X in self.nt | self.t}
        self.follow = {X: set() for X in self.nt}
        self.predict = {}
        
        for terminal in self.t:
            self.first[terminal].add(terminal)
        self.first['epsilon'] = {'epsilon'}

    def get_first_of_sequence(self, sequence):
        result = set()
        if not sequence:
            result.add('epsilon')
            return result
            
        for symbol in sequence:
            symbol_first = self.first[symbol]
            result |= (symbol_first - {'epsilon'})
            if 'epsilon' not in symbol_first:
                break
        else:
            result.add('epsilon')
        return result

    def compute_first(self):
        changed = True
        while changed:
            changed = False
            for head, bodies in self.prods.items():
                for body in bodies:
                    seq_first = self.get_first_of_sequence(body)
                    if not seq_first.issubset(self.first[head]):
                        self.first[head] |= seq_first
                        changed = True

    def compute_follow(self):
        self.follow[self.start].add('$')
        changed = True
        while changed:
            changed = False
            for head, bodies in self.prods.items():
                for body in bodies:
                    for i, symbol in enumerate(body):
                        if symbol in self.nt:
                            beta = body[i+1:]
                            beta_first = self.get_first_of_sequence(beta)
                            
                            new_follow = beta_first - {'epsilon'}
                            if not new_follow.issubset(self.follow[symbol]):
                                self.follow[symbol] |= new_follow
                                changed = True
                            
                            if 'epsilon' in beta_first or not beta:
                                if not self.follow[head].issubset(self.follow[symbol]):
                                    self.follow[symbol] |= self.follow[head]
                                    changed = True

    def compute_predict(self):
        for head, bodies in self.prods.items():
            for body in bodies:
                rule_str = f"{head} -> {' '.join(body) if body != ['epsilon'] else 'epsilon'}"
                first_alpha = self.get_first_of_sequence(body)
                
                predict_set = first_alpha - {'epsilon'}
                if 'epsilon' in first_alpha:
                    predict_set |= self.follow[head]
                
                self.predict[rule_str] = predict_set

    def run_all(self):
        self.compute_first()
        self.compute_follow()
        self.compute_predict()

    def print_results(self, title):
        print(f"\n{'='*40}\n{title}\n{'='*40}")
        print("\n--- CONJUNTOS DE PRIMEROS ---")
        for x in self.nt:
            print(f"PRIMEROS({x}) = {self.first[x]}")
            
        print("\n--- CONJUNTOS DE SIGUIENTES ---")
        for x in self.nt:
            print(f"SIGUIENTES({x}) = {self.follow[x]}")
            
        print("\n--- CONJUNTOS DE PREDICCIÓN ---")
        for rule, pred in self.predict.items():
            print(f"PRED({rule}) = {pred}")


terminals_1 = {'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis'}
non_terminals_1 = {'S', 'A', 'B', 'C', 'D'}
prods_1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['epsilon']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['epsilon']],
    'C': [['cinco', 'D', 'B'], ['epsilon']],
    'D': [['seis'], ['epsilon']]
}

analizador_1 = GrammarAnalyzer(non_terminals_1, terminals_1, 'S', prods_1)
analizador_1.run_all()
analizador_1.print_results("RESULTADOS EJERCICIO 1")


terminals_2 = {'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis'}
non_terminals_2 = {'S', 'A', 'B', 'C', 'D'}
prods_2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['epsilon']],
    'B': [['C', 'D'], ['tres'], ['epsilon']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['epsilon']]
}

analizador_2 = GrammarAnalyzer(non_terminals_2, terminals_2, 'S', prods_2)
analizador_2.run_all()
analizador_2.print_results("RESULTADOS EJERCICIO 2")
