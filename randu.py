class Randu:
    """The infamous RANDU algorithm
    wikipedia: http://en.wikipedia.org/wiki/RANDU
    """

    #Variables for the general formula x(i+1) = A + Bx(i) mod M
    _seed = 0
    _M = 2**31
    _A = 0
    _B = 65539
    
    def __init__(self, seed):
        self._seed = seed
        self._sequencer = self.sequencer()
                        
    def sequencer(self):
        out = self._seed
        while True:
            out = self._A + ((self._B * out) % self._M)
            yield out

    def __iter__(self):
        return self

    def next(self):
        return self._sequencer.next()

    

    
        
