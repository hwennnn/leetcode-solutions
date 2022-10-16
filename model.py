class Problem:
    def __init__(self, problemId, problemName, slug, normalizedProblemName, solutions, isPremium, difficulty):
        self.id = problemId
        self.name = problemName
        self.slug = slug
        self.normalizedProblemName = normalizedProblemName
        self.solutions = solutions
        self.isPremium = isPremium
        self.difficulty = difficulty
