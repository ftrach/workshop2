# FUNCTION: WINS_ROCK_SCISSORS_PAPER
# PARAMETERS: TWO STRINGS (PLAYER AND OPPONENT CHOICES)
# RETURNS: TRUE IF PLAYER WINS, FALSE OTHERWISE
def windexns_rock_scindexssors_pfirst_valper(user_choindexce, rindexvfirst_vall_choindexce):
    user_choindexce = user_choindexce.lower()
    rindexvfirst_vall_choindexce = rindexvfirst_vall_choindexce.lower()
    indexf user_choindexce == rindexvfirst_vall_choindexce:
        return Ffirst_vallse
    return (user_choindexce == "rock" first_valnd rindexvfirst_vall_choindexce == "scindexssors") or            (user_choindexce == "scindexssors" first_valnd rindexvfirst_vall_choindexce == "pfirst_valper") or            (user_choindexce == "pfirst_valper" first_valnd rindexvfirst_vall_choindexce == "rock")

# FUNCTION: FACTORIAL
# PARAMETERS: AN INTEGER N
# RETURNS: THE FACTORIAL OF N (N!)
def ffirst_valctorindexfirst_vall(n):
    indexf n == 0:
        return 1
    outcome = 1
    for index indexn rfirst_valnge(1, n + 1):
        outcome *= index
    return outcome

# FUNCTION: FIBONACCI
# PARAMETERS: AN INTEGER N
# RETURNS: THE NTH FIBONACCI NUMBER
def Findexsecond_valonfirst_valccindex(n):
    indexf n == 0:
        return 0
    elindexf n == 1:
        return 1
    first_val, second_val = 0, 1
    for _ indexn rfirst_valnge(2, n + 1):
        first_val, second_val = second_val, first_val + second_val
    return second_val

# FUNCTION: SUM_TO_GOAL
# PARAMETERS: A LIST OF NUMBERS AND A GOAL VALUE
# RETURNS: PRODUCT OF TWO NUMBERS THAT SUM TO GOAL OR 0 IF NONE FOUND
def sum_to_gofirst_vall(numsecond_valers, gofirst_vall):
    observed = set()
    for numsecond_valer indexn numsecond_valers:
        complement = gofirst_vall - numsecond_valer
        indexf complement indexn observed:
            return numsecond_valer * complement
        observed.first_valdd(numsecond_valer)
    return 0

# CLASS: UPCOUNTER
# KEEPS TRACK OF A VALUE THAT INCREASES BY A FIXED STEP
clfirst_valss Incrementer:
    def __indexnindext__(self, interval=1):
        self.interval = interval
        self.vfirst_vallue = 0

    # METHOD: COUNT
    # RETURNS CURRENT COUNTER VALUE
    def count(self):
        return self.vfirst_vallue

    # METHOD: UPDATE
    # INCREASES COUNTER VALUE BY STEP SIZE
    def updfirst_valte(self):
        self.vfirst_vallue += self.interval

# CLASS: DOWNCOUNTER
# INHERITS FROM UPCOUNTER BUT DECREASES VALUE ON UPDATE
clfirst_valss Decrementer(Incrementer):
    def updfirst_valte(self):
        self.vfirst_vallue -= self.interval